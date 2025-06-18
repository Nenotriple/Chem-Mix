#region - Imports


# Standard
from tkinter import ttk, messagebox
import tkinter as tk

# Local
import preset_manager
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
    list_frame = ttk.LabelFrame(left_frame, text="Presets")
    list_frame.pack(fill='both', expand=True)
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
    ttk.Button(control_frame, text="Add New", command=lambda: preset_manager.add_preset(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Edit", command=lambda: preset_manager.edit_preset(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Delete", command=lambda: preset_manager.delete_preset_gui(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Move Up", command=lambda: preset_manager.move_preset_up(app, preset_listbox)).pack(side='left', padx=(0, 5))
    ttk.Button(control_frame, text="Move Down", command=lambda: preset_manager.move_preset_down(app, preset_listbox)).pack(side='left')
    # Right side - Preset details
    right_frame = ttk.LabelFrame(main_frame, text="Preset Details")
    right_frame.pack(side='right', fill='both', expand=True)
    # Store references for updating
    app.preset_listbox = preset_listbox
    app.preset_details_frame = right_frame
    # Bind selection event
    preset_listbox.bind('<<ListboxSelect>>', lambda e: preset_manager.show_preset_details(preset_listbox, right_frame))
    # Load initial data
    preset_manager.refresh_preset_list(preset_listbox)


def create_calculator_tab(app, notebook):
    calculator_frame = ttk.Frame(notebook, padding="5")
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
    m_frame = ttk.LabelFrame(frame, text="Mode")
    m_frame.pack(side='left', fill='both', expand=True)
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
    o_frame = ttk.LabelFrame(frame, text="Output")
    o_frame.pack(side='left', fill='both', expand=True)
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
    i_frame = ttk.LabelFrame(frame, text="Input")
    i_frame.pack(side='left', fill='both', expand=True)
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
    r_frame = ttk.LabelFrame(frame, text="Result")
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
    f_frame = ttk.LabelFrame(frame, text="Formula")
    f_frame.pack(fill='x')
    # Frame
    p_row = ttk.Frame(f_frame)
    p_row.pack(fill='x')
    # Label
    app.preset_label = ttk.Label(p_row, text="Preset", width=17, anchor="center")
    app.preset_label.pack(side='left', padx=(0, 5))
    # Combobox
    app.preset_combo = ttk.Combobox(p_row, textvariable=app.preset_var, values=preset_manager.get_preset_names(), width=20, state='readonly')
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
#region - PresetDialog


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
        formula_frame = ttk.LabelFrame(main_frame, text="Formula")
        formula_frame.pack(fill='x')
        # Part A
        ttk.Label(formula_frame, text="Part A:").pack(anchor='w')
        input1_frame = ttk.Frame(formula_frame)
        input1_frame.pack(fill='x', pady=(0, 5))
        ttk.Entry(input1_frame, textvariable=self.input1_var, width=10).pack(side='left')
        ttk.Combobox(input1_frame, textvariable=self.input1_unit_var, values=list(CONVERSIONS.keys()), state='readonly', width=15).pack(side='left', padx=(5, 0))
        # Operator
        ttk.Label(formula_frame, text="Operator:").pack(anchor='w', pady=(5, 0))
        ttk.Combobox(formula_frame, textvariable=self.operator_var, values=["/", "*"], state='readonly', width=10).pack(anchor='w', pady=(0, 5))
        # Part B
        ttk.Label(formula_frame, text="Part B:").pack(anchor='w')
        input2_frame = ttk.Frame(formula_frame)
        input2_frame.pack(fill='x', pady=(0, 5))
        ttk.Entry(input2_frame, textvariable=self.input2_var, width=10).pack(side='left')
        ttk.Combobox(input2_frame, textvariable=self.input2_unit_var, values=list(CONVERSIONS.keys()), state='readonly', width=15).pack(side='left', padx=(5, 0))
        # Coverage rate
        ttk.Label(formula_frame, text="Coverage Rate (sq ft/gallon):").pack(anchor='w', pady=(5, 0))
        ttk.Entry(formula_frame, textvariable=self.coverage_var, width=15).pack(anchor='w')
        # Info section
        info_frame = ttk.LabelFrame(main_frame, text="Information")
        info_frame.pack(fill='both', expand=True)
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


#endregion
