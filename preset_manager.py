import json
import os


PRESETS_FILE = "presets.json"


def load_presets():
    """Load presets from JSON file. Returns empty dict if file doesn't exist."""
    if os.path.exists(PRESETS_FILE):
        try:
            with open(PRESETS_FILE, 'r') as f:
                data = json.load(f)
                # Handle both old format (dict) and new format (dict with _order)
                if isinstance(data, dict) and '_order' not in data:
                    # Convert old format to new format
                    order = list(data.keys())
                    data['_order'] = order
                    save_presets_data(data)
                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return {'_order': []}
    return {'_order': []}


def save_presets_data(data):
    """Save the entire presets data structure."""
    with open(PRESETS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def save_preset(name, preset_data):
    """Save a single preset to the JSON file."""
    presets = load_presets()
    if name not in presets['_order']:
        presets['_order'].append(name)
    presets[name] = preset_data
    save_presets_data(presets)


def delete_preset(name):
    """Delete a preset from the JSON file."""
    presets = load_presets()
    if name in presets:
        del presets[name]
        if name in presets['_order']:
            presets['_order'].remove(name)
        save_presets_data(presets)


def reorder_presets(new_order):
    """Update the order of presets."""
    presets = load_presets()
    presets['_order'] = new_order
    save_presets_data(presets)


def get_preset_names():
    """Get list of all preset names in order."""
    presets = load_presets()
    return presets.get('_order', [])


def get_preset(name):
    """Get a specific preset by name."""
    presets = load_presets()
    return presets.get(name)


# Load presets at module level for compatibility
PRESETS = load_presets()
