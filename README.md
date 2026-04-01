[![GitHub release](https://img.shields.io/github/release/sander1988/Indego.svg)](https://github.com/sander1988/Indego/releases/) [![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

# Bosch Indego Mower

**Home Assistant Custom Component for Bosch Indego robotic lawn mowers**

A comprehensive Home Assistant integration that provides full control and monitoring of your Bosch Indego lawn mower. Get real-time status, battery information, mowing schedules, and more.

![Entities in Home Assistant](/doc/sensors.png)

## ✨ Features

- 🎮 **Full Mower Control** - Start, pause, dock, and schedule mowing
- 📊 **Real-time Monitoring** - Battery, location, alerts, and more
- 📍 **Lawn Mapping** - Visual SVG map with mower position overlay
- 🤖 **SmartMowing** - Automatic schedule optimization based on weather
- ⚠️ **Alert Management** - Monitor and manage mower alerts
- 🌍 **Multi-language** - German, English, Dutch, French, Spanish, Italian, and more
- 🏠 **Native Entities** - Lawn Mower and Vacuum entities for seamless Home Assistant integration
- 📱 **Multiple Mowers** - Support for multiple mowers in one Home Assistant instance

## 📖 Table of Contents

- [Features](#-features)
- [Community](#-community)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Monitored Entities](#-monitored-entities)
- [Services & Control](#-services--control)
- [Examples](#-examples)
- [Debugging](#-debugging)
- [Supported Models](#-supported-models)
- [Known Issues](#️-known-issues)
- [Contribution & Support](#-contribution--support)
- [Credits](#-credits)

## 💬 Community

Join our Discord community to discuss features, vote on improvements, and get support:
[discord.gg/aD33GsP](https://discord.gg/aD33GsP)

## Installation

### Option 1: Via HACS (Recommended)

1. Add this repository to HACS (Community Store)
2. Search for "Bosch Indego"
3. Click "Install"
4. Restart Home Assistant

[HACS Repository](https://hacs.xyz/)

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
| **Estimated Session Duration** | Estimated duration of current session (minutes) |

### Battery & Charging

| Sensor | Description |
|--------|-------------|
| **Battery Level** | Current battery charge (%) |
| **Battery Health** | Battery health status |

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
| **Alerts** | Active alert status with count and last message |
| **Last Error** | Last error code and timestamp |
| **Firmware Version** | Current firmware version |
| **Maintenance Hours** | Maintenance counter (hours) |

### Other Information

| Sensor | Description |
|--------|-------------|
| **Mowing Mode** | Current mowing mode setting |
| **Online Status** | Whether mower is connected (True/False) |
| **Update Available** | Firmware update availability (On/Off) |
| **Last Completed Mow** | Last full lawn mowing completion time |
| **Next Mow Time** | Scheduled next mowing time |
| **Lawn Mower Entity** | Native Home Assistant Lawn Mower entity (Start, Pause, Dock) |
| **Vacuum Entity** | Legacy Home Assistant Vacuum entity (Start, Pause, Return, Battery) |
| **Lawn Map** | SVG lawn map with mower position overlay |



## 🎮 Services & Control

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

Downloads the current lawn map from Bosch Cloud API and saves as `www/indego_map_base.svg` in your Home Assistant configuration directory. Used by the camera entity.

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
