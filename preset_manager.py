#region Imports

# Standard
import json
import os

# Standard GUI
import tkinter as tk
from tkinter import ttk, messagebox

# Type checking
from typing import TYPE_CHECKING, Dict, Any, List, Optional
if TYPE_CHECKING:
    from app import Main


#endregion
#region Constants


PRESETS_FILE = "presets.json"


#endregion
#region Preset File Ops


def load_presets() -> Dict[str, Any]:
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


def save_presets_data(data: Dict[str, Any]):
    """Save the entire presets data structure."""
    with open(PRESETS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def save_preset(name: str, preset_data: Dict[str, Any]):
    """Save a single preset to the JSON file."""
    presets = load_presets()
    if name not in presets['_order']:
        presets['_order'].append(name)
    presets[name] = preset_data
    save_presets_data(presets)


def delete_preset(name: str):
    """Delete a preset from the JSON file."""
    presets = load_presets()
    if name in presets:
        del presets[name]
        if name in presets['_order']:
            presets['_order'].remove(name)
        save_presets_data(presets)


def reorder_presets(new_order: List[str]):
    """Update the order of presets."""
    presets = load_presets()
    presets['_order'] = new_order
    save_presets_data(presets)


def get_preset_names() -> List[str]:
    """Get list of all preset names in order."""
    presets = load_presets()
    return presets.get('_order', [])


def get_preset(name: str) -> Optional[Dict[str, Any]]:
    """Get a specific preset by name."""
    presets = load_presets()
    return presets.get(name)


#endregion
#region Preset List Ops


def refresh_preset_list(listbox: tk.Listbox):
    """Refresh the preset listbox with current presets."""
    listbox.delete(0, tk.END)
    for name in get_preset_names():
        listbox.insert(tk.END, name)


def show_preset_details(listbox: tk.Listbox, details_frame: ttk.Frame):
    """Show details of selected preset."""
    selection = listbox.curselection()
    if not selection:
        clear_preset_details(details_frame)
        return
    preset_name = listbox.get(selection[0])
    preset = get_preset(preset_name)
    if not preset:
        clear_preset_details(details_frame)
        return
    # Clear existing widgets
    for widget in details_frame.winfo_children():
        widget.destroy()
    # Display preset details
    ttk.Label(details_frame, text=f"Name: {preset_name}", font=('TkDefaultFont', 10, 'bold')).pack(anchor='w', pady=(0, 10))
    # Formula details
    formula_frame = ttk.LabelFrame(details_frame, text="Formula", padding="5")
    formula_frame.pack(fill='x', pady=(0, 10))
    ttk.Label(formula_frame, text=f"Input 1: {preset.get('input1', 'N/A')} {preset.get('input1_unit', '')}").pack(anchor='w')
    ttk.Label(formula_frame, text=f"Operator: {preset.get('operator', 'N/A')}").pack(anchor='w')
    ttk.Label(formula_frame, text=f"Input 2: {preset.get('input2', 'N/A')} {preset.get('input2_unit', '')}").pack(anchor='w')
    ttk.Label(formula_frame, text=f"Coverage Rate: {preset.get('coverage_rate', 'N/A')} sq ft/gallon").pack(anchor='w')
    # Info section
    if preset.get('info'):
        info_frame = ttk.LabelFrame(details_frame, text="Information", padding="5")
        info_frame.pack(fill='both', expand=True)
        info_text = tk.Text(info_frame, wrap='word', height=6, state='disabled')
        info_text.pack(fill='both', expand=True)
        info_text.config(state='normal')
        info_text.insert('1.0', preset['info'])
        info_text.config(state='disabled')


def clear_preset_details(details_frame: ttk.Frame):
    """Clear the preset details area."""
    for widget in details_frame.winfo_children():
        widget.destroy()
    ttk.Label(details_frame, text="Select a preset to view details").pack(expand=True)


#endregion
#region GUI Helpers


def _refresh_all_preset_displays(app: 'Main', listbox: tk.Listbox):
    """Helper to refresh both preset list and calculator dropdown."""
    refresh_preset_list(listbox)
    refresh_calculator_presets(app)


def _get_selected_preset_name(listbox: tk.Listbox, action_name: str) -> Optional[str]:
    """Helper to get selected preset name with validation and error handling."""
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", f"Please select a preset to {action_name}.")
        return None
    return listbox.get(selection[0])


def _move_preset_by_offset(app: 'Main', listbox: tk.Listbox, offset: int):
    """Helper to move preset up (-1) or down (1) in the list."""
    selection = listbox.curselection()
    current_order = get_preset_names()

    if not selection:
        return
    index = selection[0]
    new_index = index + offset
    # Check bounds
    if new_index < 0 or new_index >= len(current_order):
        return
    # Swap positions
    current_order[index], current_order[new_index] = current_order[new_index], current_order[index]
    reorder_presets(current_order)
    _refresh_all_preset_displays(app, listbox)
    # Maintain selection
    listbox.selection_set(new_index)


#endregion
#region GUI Actions


def add_preset(app: 'Main', listbox: tk.Listbox):
    """Add a new preset."""
    from widgets import PresetDialog
    dialog = PresetDialog(app, "Add Preset")
    app.wait_window(dialog.dialog)
    if dialog.result:
        name, preset_data = dialog.result
        save_preset(name, preset_data)
        _refresh_all_preset_displays(app, listbox)
        # Select the new preset
        preset_names = get_preset_names()
        if name in preset_names:
            listbox.selection_set(preset_names.index(name))


def edit_preset(app: 'Main', listbox: tk.Listbox):
    """Edit selected preset."""
    from widgets import PresetDialog
    preset_name = _get_selected_preset_name(listbox, "edit")
    if not preset_name:
        return
    preset = get_preset(preset_name)
    if not preset:
        messagebox.showerror("Error", "Preset not found.")
        return
    dialog = PresetDialog(app, "Edit Preset", preset_name, preset)
    app.wait_window(dialog.dialog)
    if dialog.result:
        new_name, preset_data = dialog.result
        # If name changed, delete old and create new
        if new_name != preset_name:
            delete_preset(preset_name)
        save_preset(new_name, preset_data)
        _refresh_all_preset_displays(app, listbox)
        # Select the edited preset
        preset_names = get_preset_names()
        if new_name in preset_names:
            listbox.selection_set(preset_names.index(new_name))


def delete_preset_gui(app: 'Main', listbox: tk.Listbox):
    """Delete selected preset."""
    preset_name = _get_selected_preset_name(listbox, "delete")
    if not preset_name:
        return
    if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{preset_name}'?"):
        delete_preset(preset_name)
        _refresh_all_preset_displays(app, listbox)
        clear_preset_details(app.preset_details_frame)


def move_preset_up(app: 'Main', listbox: tk.Listbox):
    """Move selected preset up in the list."""
    _move_preset_by_offset(app, listbox, -1)


def move_preset_down(app: 'Main', listbox: tk.Listbox):
    """Move selected preset down in the list."""
    _move_preset_by_offset(app, listbox, 1)


def refresh_calculator_presets(app: 'Main'):
    """Refresh the preset dropdown in the calculator tab."""
    if hasattr(app, 'preset_combo'):
        current_value = app.preset_var.get()
        new_names = get_preset_names()
        app.preset_combo['values'] = new_names
        # If current selection is still valid, keep it
        if current_value not in new_names and new_names:
            app.preset_var.set(new_names[0] if new_names else "")
        elif not new_names:
            app.preset_var.set("")


#endregion
#region Module Level


# Load presets at module level for compatibility
# Presets
PRESETS = load_presets()


#endregion
