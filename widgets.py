#region - Imports


# Standard
from tkinter import ttk

# Local
from preset_manager import get_preset_names
from conversions import CONVERSIONS


# Type checking
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import Main


#endregion
#region - All


def create_all_widgets(parent: 'Main'):
    top_frame = ttk.Frame(parent)
    top_frame.pack(fill='x', pady=5)
    create_primary_mode_frame(top_frame, parent.primary_mode)
    create_mode_frame(top_frame, parent.calc_mode, parent.update_labels)
    create_input_frame(top_frame, parent.input_label_var, parent.input_var, parent.input_unit)
    create_result_frame(parent, parent.result_label_var, parent.output_var, parent.output_unit, parent.coverage_output_var)
    create_formula_frame(parent, parent.preset_var, parent.formula_input1, parent.formula_input1_unit, parent.formula_operator, parent.formula_input2, parent.formula_input2_unit, parent.coverage_rate, parent.ratio_input, parent.primary_mode)


#endregion
#region - Primary Mode


def create_primary_mode_frame(parent, primary_mode):
    # Frame
    primary_mode_frame = ttk.LabelFrame(parent, text="Mode", padding="5")
    primary_mode_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))
    # Frame
    primary_radio_frame = ttk.Frame(primary_mode_frame)
    primary_radio_frame.pack(expand=True)
    # Radio Button
    ttk.Radiobutton(primary_radio_frame, text="By Volume", variable=primary_mode, value="volume").pack(anchor='w', padx=5, pady=2)
    ttk.Radiobutton(primary_radio_frame, text="By Ratio", variable=primary_mode, value="ratio").pack(anchor='w', padx=5, pady=2)


#endregion
#region - Mode


def create_mode_frame(parent, calc_mode, update_labels):
    # Frame
    mode_frame = ttk.LabelFrame(parent, text="Output", padding="5")
    mode_frame.pack(side='left', fill='both', expand=True, padx=5)
    # Frame
    mode_radio_frame = ttk.Frame(mode_frame)
    mode_radio_frame.pack(expand=True)
    # Radio Button
    ttk.Radiobutton(mode_radio_frame, text="Get: Part A", variable=calc_mode, value="partB", command=update_labels).pack(anchor='center', padx=5, pady=2)
    ttk.Radiobutton(mode_radio_frame, text="Get: Part B", variable=calc_mode, value="partA", command=update_labels).pack(anchor='center', padx=5, pady=2)


#endregion
#region - Input


def create_input_frame(parent: 'Main', input_label_var, input_var, input_unit):
    # Frame
    input_frame = ttk.LabelFrame(parent, text="Input", padding="5")
    input_frame.pack(side='left', fill='both', expand=True, padx=(5, 0))
    # Frame
    input_row = ttk.Frame(input_frame)
    input_row.pack(fill='x', expand=True)
    # Label
    ttk.Label(input_row, textvariable=input_label_var, width=18, anchor="center").pack(side='left')
    # Entry
    ttk.Entry(input_row, textvariable=input_var).pack(side='left', fill='x', expand=True)
    # Frame
    unit_frame = ttk.Frame(input_frame)
    unit_frame.pack(fill='x', pady=(5, 0))
    # Combobox
    ttk.Combobox(unit_frame, textvariable=input_unit, values=list(CONVERSIONS.keys()), state='readonly', width=12).pack(side='right')


#endregion
#region - Result


def create_result_frame(parent: 'Main', result_label_var, output_var, output_unit, coverage_output_var):
    # Frame
    result_frame = ttk.LabelFrame(parent, text="Result", padding="5")
    result_frame.pack(fill='x', pady=5)
    # Frame
    result_row = ttk.Frame(result_frame)
    result_row.pack(fill='x')
    # Label
    ttk.Label(result_row, textvariable=result_label_var, width=17, anchor="center").pack(side='left', padx=(0, 5))
    # Entry
    ttk.Entry(result_row, textvariable=output_var, state='readonly').pack(side='left', fill='x', expand=True)
    # Combobox
    ttk.Combobox(result_row, textvariable=output_unit, values=list(CONVERSIONS.keys()), state='readonly', width=12).pack(side='left', padx=(5, 0))
    # Frame
    coverage_row = ttk.Frame(result_frame)
    coverage_row.pack(fill='x', pady=(10, 0))
    # Label
    ttk.Label(coverage_row, text="Coverage", width=17, anchor="center").pack(side='left', padx=(0, 5))
    # Entry
    ttk.Entry(coverage_row, textvariable=coverage_output_var, state='readonly').pack(side='left', fill='x', expand=True)
    # Label
    ttk.Label(coverage_row, text="sq ft", width=15, anchor="center").pack(side='left', padx=(5, 0))


#endregion
#region - Formula


def create_formula_frame(parent: 'Main', preset_var, formula_input1, formula_input1_unit, formula_operator, formula_input2, formula_input2_unit, coverage_rate, ratio_input, primary_mode):
    # Frame
    formula_frame = ttk.LabelFrame(parent, text="Formula", padding="5")
    formula_frame.pack(fill='x', pady=5)
    # Frame
    preset_row = ttk.Frame(formula_frame)
    preset_row.pack(fill='x')
    # Label
    parent.preset_label = ttk.Label(preset_row, text="Preset", width=17, anchor="center")
    parent.preset_label.pack(side='left', padx=(0, 5))
    # Combobox
    parent.preset_combo = ttk.Combobox(preset_row, textvariable=preset_var, values=get_preset_names(), width=20, state='readonly')
    parent.preset_combo.pack(side='left', fill='x', expand=True)
    # Help button
    parent.preset_help_button = ttk.Button(preset_row, text="?", width=2, command=parent.show_preset_info)
    parent.preset_help_button.pack(side='left', padx=(5, 0))

    # Ratio input row
    ratio_row = ttk.Frame(formula_frame)
    ratio_row.pack(fill='x', pady=(10, 0))
    # Label
    parent.ratio_label = ttk.Label(ratio_row, text="Ratio (B:A)", width=17, anchor="center")
    parent.ratio_label.pack(side='left', padx=(0, 5))
    # Entry
    parent.ratio_entry = ttk.Entry(ratio_row, textvariable=ratio_input, width=10)
    parent.ratio_entry.pack(side='left')

    # Frame
    formula_row = ttk.Frame(formula_frame)
    formula_row.pack(fill='x', pady=(10, 0))
    # Label
    parent.formula_label = ttk.Label(formula_row, text="Volume Ratio", width=17, anchor="center")
    parent.formula_label.pack(side='left', padx=(0, 5))
    # Entry
    formula_entry1 = ttk.Entry(formula_row, textvariable=formula_input1, width=4)
    formula_entry1.pack(side='left', fill='x', expand=True)
    # Combobox
    formula_combo1 = ttk.Combobox(formula_row, textvariable=formula_input1_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly')
    formula_combo1.pack(side='left', padx=2)
    formula_operator_combo = ttk.Combobox(formula_row, textvariable=formula_operator, values=["/", "*"], width=4, state='readonly')
    formula_operator_combo.pack(side='left', padx=2)
    # Entry
    formula_entry2 = ttk.Entry(formula_row, textvariable=formula_input2, width=4)
    formula_entry2.pack(side='left', fill='x', expand=True)
    # Combobox
    formula_combo2 = ttk.Combobox(formula_row, textvariable=formula_input2_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly')
    formula_combo2.pack(side='left', padx=2)

    # Frame
    coverage_input_row = ttk.Frame(formula_frame)
    coverage_input_row.pack(fill='x', pady=(10, 0))
    # Label
    ttk.Label(coverage_input_row, text="Coverage Rate", width=17, anchor="center").pack(side='left', padx=(0, 5))
    # Entry
    ttk.Entry(coverage_input_row, textvariable=coverage_rate).pack(side='left', fill='x', expand=True)
    # Label
    ttk.Label(coverage_input_row, text="sq ft/gallon", width=15, anchor="center").pack(side='left', padx=(5, 0))

    # Initialize widget states
    parent.after_idle(parent.update_widget_states)
