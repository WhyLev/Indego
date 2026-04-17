"""System health integration for Indego."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components import system_health
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


@callback
def async_register(
    hass: HomeAssistant, register: system_health.SystemHealthRegistration
) -> None:
    """Register system health callback."""
    register.async_register_info(system_health_info)


async def system_health_info(hass: HomeAssistant) -> dict[str, Any]:
    """Get system health information."""
    from .const import ENTITY_ONLINE

    info: dict[str, Any] = {
        "can_reach_bosch_api": system_health.async_check_can_reach_url(
            hass,
            "https://api.indego.bosch-home.com/api/v1/alms",
        ),
        "can_reach_auth_service": system_health.async_check_can_reach_url(
            hass,
            "https://prodindego.b2clogin.com/",
        ),
    }

    # Get mower status from active instances
    try:
        if DOMAIN in hass.data and hass.data[DOMAIN]:
            hub = None
            # Get first active hub
            for entry_id, instance in hass.data[DOMAIN].items():
                if entry_id != "health_registered" and hasattr(instance, "entities"):
                    hub = instance
                    break

            if hub:
                # Bosch service status
                service_status = "ok" if not hub._last_service_error else "error"
                service_value = (
                    "OK"
                    if not hub._last_service_error
                    else f"Last error: {hub._last_service_error}"
                )

                info["bosch_service_status"] = {
                    "type": service_status,
                    "status": service_status,
                    "value": service_value,
                }

                # Mower online status
                online_entity = hub.entities.get(ENTITY_ONLINE)
                if online_entity:
                    is_online = online_entity.state
                    info["mower_online"] = {
                        "type": "boolean" if isinstance(is_online, bool) else "string",
                        "status": "ok" if is_online else "unknown",
                        "value": "Online" if is_online else "Offline",
                    }

                # Last API response time
                if hub._last_successful_update:
                    import time

                    seconds_ago = int(time.time() - hub._last_successful_update)
                    if seconds_ago < 60:
                        time_str = f"{seconds_ago} seconds ago"
                    elif seconds_ago < 3600:
                        minutes_ago = seconds_ago // 60
                        time_str = f"{minutes_ago} minutes ago"
                    else:
                        hours_ago = seconds_ago // 3600
                        time_str = f"{hours_ago} hours ago"

                    response_status = (
                        "ok" if seconds_ago < 600 else "warning"
                    )  # 10 minutes warning threshold
                    info["last_api_response"] = {
                        "type": "string",
                        "status": response_status,
                        "value": time_str,
                    }

    except Exception as err:
        _LOGGER.warning("Error gathering system health info: %s", err)

    return info


