[![GitHub release](https://img.shields.io/github/release/sander1988/Indego.svg)](https://github.com/sander1988/Indego/releases/) [![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

# Bosch Indego Mower

**Home Assistant Custom Component for Bosch Indego robotic lawn mowers**

A comprehensive Home Assistant integration that provides full control and monitoring of your Bosch Indego lawn mower. Get real-time status, battery information, mowing schedules, and more.

![Sensors in Home Assistant](/doc/01_sensors.png)
![Diagnostics in Home Assistant](/doc/02_diagnostics.png)

## ✨ Features

- 🎮 **Full Mower Control** - Start, pause, dock, and schedule mowing
- 📊 **Real-time Monitoring** - Battery, location, alerts, and more
- 📍 **Lawn Mapping** - Visual SVG map with mower position overlay (dynamic streaming based on movement)
- 🤖 **SmartMowing Switch** - Toggle automatic schedule optimization based on weather
- ⚠️ **Alert Management** - Monitor and manage mower alerts with action buttons and complete error list extraction
- 🌍 **Multi-language Support** - German, English, Dutch, French, Spanish, Italian, Danish, Norwegian, Polish, Swedish, Slovak, and more
- 🏠 **Native Entities** - Lawn Mower and Vacuum entities for seamless Home Assistant integration
- 📱 **Multiple Mowers** - Support for multiple mowers in one Home Assistant instance
- 🔌 **Service Monitoring** - Bosch Cloud API availability detection with HTTP 5xx error tracking
- 🔋 **Advanced Battery Info** - Detailed battery metrics (voltage, temperature, cycles, discharge)
- 🛡️ **Intelligent Offline Detection** - 3-layer system (error codes, timeout, successful updates)
- 📍 **Stuck Detection** - Automatic detection when mower is immobilized (> 60 seconds without movement)
- 👤 **Custom User Agent** - Configurable User-Agent for API requests to work around Bosch restrictions
- 📈 **Session Tracking** - Counter for completed mowing sessions
- 🎯 **Dynamic Camera Streaming** - Camera shows as streaming when mower is actively moving/mowing
- 🔲 **Alert Action Buttons** - Quick action buttons to manage specific alerts

## 📖 Table of Contents

- [Features](#-features)
- [Community](#-community)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Monitored Entities](#-monitored-entities)
- [Advanced Features](#-advanced-features)
- [Debugging](#-debugging)
- [Supported Models](#-supported-models)
- [Known Issues](#️-known-issues)
- [Contribution & Support](#-contribution--support)
- [Credits](#-credits)

## 💬 Community

Join our Discord community to discuss features, vote on improvements, and get support:
[discord.gg/aD33GsP](https://discord.gg/aD33GsP)

## Installation

**HACS NOT AVAILABLE YET**
<s>
### Option 1: Via HACS (Recommended)

1. Add this repository to HACS (Community Store)
2. Search for "Bosch Indego"
3. Click "Install"
4. Restart Home Assistant

[HACS Repository](https://hacs.xyz/)
</s>

### Option 2: Manual Installation

1. Copy the `indego` folder from `custom_components` to your Home Assistant `custom_components` folder
2. Restart Home Assistant

## Getting Started

### 1. Install Chrome Extension (Required for Authentication)

Bosch Indego uses OAuth authentication (Bosch SingleKey ID). To complete authentication, you need a Chrome extension:

1. Download: [HomeAssistant Indego authentication helper](/chrome-extension.zip)
2. Extract the ZIP file
3. Go to `chrome://extensions/` in Google Chrome
4. Enable **Developer mode** (top right)
5. Click **Load unpacked** and select the extracted folder
6. ✅ You can disable the extension after setup if you prefer

**Note:** Currently only Google Chrome supports the Bosch authentication flow.

### 2. Add the Integration

1. In Home Assistant: **Settings → Devices & Services → Create Integration**
2. Search for **"Bosch Indego"**
3. Click **Create**
4. Follow the authentication flow (uses the Chrome extension above)
5. All sensors will appear as "Unused Entities" after setup

**You can add this integration multiple times if you own multiple mowers.**

### 3. Configuration Options (Optional)

After adding the integration, you can enable additional features in **Settings → Devices & Services → Bosch Indego → Configure**:

- **Custom User Agent** - Useful if Bosch Cloud is blocking requests. Try alternatives like `HomeAssistant/Indego` or `HA/Indego`
- **Expose as Lawn Mower** - Enable native Home Assistant Lawn Mower entity (recommended for automation compatibility)
- **Expose as Vacuum** - Enable legacy Vacuum entity for backward compatibility
- **Show All Alerts** - Store all historical alerts (use sparingly due to Entity Registry limits)

## 📊 Monitored Entities

All sensors are automatically discovered after setup and will appear as "Unused Entities" in Home Assistant.

### Mowing Status

| Sensor | Description |
|--------|-------------|
| **Mower State** | Current state of the mower (e.g., mowing, paused, charging) |
| **State Detail** | Detailed state information with more context |
| **Lawn Mowed** | Percentage of lawn mowed (%) |
| **Total Mowing Time** | Total cumulative mowing time (hours) |
| **Session Count** | Total number of completed mowing sessions |

### Battery & Charging

| Sensor | Description |
|--------|-------------|
| **Battery Level** | Current battery charge (%) |
| **Battery Voltage** | Battery voltage (V) - diagnostic |
| **Battery Temperature** | Battery cell temperature (°C) - diagnostic |
| **Ambient Temperature** | Ambient air temperature (°C) - diagnostic |
| **Battery Cycles** | Battery charge cycles count - diagnostic |
| **Battery Discharge** | Battery discharge capacity (Ah) - diagnostic |

### Location & Movement

| Sensor | Description |
|--------|-------------|
| **Mower Position X** | X coordinate on map (pixels) |
| **Mower Position Y** | Y coordinate on map (pixels) |
| **Mower Stuck** | Binary sensor - indicates if mower is stuck |
| **Garden Size** | Total lawn area (m²) |

### Alerts & Maintenance

| Sensor | Description |
|--------|-------------|
| **Alerts** | Active alert status with count, last message, and **complete error list** with codes and timestamps |
| **Last Error** | Last error code and timestamp with error description |
| **Firmware Version** | Current firmware version |
| **Maintenance Hours** | Maintenance counter (hours) with status (good/service_due_soon/service_required) |
| **Service Status** | Bosch Cloud API availability - detects HTTP 5xx errors with last error timestamp |

### Other Information

| Sensor | Description |
|--------|-------------|
| **Mowing Mode** | Current mowing mode setting |
| **Online Status** | Whether mower is connected (True/False) - with intelligent 3-layer offline detection |
| **Update Available** | Firmware update availability (On/Off) |
| **Last Completed Mow** | Last full lawn mowing completion time |
| **Next Mow Time** | Scheduled next mowing time |
| **Lawn Mowed Size** | Absolute lawn area mowed in current session (m²) |
| **Session Count** | Total number of completed mowing sessions |
| **Lawn Mower Entity** | Native Home Assistant Lawn Mower entity (Start, Pause, Dock) |
| **Vacuum Entity** | Legacy Home Assistant Vacuum entity (Start, Pause, Return, Battery) |
| **Lawn Map** | SVG lawn map with mower position overlay with dynamic streaming state |

### Switches

| Switch | Description |
|--------|-------------|
| **SmartMowing** | Toggle SmartMowing mode on/off - enables automatic schedule optimization based on weather conditions |

### Buttons

| Button | Description |
|--------|-------------|
| **Delete Alert** | Action button to delete specific alerts from the mower |
| **Mark Alert as Read** | Action button to mark specific alerts as read |


## 🔍 Advanced Features

### Complete Error List in Alert Sensor Attributes

The `binary_sensor.indego_<SERIAL>_alert` sensor stores all active mower alerts as individual attributes, making it easy to extract and display errors in Home Assistant automations:

**Available Attributes (for each alert):**
- `error_0` - Complete error format: `"802: WiFi connection lost - 2024-01-01 12:34:56"`
- `error_0_code` - Error code only: `"802"`
- `error_0_description` - Error description: `"WiFi connection lost"`
- `error_0_timestamp` - Time of error: `"2024-01-01 12:34:56"`
- `error_0_message` - Original message from API
- `error_0_read` - Read status (True/False)


### Bosch Cloud Service Monitoring

The `binary_sensor.indego_<SERIAL>_service_status` sensor monitors the availability of Bosch Cloud API:

- **UP** (True) - Bosch API is responding normally
- **DOWN** (False) - Bosch Cloud is experiencing 5xx errors (usually temporary)
- **Attribute** `last_service_error` - Shows the HTTP error code (e.g., "HTTP 503")

**Note:** 5xx errors are typically temporary Bosch Cloud issues and resolve automatically.

### Intelligent Offline Detection (3-Layer System)

The integration uses a sophisticated 3-layer system to accurately detect when your mower is offline:

**Layer 1: Error Code Detection**
- Immediately marks mower as offline on API errors: 802, 803, 804 (connection failures)
- Provides instant feedback when mower loses connectivity

**Layer 2: Timeout System**
- After 300 seconds (5 minutes) without a successful API response, mower is marked offline
- Handles situations where the API doesn't return explicit error codes
- Automatically recovers when connectivity is restored

**Layer 3: Last Successful Update Tracking**
- Continuously tracks `_last_successful_update` timestamp
- Monitors refresh cycles to detect prolonged connection loss
- Works in conjunction with error codes and timeout system

**How It Works:**
1. Each successful API call updates the timestamp
2. Every refresh cycle checks for timeout or error conditions
3. If timeout exceeded OR error codes detected → mower state set to offline
4. Online state automatically restored when connection resumes

### SmartMowing Switch

Enable or disable SmartMowing directly from Home Assistant using the **SmartMowing** switch entity:

- **Switch Location**: `switch.indego_<SERIAL>_smartmowing`
- **State Detection**: Automatically detects SmartMowing status from mower's current mowing mode description
- **Manual Toggle**: Turn the switch on/off to enable/disable SmartMowing
- **Real-time Sync**: Switch state updates automatically based on mower's current settings

### Dynamic Camera Streaming

The lawn map camera entity provides dynamic streaming capabilities:

- **Streaming State**: Camera's `is_streaming` property indicates active mower movement
- **Movement Detection**: Automatically detects if mower is in a mowing, moving, or cutting state (states 500-799)
- **Map Updates**: SVG map reloads when mower movement is detected for fresh position data
- **Visual Feedback**: Streaming indicator in Home Assistant UI shows when mower is actively working

### Alert Action Buttons

Quick action buttons appear for managing mower alerts:

- **Delete Alert**: Button for removing specific alerts from the mower's alert history
- **Mark as Read**: Button for marking alerts as read without deleting them

These buttons can be used in automations or dashboards for quick alert management.

### Multilingual Support

The integration includes translations for the following languages:
- German (Deutsch)
- English
- Dutch (Nederlands)
- French (Français)
- Spanish (Español)
- Italian (Italiano)
- Danish (Dansk)
- Norwegian (Norsk)
- Polish (Polski)
- Swedish (Svenska)
- Slovak (Slovenčina)

Language selection is handled automatically by Home Assistant based on your system settings.

### Stuck Detection

The integration automatically detects when your mower is stuck:

- **Binary Sensor**: `binary_sensor.indego_<SERIAL>_mower_stuck`
- **Detection**: Mower is marked as stuck if it doesn't move > 5 pixels for 60+ seconds while actively mowing
- **Attributes**:
  - `stuck_since` - Time when mower became stuck
  - `stuck_x` - X position (pixels)
  - `stuck_y` - Y position (pixels)



Control your mower through Home Assistant services. All services support multiple mowers via the `mower_serial` parameter.

### Send Command

**Service:** `indego.command`

Sends control commands to your mower.

**Parameters:**
- `command` (required): `mow` | `pause` | `returnToDock`
- `mower_serial` (optional): Serial number (only needed for multiple mowers)

**Example:**
```yaml
service: indego.command
data:
  command: mow
```

### SmartMowing Control

**Service:** `indego.smartmowing`

Enable or disable SmartMowing feature (automatic schedule adjustment based on weather and lawn growth).

**Parameters:**
- `enable` (required): `true` | `false`
- `mower_serial` (optional): Serial number (only needed for multiple mowers)

### Alert Management

#### Delete Specific Alert
**Service:** `indego.delete_alert`

**Parameters:**
- `alert_index` (required): 0 = most recent, 1 = second most recent, etc.
- `mower_serial` (optional)

#### Delete All Alerts
**Service:** `indego.delete_alert_all`

**Parameters:**
- `mower_serial` (optional)

#### Mark Alert as Read
**Service:** `indego.read_alert`

**Parameters:**
- `alert_index` (required): 0 = most recent, 1 = second most recent, etc.
- `mower_serial` (optional)

#### Mark All Alerts as Read
**Service:** `indego.read_alert_all`

**Parameters:**
- `mower_serial` (optional)

### Download Lawn Map

**Service:** `indego.download_map`

Downloads the current lawn map from Bosch Cloud API and saves as `www/indego_map_<SERIAL>.svg` in your Home Assistant configuration directory. Used by the camera entity.

**Parameters:**
- `mower_serial` (optional): Serial number (only needed for multiple mowers)

## 🐛 Debugging

To enable debug logging for troubleshooting, add this to your Home Assistant configuration:

```yaml
logger:
  logs:
    custom_components.indego: debug
    pyIndego: debug
```

Then check your logs in **Settings → System → Logs** for detailed debugging information.

## 📋 Supported Models

The integration supports the following Bosch Indego models:

- Indego 1000, 1100, 1200
- Indego 10C, 13C
- Indego 350, 400
- Indego S+ 350 (1st & 2nd Gen)
- Indego S+ 400 (1st & 2nd Gen)
- Indego S+ 500
- Indego M+ 700 (1st & 2nd Gen)

_Not seeing your model? Please [open an issue](https://github.com/sander1988/Indego/issues) to request support._

## ⚠️ Known Issues

1. **Chrome Extension Required**
   - A [Chrome extension](/chrome-extension.zip) is required to complete the authentication setup (Bosch SingleKey ID OAuth flow)
   - Can be disabled/removed after initial setup

2. **Bosch Cloud API Issues**
   - The Bosch Cloud (Azure) may occasionally block the integration: `HTTP 4XX` errors ("The connection to the Bosch Indego API failed!")
   - **Workaround:** Try changing the user agent during setup or in **Settings → Devices & Services → Bosch Indego Mower → Configure**

3. **Temporary Bosch Cloud Outages**
   - `HTTP 5XX` errors typically indicate temporary Bosch Cloud unavailability (often occurs once daily)
   - These are temporary and resolve automatically

4. **Invalid Commands**
   - Sending impossible commands (e.g., docking while already docked) may cause temporary `HTTP 5XX` errors from Bosch

## 💡 Contribution & Support

### Found a Bug or Have a Suggestion?

1. Check [existing issues](https://github.com/sander1988/Indego/issues) first
2. Open a [new issue](https://github.com/sander1988/Indego/issues/new) with:
   - Your mower model and firmware version
   - Steps to reproduce
   - Relevant logs (with debug enabled)
   - Screenshots if applicable

### Getting Help

- 📚 [Documentation & Issues](https://github.com/sander1988/Indego/issues)
- 💬 [Discord Community](https://discord.gg/aD33GsP)
- 📋 Services reference: **Developer Tools → Services** (search "Bosch Indego")

## 🙏 Credits

**Maintainers:** [@whylev](https://github.com/whylev), [@kimzeuner](https://github.com/kimzeuner), [@sander1988](https://github.com/sander1988)

**Contributors:**
[Eduard](https://github.com/eavanvalkenburg), [Jumper78](https://github.com/Jumper78), [dykandDK](https://github.com/dykandDK), [ultrasub](https://github.com/UltraSub), [Gnol86](https://github.com/Gnol86), naethan, bekkm, onkelfarmor, ltjessem, nsimb, jjandersson, [Shamshala](https://github.com/Shamshala), nath, [urbatecte](https://github.com/urbatecte), [Windmelodie](https://github.com/Windmelodie), [Fuempel](https://github.com/Fuempel), [MagaliDB](https://github.com/MagaliDB), [mhosse](https://github.com/mhosse), [Promises](https://github.com/Pr0mises)

**Inspiration:**
- [Bosch Indego API Documentation](http://grauonline.de/wordpress/?page_id=219)
- [Bosch Indego Controller](https://github.com/jofleck/iot-device-bosch-indego-controller)
