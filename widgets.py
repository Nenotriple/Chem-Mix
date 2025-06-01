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


def create_all_widgets(app: 'Main'):
    app.config(padx=5, pady=5)
    # Top frame
    top_frame = ttk.Frame(app)
    top_frame.pack(fill='x', pady=5)
    create_mode_sel_frame(top_frame, app)
    create_output_sel_frame(top_frame, app)
    create_input_frame(top_frame, app)
    # Result frame
    result_frame = ttk.Frame(app)
    result_frame.pack(fill='x', pady=5)
    create_result_frame(result_frame, app)
    # Formula frame
    formula_frame = ttk.Frame(app)
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
