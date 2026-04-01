"""Error code mappings for Bosch Indego mowers."""

# Common Indego error codes and their descriptions
ERROR_CODE_MAP = {
    # No error
    "0": "No error",

    # Wheel/Motor errors (100-199)
    "101": "Mower was lifted / Mäher wurde angehoben",
    "102": "Left wheel motor blocked",
    "103": "Right wheel motor blocked",
    "110": "Mower motor blocked",
    "111": "Battery error / Akkufehler",
    "115": "Permanent tactile detected / Dauerhaftes Hindernis erkannt",
    "130": "Cutter motor load too high / Messermotor überlastet",
    "143": "Intermittent error / Intermittierender Fehler",

    # Perimeter/Wire errors (140-160)
    "149": "Mower out of perimeter limit / Mäher außerhalb der Begrenzung",
    "151": "Wire signal / Communication fault / Drahtsignal / Kommunikationsfehler",

    # Sensor errors (600-699)
    "57": "Compass error / Kompassfehler",
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
    "1138": "Mower stuck / Sensor after cleaning / Mäher steckt fest / Sensor nach Reinigung",

    # Communication errors (800-899)
    "801": "Bluetooth error",
    "802": "WiFi connection lost",
    "803": "API connection error",
    "804": "No connection to server",
    "805": "Communication timeout",

    # Firmware/Software errors (900-999)
    "580": "Software version outdated / Software-Version veraltet",
    "901": "Firmware error",
    "902": "Software error",
    "903": "Configuration error",
    "904": "Memory error",

    # Battery errors (1100+)
    "1111": "Battery error / Akkufehler",
    "1156": "Unsupported battery pack / Communication fault battery pack / Akkupack nicht unterstützt",

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
