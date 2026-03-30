"""Error code mappings for Bosch Indego mowers."""

# Common Indego error codes and their descriptions
ERROR_CODE_MAP = {
    # No error
    "0": "No error",

    # Wheel/Motor errors (100-199)
    "101": "Wheel motor blocked",
    "102": "Left wheel motor blocked",
    "103": "Right wheel motor blocked",
    "110": "Mower motor blocked",
    "111": "Mower motor overloaded",

    # Battery/Charging errors (200-299)
    "201": "Battery disconnect",
    "202": "Battery low",
    "203": "Battery empty",
    "204": "Charging error",
    "205": "Battery temperature too high",
    "206": "Battery temperature too low",
    "207": "Battery disconnected",

    # Blade/Cutting errors (300-399)
    "301": "Blade/Motor blocked",
    "302": "Blade stuck",
    "303": "Blade jam detected",
    "304": "Blade motor overload",

    # Docking station errors (400-499)
    "401": "Docking station error",
    "402": "Docking station not found",
    "403": "Cannot go to dock",
    "404": "Docking charger not detected",

    # Perimeter/Wire errors (500-599)
    "501": "Perimeter signal weak",
    "502": "Perimeter wire cut",
    "503": "Perimeter signal malfunction",
    "504": "Perimeter wire not found",

    # Sensor errors (600-699)
    "601": "Ultrasonic sensor error",
    "602": "Collision sensor error",
    "603": "Gyroscope error",
    "604": "Accelerometer error",
    "605": "Compass error",
    "606": "GPS error",
    "607": "Wheel speed sensor error",

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

    # System errors (1000+)
    "1000": "System error",
    "1001": "Unknown error",
    "1002": "Shutdown detected",
}

def get_error_description(error_code: str) -> str:
    """Get error description from error code.

    Args:
        error_code: Error code as string

    Returns:
        Error description or "Unknown error" if not found
    """
    return ERROR_CODE_MAP.get(str(error_code), f"Unknown error code: {error_code}")
