"""Error code mappings for Bosch Indego mowers."""

# Common Indego error codes and their descriptions
ERROR_CODE_MAP = {
    # No error
    "0": "No error",

    # Internal/System errors (40-70)
    "45": "Unknown internal error",
    "55": "Button cell almost empty",
    "57": "Compass error",
    "58": "No data from mobile module",
    "60": "Mower tilted",

    # Wheel/Motor/Sensor errors (100-220)
    "101": "Mower was lifted",
    "102": "Lift sensor right front steering wheel",
    "103": "Lift sensor left front steering wheel",
    "104": "Stop button pressed",
    "105": "Mower tilted >45°",
    "106": "Invalid input",
    "107": "System error",
    "108": "System error",
    "109": "System error",
    "115": "Permanent tactile detected",
    "126": "Charging current/voltage too high",
    "127": "Charging current/voltage too high",
    "129": "Cutter load too high",
    "130": "Cutter load too high",
    "131": "Cutter load too high",
    "133": "Internal error",
    "134": "Internal error",
    "136": "Left wheel blocked",
    "137": "Right wheel blocked",
    "142": "Internal wheel drive error",
    "143": "Intermittent error",

    # Perimeter/Wire errors (149-194)
    "149": "Mower out of perimeter limit",
    "150": "No signal from perimeter wire",
    "151": "Waiting for loop signal",
    "162": "Charging error",
    "194": "No perimeter signal detected",

    # Drive errors (216)
    "216": "Left wheel stuck",

    # Navigation/Stuck errors (700-799)
    "701": "Mower stuck",
    "702": "Mower trapped",
    "703": "Mower too high",
    "704": "Unable to proceed",
    "705": "Uneven ground",
    "706": "Grass too high",

    # Communication errors (800-899)
    "801": "Bluetooth error",
    "802": "WiFi connection lost",
    "803": "API connection error",
    "804": "No connection to server",
    "805": "Communication timeout",

    # Firmware/Software errors (900-999)
    "901": "Firmware error",
    "902": "Software error",
    "903": "Configuration error",
    "904": "Memory error",

    # Battery/System errors (1100+)
    "1138": "Last run error",
    "1146": "Orientation filter error",
    "1156": "Unsupported battery pack",

    # System errors (1000+)
    "1000": "System error",
    "1001": "Unknown error",
    "1002": "Shutdown detected",
    "1008": "Mower is stuck",
}

def get_error_description(error_code: str) -> str:
    """Get error description from error code.

    Args:
        error_code: Error code as string

    Returns:
        Error description or "Unknown error" if not found
    """
    return ERROR_CODE_MAP.get(str(error_code), f"Unknown error code: {error_code}")
