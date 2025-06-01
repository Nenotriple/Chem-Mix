import json
import os


PRESETS_FILE = "presets.json"


def load_presets():
    """Load presets from JSON file. Returns empty dict if file doesn't exist."""
    if os.path.exists(PRESETS_FILE):
        try:
            with open(PRESETS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}


def save_preset(name, preset_data):
    """Save a single preset to the JSON file."""
    presets = load_presets()
    presets[name] = preset_data
    with open(PRESETS_FILE, 'w') as f:
        json.dump(presets, f, indent=2)


def get_preset_names():
    """Get list of all preset names."""
    presets = load_presets()
    return list(presets.keys())


# Load presets at module level for compatibility
PRESETS = load_presets()
