#region - Imports


# Standard
from tkinter import ttk, messagebox, simpledialog
import tkinter as tk

# Local
from preset_manager import get_preset_names, get_preset, save_preset, delete_preset, reorder_presets
from conversions import CONVERSIONS


# Type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import Main


#endregion
#region - All


def create_all_widgets(app: 'Main'):
    app.config(padx=5, pady=5)
    # Create notebook container
    notebook = ttk.Notebook(app)
    notebook.pack(fill='both', expand=True, padx=5, pady=5)
    create_calculator_tab(app, notebook)
    create_preset_manager_tab(app, notebook)


def create_preset_manager_tab(app, notebook):
    preset_manager_frame = ttk.Frame(notebook)
    notebook.add(preset_manager_frame, text="Preset Manager")
    # Main container
    main_frame = ttk.Frame(preset_manager_frame)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)
    # Left side - Preset list and controls
    left_frame = ttk.Frame(main_frame)
    left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
    # Preset list
    list_frame = ttk.LabelFrame(left_frame, text="Presets", padding="5")
    list_frame.pack(fill='both', expand=True, pady=(0, 10))
    # Listbox with scrollbar
    listbox_frame = ttk.Frame(list_frame)
    listbox_frame.pack(fill='both', expand=True)
    preset_listbox = tk.Listbox(listbox_frame, selectmode='single')
    scrollbar = ttk.Scrollbar(listbox_frame, orient='vertical', command=preset_listbox.yview)
    preset_listbox.configure(yscrollcommand=scrollbar.set)
    preset_listbox.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    # Control buttons
    control_frame = ttk.Frame(left_frame)
    control_frame.pack(fill='x')
    ttk.Button(control_frame, text="Add New", command=lambda: add_preset(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Edit", command=lambda: edit_preset(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Delete", command=lambda: delete_preset_gui(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Move Up", command=lambda: move_preset_up(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Move Down", command=lambda: move_preset_down(app, preset_listbox)).pack(side='left')
    # Right side - Preset details
    right_frame = ttk.LabelFrame(main_frame, text="Preset Details", padding="5")
    right_frame.pack(side='right', fill='both', expand=True)
    # Store references for updating
    app.preset_listbox = preset_listbox
    app.preset_details_frame = right_frame
    # Bind selection event
    preset_listbox.bind('<<ListboxSelect>>', lambda e: show_preset_details(app, preset_listbox, right_frame))
    # Load initial data
    refresh_preset_list(preset_listbox)


def create_calculator_tab(app, notebook):
    calculator_frame = ttk.Frame(notebook)
    notebook.add(calculator_frame, text="Calculator")
    # Top frame
    top_frame = ttk.Frame(calculator_frame)
    top_frame.pack(fill='x', pady=5)
    create_mode_sel_frame(top_frame, app)
    create_output_sel_frame(top_frame, app)
    create_input_frame(top_frame, app)
    # Result frame
    result_frame = ttk.Frame(calculator_frame)
    result_frame.pack(fill='x', pady=5)
    create_result_frame(result_frame, app)
    # Formula frame
    formula_frame = ttk.Frame(calculator_frame)
    formula_frame.pack(fill='x', pady=5)
    create_formula_frame(formula_frame, app)


#endregion
#region - Primary Mode


def create_mode_sel_frame(frame: 'ttk.Frame', app: 'Main'):
    # Frame
    m_frame = ttk.LabelFrame(frame, text="Mode", padding="5")
    m_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))
    # Frame
    r_frame = ttk.Frame(m_frame)
    r_frame.pack(expand=True)
    # Radio Button
    ttk.Radiobutton(r_frame, text="By Volume", variable=app.primary_mode, value="volume").pack(anchor='w', padx=5, pady=2)
    ttk.Radiobutton(r_frame, text="By Ratio", variable=app.primary_mode, value="ratio").pack(anchor='w', padx=5, pady=2)


#endregion
#region - Mode


def create_output_sel_frame(frame: 'ttk.Frame', app: 'Main'):
    # Frame
    o_frame = ttk.LabelFrame(frame, text="Output", padding="5")
    o_frame.pack(side='left', fill='both', expand=True, padx=5)
    # Frame
    r_frame = ttk.Frame(o_frame)
    r_frame.pack(expand=True)
    # Radio Button
    ttk.Radiobutton(r_frame, text="Get: Part A", variable=app.calc_mode, value="partB", command=app.update_labels).pack(anchor='center', padx=5, pady=2)
    ttk.Radiobutton(r_frame, text="Get: Part B", variable=app.calc_mode, value="partA", command=app.update_labels).pack(anchor='center', padx=5, pady=2)


#endregion
#region - Input


def create_input_frame(frame: 'ttk.Frame', app: 'Main'):
    # Frame
    i_frame = ttk.LabelFrame(frame, text="Input", padding="5")
    i_frame.pack(side='left', fill='both', expand=True, padx=(5, 0))
    # Frame
    i_row = ttk.Frame(i_frame)
    i_row.pack(fill='x', expand=True)
    # Label
    ttk.Label(i_row, textvariable=app.input_label_var, width=18, anchor="center").pack(side='left')
    # Entry
    ttk.Entry(i_row, textvariable=app.input_var).pack(side='left', fill='x', expand=True)
    # Frame
    u_frame = ttk.Frame(i_frame)
    u_frame.pack(fill='x', pady=(5, 0))
    # Combobox
    ttk.Combobox(u_frame, textvariable=app.input_unit, values=list(CONVERSIONS.keys()), state='readonly', width=12).pack(side='right')


#endregion
#region - Result


def create_result_frame(frame: 'ttk.Frame', app: 'Main'):
    # Frame
    r_frame = ttk.LabelFrame(frame, text="Result", padding="5")
    r_frame.pack(fill='x')
    # Frame
    r_row = ttk.Frame(r_frame)
    r_row.pack(fill='x')
    # Label
    ttk.Label(r_row, textvariable=app.result_label_var, width=17, anchor="center").pack(side='left', padx=(0, 5))
    # Entry
    ttk.Entry(r_row, textvariable=app.output_var, state='readonly').pack(side='left', fill='x', expand=True)
    # Combobox
    ttk.Combobox(r_row, textvariable=app.output_unit, values=list(CONVERSIONS.keys()), state='readonly', width=12).pack(side='left', padx=(5, 0))
    # Frame
    c_row = ttk.Frame(r_frame)
    c_row.pack(fill='x', pady=(10, 0))
    # Label
    ttk.Label(c_row, text="Coverage", width=17, anchor="center").pack(side='left', padx=(0, 5))
    # Entry
    ttk.Entry(c_row, textvariable=app.coverage_output_var, state='readonly').pack(side='left', fill='x', expand=True)
    # Label
    ttk.Label(c_row, text="sq ft", width=15, anchor="center").pack(side='left', padx=(5, 0))


#endregion
#region - Formula


def create_formula_frame(frame: 'ttk.Frame', app: 'Main'):
    # Frame
    f_frame = ttk.LabelFrame(frame, text="Formula", padding="5")
    f_frame.pack(fill='x')
    # Frame
    p_row = ttk.Frame(f_frame)
    p_row.pack(fill='x')
    # Label
    app.preset_label = ttk.Label(p_row, text="Preset", width=17, anchor="center")
    app.preset_label.pack(side='left', padx=(0, 5))
    # Combobox
    app.preset_combo = ttk.Combobox(p_row, textvariable=app.preset_var, values=get_preset_names(), width=20, state='readonly')
    app.preset_combo.pack(side='left', fill='x', expand=True)
    # Help button
    app.preset_help_button = ttk.Button(p_row, text="?", width=2, command=app.show_preset_info)
    app.preset_help_button.pack(side='left', padx=(5, 0))
    # Ratio input row
    r_row = ttk.Frame(f_frame)
    r_row.pack(fill='x', pady=(10, 0))
    # Label
    app.ratio_label = ttk.Label(r_row, text="Ratio (B:A)", width=17, anchor="center")
    app.ratio_label.pack(side='left', padx=(0, 5))
    # Entry
    app.ratio_entry = ttk.Entry(r_row, textvariable=app.ratio_input, width=10)
    app.ratio_entry.pack(side='left')
    # Frame
    f_row = ttk.Frame(f_frame)
    f_row.pack(fill='x', pady=(10, 0))
    # Label
    app.formula_label = ttk.Label(f_row, text="Volume Ratio", width=17, anchor="center")
    app.formula_label.pack(side='left', padx=(0, 5))
    # Entry
    formula_entry1 = ttk.Entry(f_row, textvariable=app.formula_input1, width=4)
    formula_entry1.pack(side='left', fill='x', expand=True)
    # Combobox
    formula_combo1 = ttk.Combobox(f_row, textvariable=app.formula_input1_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly')
    formula_combo1.pack(side='left', padx=2)
    formula_operator_combo = ttk.Combobox(f_row, textvariable=app.formula_operator, values=["/", "*"], width=4, state='readonly')
    formula_operator_combo.pack(side='left', padx=2)
    # Entry
    formula_entry2 = ttk.Entry(f_row, textvariable=app.formula_input2, width=4)
    formula_entry2.pack(side='left', fill='x', expand=True)
    # Combobox
    formula_combo2 = ttk.Combobox(f_row, textvariable=app.formula_input2_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly')
    formula_combo2.pack(side='left', padx=2)
    # Frame
    c_row = ttk.Frame(f_frame)
    c_row.pack(fill='x', pady=(10, 0))
    # Label
    ttk.Label(c_row, text="Coverage Rate", width=17, anchor="center").pack(side='left', padx=(0, 5))
    # Entry
    ttk.Entry(c_row, textvariable=app.coverage_rate).pack(side='left', fill='x', expand=True)
    # Label
    ttk.Label(c_row, text="sq ft/gallon", width=15, anchor="center").pack(side='left', padx=(5, 0))
    # Store formula widget references for state management
    app.formula_widgets = [
        formula_entry1, formula_combo1, formula_operator_combo,
        formula_entry2, formula_combo2
    ]
    # Initialize widget states
    app.after_idle(app.update_widget_states)


#endregion
#region - Preset Manager Functions


def refresh_preset_list(listbox):
    """Refresh the preset listbox with current presets."""
    listbox.delete(0, tk.END)
    for name in get_preset_names():
        listbox.insert(tk.END, name)


def show_preset_details(app, listbox, details_frame):
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


def clear_preset_details(details_frame):
    """Clear the preset details area."""
    for widget in details_frame.winfo_children():
        widget.destroy()
    ttk.Label(details_frame, text="Select a preset to view details").pack(expand=True)


def add_preset(app, listbox):
    """Add a new preset."""
    dialog = PresetDialog(app, "Add Preset")
    app.wait_window(dialog.dialog)
    if dialog.result:
        name, preset_data = dialog.result
        save_preset(name, preset_data)
        refresh_preset_list(listbox)
        refresh_calculator_presets(app)
        # Select the new preset
        preset_names = get_preset_names()
        if name in preset_names:
            listbox.selection_set(preset_names.index(name))


def edit_preset(app, listbox):
    """Edit selected preset."""
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Please select a preset to edit.")
        return
    preset_name = listbox.get(selection[0])
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
        refresh_preset_list(listbox)
        refresh_calculator_presets(app)
        # Select the edited preset
        preset_names = get_preset_names()
        if new_name in preset_names:
            listbox.selection_set(preset_names.index(new_name))


def delete_preset_gui(app, listbox):
    """Delete selected preset."""
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Please select a preset to delete.")
        return
    preset_name = listbox.get(selection[0])
    if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{preset_name}'?"):
        delete_preset(preset_name)
        refresh_preset_list(listbox)
        refresh_calculator_presets(app)
        clear_preset_details(app.preset_details_frame)


def move_preset_up(app, listbox):
    """Move selected preset up in the list."""
    selection = listbox.curselection()
    if not selection or selection[0] == 0:
        return
    current_order = get_preset_names()
    index = selection[0]
    # Swap positions
    current_order[index], current_order[index-1] = current_order[index-1], current_order[index]
    reorder_presets(current_order)
    refresh_preset_list(listbox)
    refresh_calculator_presets(app)
    # Maintain selection
    listbox.selection_set(index-1)


def move_preset_down(app, listbox):
    """Move selected preset down in the list."""
    selection = listbox.curselection()
    current_order = get_preset_names()
    if not selection or selection[0] >= len(current_order) - 1:
        return
    index = selection[0]
    # Swap positions
    current_order[index], current_order[index+1] = current_order[index+1], current_order[index]
    reorder_presets(current_order)
    refresh_preset_list(listbox)
    refresh_calculator_presets(app)
    # Maintain selection
    listbox.selection_set(index+1)


def refresh_calculator_presets(app):
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


class PresetDialog:
    """Dialog for adding/editing presets."""

    def __init__(self, parent, title, preset_name="", preset_data=None):
        self.result = None
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x500")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        # Center dialog
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
        # Variables
        self.name_var = tk.StringVar(value=preset_name)
        self.input1_var = tk.DoubleVar(value=preset_data.get('input1', 1.0) if preset_data else 1.0)
        self.input1_unit_var = tk.StringVar(value=preset_data.get('input1_unit', 'Gallon') if preset_data else 'Gallon')
        self.operator_var = tk.StringVar(value=preset_data.get('operator', '/') if preset_data else '/')
        self.input2_var = tk.DoubleVar(value=preset_data.get('input2', 1.0) if preset_data else 1.0)
        self.input2_unit_var = tk.StringVar(value=preset_data.get('input2_unit', 'Ounce') if preset_data else 'Ounce')
        self.coverage_var = tk.DoubleVar(value=preset_data.get('coverage_rate', 100.0) if preset_data else 100.0)
        self.info_var = tk.StringVar(value=preset_data.get('info', '') if preset_data else '')
        self.create_widgets()


    def create_widgets(self):
        main_frame = ttk.Frame(self.dialog, padding="10")
        main_frame.pack(fill='both', expand=True)
        # Name
        ttk.Label(main_frame, text="Preset Name:").pack(anchor='w')
        ttk.Entry(main_frame, textvariable=self.name_var, width=40).pack(fill='x', pady=(0, 10))
        # Formula section
        formula_frame = ttk.LabelFrame(main_frame, text="Formula", padding="5")
        formula_frame.pack(fill='x', pady=(0, 10))
        # Input 1
        ttk.Label(formula_frame, text="Input 1:").pack(anchor='w')
        input1_frame = ttk.Frame(formula_frame)
        input1_frame.pack(fill='x', pady=(0, 5))
        ttk.Entry(input1_frame, textvariable=self.input1_var, width=10).pack(side='left')
        ttk.Combobox(input1_frame, textvariable=self.input1_unit_var, values=list(CONVERSIONS.keys()), state='readonly', width=15).pack(side='left', padx=(5, 0))
        # Operator
        ttk.Label(formula_frame, text="Operator:").pack(anchor='w', pady=(5, 0))
        ttk.Combobox(formula_frame, textvariable=self.operator_var, values=["/", "*"], state='readonly', width=10).pack(anchor='w', pady=(0, 5))
        # Input 2
        ttk.Label(formula_frame, text="Input 2:").pack(anchor='w')
        input2_frame = ttk.Frame(formula_frame)
        input2_frame.pack(fill='x', pady=(0, 5))
        ttk.Entry(input2_frame, textvariable=self.input2_var, width=10).pack(side='left')
        ttk.Combobox(input2_frame, textvariable=self.input2_unit_var, values=list(CONVERSIONS.keys()), state='readonly', width=15).pack(side='left', padx=(5, 0))
        # Coverage rate
        ttk.Label(formula_frame, text="Coverage Rate (sq ft/gallon):").pack(anchor='w', pady=(5, 0))
        ttk.Entry(formula_frame, textvariable=self.coverage_var, width=15).pack(anchor='w')
        # Info section
        info_frame = ttk.LabelFrame(main_frame, text="Information", padding="5")
        info_frame.pack(fill='both', expand=True, pady=(0, 10))
        self.info_text = tk.Text(info_frame, height=8, wrap='word')
        info_scroll = ttk.Scrollbar(info_frame, orient='vertical', command=self.info_text.yview)
        self.info_text.configure(yscrollcommand=info_scroll.set)
        self.info_text.pack(side='left', fill='both', expand=True)
        info_scroll.pack(side='right', fill='y')
        # Insert existing info if editing
        if self.info_var.get():
            self.info_text.insert('1.0', self.info_var.get())
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x')
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side='right', padx=(5, 0))
        ttk.Button(button_frame, text="Save", command=self.save).pack(side='right')


    def save(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a preset name.")
            return
        try:
            preset_data = {
                'input1': self.input1_var.get(),
                'input1_unit': self.input1_unit_var.get(),
                'operator': self.operator_var.get(),
                'input2': self.input2_var.get(),
                'input2_unit': self.input2_unit_var.get(),
                'coverage_rate': self.coverage_var.get(),
                'info': self.info_text.get('1.0', 'end-1c').strip()
            }
            self.result = (name, preset_data)
            self.dialog.destroy()
        except tk.TclError:
            messagebox.showerror("Error", "Please check that all numeric values are valid.")


    def cancel(self):
        self.dialog.destroy()
