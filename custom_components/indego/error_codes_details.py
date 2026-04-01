"""Detailed error code descriptions and troubleshooting for Indego mowers."""

# Extended error code mapping with detailed descriptions and troubleshooting tips
ERROR_CODES_DETAILED = {
    "101": {
        "de": "Mäher wurde angehoben",
        "en": "Mower was lifted",
        "common_causes": [
            "Lift sensor triggered (wheels blocked, grass too high, dirt)",
            "Mower lifted during operation",
            "Dirty wheel sensors"
        ],
        "solutions": [
            "Lift the mower and check underneath for dirt/blockages",
            "Clean wheel sensors",
            "Trim grass if too high",
            "Check if wheels move freely",
            "If problem persists: faulty sensor (contact service)"
        ]
    },
    "111": {
        "de": "Akkufehler",
        "en": "Battery error",
        "common_causes": [
            "Battery not recognized",
            "Defective battery",
            "Poor battery contacts"
        ],
        "solutions": [
            "Remove battery and clean contacts",
            "Reinsert battery firmly",
            "For Connect models: Reset app or exchange battery",
            "Check battery for visible damage"
        ]
    },
    "115": {
        "de": "Dauerhaftes Hindernis erkannt (Stoßsensor)",
        "en": "Permanent tactile detected (Bumper sensor)",
        "common_causes": [
            "Mower constantly bumping (stuck at dock, dirt on bumper)",
            "Defective collision sensor",
            "Dock positioned too close"
        ],
        "solutions": [
            "Check mower underneath for dirt/debris on bumper",
            "Reposition docking station",
            "Clean bumper sensor",
            "Perform firmware update",
            "If persists: faulty sensor (contact service)"
        ]
    },
    "130": {
        "de": "Messermotor überlastet",
        "en": "Cutter motor load too high",
        "common_causes": [
            "Grass too long",
            "Blade blockage",
            "Dull blades",
            "Dirt/debris under mower"
        ],
        "solutions": [
            "Pre-cut grass if too high",
            "Replace blades with new ones",
            "Clean underneath thoroughly",
            "Check for stuck objects"
        ]
    },
    "143": {
        "de": "Intermittierender Fehler",
        "en": "Intermittent error",
        "common_causes": [
            "Sensor or software issue",
            "Poor electrical connections",
            "Firmware corruption"
        ],
        "solutions": [
            "Power off mower and dock completely (5-10 minutes)",
            "Power on and restart",
            "Check and update firmware via app",
            "If problem persists: contact support"
        ]
    },
    "149": {
        "de": "Mäher außerhalb der Begrenzung",
        "en": "Mower out of perimeter limit",
        "common_causes": [
            "Wire signal lost",
            "Perimeter wire broken/damaged",
            "Wire too close to electrical sources",
            "Wrong boundary ID"
        ],
        "solutions": [
            "Test perimeter wire with multimeter/wire tester",
            "Check for breaks in wire",
            "Move wire away from power lines/sources",
            "Change boundary ID in app menu",
            "Reroute wire if damaged"
        ]
    },
    "151": {
        "de": "Drahtsignal / Kommunikationsfehler",
        "en": "Wire signal / Communication fault",
        "common_causes": [
            "Perimeter wire broken or damaged",
            "Wire too long/short",
            "No connection to dock",
            "Faulty dock connectors"
        ],
        "solutions": [
            "Test perimeter wire with wire tester",
            "Check wire length is within specs",
            "Clean dock connectors",
            "Verify wire connections are tight",
            "Check dock power supply"
        ]
    },
    "57": {
        "de": "Kompassfehler",
        "en": "Compass error",
        "common_causes": [
            "Magnetic interference",
            "Compass sensor malfunction"
        ],
        "solutions": [
            "Move away from strong magnetic fields",
            "Update firmware",
            "Check for compass interference"
        ]
    },
    "580": {
        "de": "Software-Version veraltet",
        "en": "Software version outdated",
        "common_causes": [
            "Firmware update required"
        ],
        "solutions": [
            "Update firmware via app",
            "Ensure mower is fully charged",
            "Do not interrupt update process"
        ]
    },
    "1111": {
        "de": "Akkufehler",
        "en": "Battery error",
        "common_causes": [
            "Battery not recognized",
            "Defective battery",
            "Poor battery contacts"
        ],
        "solutions": [
            "Remove battery, clean contacts thoroughly",
            "Reinsert battery firmly",
            "Exchange battery if defective",
            "Perform firmware update"
        ]
    },
    "1138": {
        "de": "Mäher steckt fest / Sensor nach Reinigung",
        "en": "Mower stuck / Sensor after cleaning",
        "common_causes": [
            "Mower wedged in tight space",
            "Sensor error after cleaning",
            "Dirt blocking wheels"
        ],
        "solutions": [
            "Manually free the mower",
            "Clean all sensors thoroughly",
            "Inspect wheels for blockages",
            "Check for debris inside",
            "Test sensors with app diagnostics"
        ]
    },
    "1156": {
        "de": "Akkupack nicht unterstützt / Kommunikationsfehler Akkupack",
        "en": "Communication fault battery pack",
        "common_causes": [
            "Unsupported battery model",
            "Dirty battery contacts",
            "Battery firmware mismatch",
            "Usually M+ 700 after battery change"
        ],
        "solutions": [
            "Clean battery and dock contacts thoroughly",
            "Insert battery firmly",
            "Perform firmware update via app",
            "Exchange battery if incompatible",
            "Check battery model compatibility"
        ]
    }
}


def get_error_details(error_code: str, language: str = "de") -> dict:
    """Get detailed error information.

    Args:
        error_code: Error code as string
        language: "de" for German or "en" for English (default: "de")

    Returns:
        Dictionary with error details or empty dict if not found
    """
    code_details = ERROR_CODES_DETAILED.get(str(error_code), {})

    if not code_details:
        return {
            "message": f"Unknown error code: {error_code}",
            "solutions": ["Contact Indego support"]
        }

    return {
        "message": code_details.get(language, code_details.get("en", "Unknown error")),
        "common_causes": code_details.get("common_causes", []),
        "solutions": code_details.get("solutions", [])
    }
