#endregion
#region - Imports


# Standard
from tkinter import ttk

# Local
from presets import PRESETS
from conversions import CONVERSIONS


#endregion
#region - All


def create_all_widgets(parent):
        top_frame = ttk.Frame(parent)
        top_frame.pack(fill='x', pady=5)
        create_mode_frame(top_frame, parent.calc_mode, parent.update_labels)
        create_input_frame(top_frame, parent.input_label_var, parent.input_var, parent.input_unit)
        create_result_frame(parent, parent.result_label_var, parent.output_var, parent.output_unit, parent.coverage_output_var)
        create_formula_frame(parent, parent.preset_var, parent.formula_input1, parent.formula_input1_unit, parent.formula_operator, parent.formula_input2, parent.formula_input2_unit, parent.coverage_rate)


#endregion
#region - Mode


def create_mode_frame(parent, calc_mode, update_labels):
    # Frame
    mode_frame = ttk.LabelFrame(parent, text="Calculation Mode", padding="5")
    mode_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))
    # Frame
    mode_radio_frame = ttk.Frame(mode_frame)
    mode_radio_frame.pack(expand=True)
    # Radio Button
    ttk.Radiobutton(mode_radio_frame, text="Get: Chemical from liquid", variable=calc_mode, value="liquid", command=update_labels).pack(anchor='center', padx=5, pady=2)
    ttk.Radiobutton(mode_radio_frame, text="Get: Liquid from chemical", variable=calc_mode, value="chemical", command=update_labels).pack(anchor='center', padx=5, pady=2)


#endregion
#region - Input


def create_input_frame(parent, input_label_var, input_var, input_unit):
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


def create_result_frame(parent, result_label_var, output_var, output_unit, coverage_output_var):
    # Frame
    result_frame = ttk.LabelFrame(parent, text="Result", padding="5")
    result_frame.pack(fill='x', pady=5)
    # Frame
    result_row = ttk.Frame(result_frame)
    result_row.pack(fill='x')
    # Label
    ttk.Label(result_row, textvariable=result_label_var, width=17, anchor="center").pack(side='left', padx=(0,5))
    # Entry
    ttk.Entry(result_row, textvariable=output_var, state='readonly').pack(side='left', fill='x', expand=True)
    # Combobox
    ttk.Combobox(result_row, textvariable=output_unit, values=list(CONVERSIONS.keys()), state='readonly', width=12).pack(side='left', padx=(5,0))
    # Frame
    coverage_row = ttk.Frame(result_frame)
    coverage_row.pack(fill='x', pady=(10,0))
    # Label
    ttk.Label(coverage_row, text="Coverage", width=17, anchor="center").pack(side='left', padx=(0,5))
    # Entry
    ttk.Entry(coverage_row, textvariable=coverage_output_var, state='readonly').pack(side='left', fill='x', expand=True)
    # Label
    ttk.Label(coverage_row, text="sq ft", width=15, anchor="center").pack(side='left', padx=(5,0))


#endregion
#region - Formula


def create_formula_frame(parent, preset_var, formula_input1, formula_input1_unit, formula_operator, formula_input2, formula_input2_unit, coverage_rate):
    # Frame
    formula_frame = ttk.LabelFrame(parent, text="Formula", padding="5")
    formula_frame.pack(fill='x', pady=5)
    # Frame
    preset_row = ttk.Frame(formula_frame)
    preset_row.pack(fill='x')
    # Label
    ttk.Label(preset_row, text="Preset", width=17, anchor="center").pack(side='left', padx=(0,5))
    # Combobox
    preset_combo = ttk.Combobox(preset_row, textvariable=preset_var, values=list(PRESETS.keys()), width=20, state='readonly')
    preset_combo.pack(side='left', fill='x', expand=True)
    # Frame
    formula_row = ttk.Frame(formula_frame)
    formula_row.pack(fill='x', pady=(10,0))
    # Label
    ttk.Label(formula_row, text="Ratio", width=17, anchor="center").pack(side='left', padx=(0,5))
    # Entry
    ttk.Entry(formula_row, textvariable=formula_input1, width=4).pack(side='left', fill='x', expand=True)
    # Combobox
    ttk.Combobox(formula_row, textvariable=formula_input1_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly').pack(side='left', padx=2)
    ttk.Combobox(formula_row, textvariable=formula_operator, values=["/", "*"], width=4, state='readonly').pack(side='left', padx=2)
    # Entry
    ttk.Entry(formula_row, textvariable=formula_input2, width=4).pack(side='left', fill='x', expand=True)
    # Combobox
    ttk.Combobox(formula_row, textvariable=formula_input2_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly').pack(side='left', padx=2)
    # Frame
    coverage_input_row = ttk.Frame(formula_frame)
    coverage_input_row.pack(fill='x', pady=(10,0))
    # Label
    ttk.Label(coverage_input_row, text="Coverage Rate", width=17, anchor="center").pack(side='left', padx=(0,5))
    # Entry
    ttk.Entry(coverage_input_row, textvariable=coverage_rate).pack(side='left', fill='x', expand=True)
    # Label
    ttk.Label(coverage_input_row, text="sq ft/gallon", width=15, anchor="center").pack(side='left', padx=(5,0))
