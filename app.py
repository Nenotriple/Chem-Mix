import tkinter as tk
from tkinter import ttk

from presets import PRESETS
from conversions import CONVERSIONS


WINDOW_TITLE = "Chemical Dilution Calculator"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 315


class ChemMixCalc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root = self
        self.title(WINDOW_TITLE)
        self.resizable(False, False)
        # Variables
        self.calc_mode = tk.StringVar(value="volume")
        self.input_label_var = tk.StringVar(value="Liquid Volume")
        self.input_var = tk.DoubleVar(value=1)
        self.input_unit = tk.StringVar(value="Gallon")
        self.output_unit = tk.StringVar(value="Ounce")
        self.result_label_var = tk.StringVar(value="Chemical Volume")
        self.output_var = tk.StringVar()
        self.coverage_output_var = tk.StringVar()
        self.formula_input1 = tk.DoubleVar()
        self.formula_operator = tk.StringVar()
        self.formula_input1_unit = tk.StringVar()
        self.formula_input2 = tk.DoubleVar()
        self.formula_input2_unit = tk.StringVar()
        self.coverage_rate = tk.DoubleVar()
        self.preset_var = tk.StringVar(value=next(iter(PRESETS)))
        self.mixing_ratio = None

        # Create Interface
        self.center_window()
        self.create_widgets()
        self.bind_events()
        self.on_preset_change()
        self.calculate()


    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = WINDOW_WIDTH
        window_height = WINDOW_HEIGHT
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')


    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self, padding="5")
        main_frame.pack(expand=True, fill='both')
        # Top row frame
        top_row_frame = ttk.Frame(main_frame)
        top_row_frame.pack(fill='x', pady=5)
        # Mode frame
        mode_frame = ttk.LabelFrame(top_row_frame, text="Calculation Mode", padding="5")
        mode_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))
        # Mode selection
        mode_radio_frame = ttk.Frame(mode_frame)
        mode_radio_frame.pack(expand=True)
        ttk.Radiobutton(mode_radio_frame, text="Chemical from Volume", variable=self.calc_mode, value="volume", command=self.update_labels).pack(anchor='center', padx=5, pady=2)
        ttk.Radiobutton(mode_radio_frame, text="Volume from Chemical", variable=self.calc_mode, value="Chemical", command=self.update_labels).pack(anchor='center', padx=5, pady=2)
        # Input frame
        input_frame = ttk.LabelFrame(top_row_frame, text="Input", padding="5")
        input_frame.pack(side='left', fill='both', expand=True, padx=(5, 0))
        # Input row
        input_row = ttk.Frame(input_frame)
        input_row.pack(fill='x', expand=True)
        ttk.Label(input_row, textvariable=self.input_label_var, width=18, anchor="center").pack(side='left')
        ttk.Entry(input_row, textvariable=self.input_var).pack(side='left', fill='x', expand=True)
        # Input unit selection
        unit_frame = ttk.Frame(input_frame)
        unit_frame.pack(fill='x', pady=(5, 0))
        ttk.Combobox(unit_frame, textvariable=self.input_unit, values=list(CONVERSIONS.keys()), state='readonly', width=12).pack(side='right')
        # Result frame
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="5")
        result_frame.pack(fill='x', pady=5)
        # Result row
        result_row = ttk.Frame(result_frame)
        result_row.pack(fill='x')
        ttk.Label(result_row, textvariable=self.result_label_var, width=17, anchor="center").pack(side='left', padx=(0,5))
        ttk.Entry(result_row, textvariable=self.output_var, state='readonly').pack(side='left', fill='x', expand=True)
        ttk.Combobox(result_row, textvariable=self.output_unit, values=list(CONVERSIONS.keys()), state='readonly', width=12).pack(side='left', padx=(5,0))
        # Coverage output
        coverage_row = ttk.Frame(result_frame)
        coverage_row.pack(fill='x', pady=(10,0))
        ttk.Label(coverage_row, text="Coverage", width=17, anchor="center").pack(side='left', padx=(0,5))
        ttk.Entry(coverage_row, textvariable=self.coverage_output_var, state='readonly').pack(side='left', fill='x', expand=True)
        ttk.Label(coverage_row, text="sq ft", width=15, anchor="center").pack(side='left', padx=(5,0))
        # Formula frame
        formula_frame = ttk.LabelFrame(main_frame, text="Formula", padding="5")
        formula_frame.pack(fill='x', pady=5)
        # Preset row
        preset_row = ttk.Frame(formula_frame)
        preset_row.pack(fill='x')
        ttk.Label(preset_row, text="Preset", width=17, anchor="center").pack(side='left', padx=(0,5))
        preset_combo = ttk.Combobox(preset_row, textvariable=self.preset_var, values=list(PRESETS.keys()), width=20, state='readonly')
        preset_combo.pack(side='left', fill='x', expand=True)
        # Formula row
        formula_row = ttk.Frame(formula_frame)
        formula_row.pack(fill='x', pady=(10,0))
        ttk.Label(formula_row, text="Ratio", width=17, anchor="center").pack(side='left', padx=(0,5))
        ttk.Entry(formula_row, textvariable=self.formula_input1, width=4).pack(side='left', fill='x', expand=True)
        ttk.Combobox(formula_row, textvariable=self.formula_input1_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly').pack(side='left', padx=2)
        ttk.Combobox(formula_row, textvariable=self.formula_operator, values=["/", "*"], width=4, state='readonly').pack(side='left', padx=2)
        ttk.Entry(formula_row, textvariable=self.formula_input2, width=4).pack(side='left', fill='x', expand=True)
        ttk.Combobox(formula_row, textvariable=self.formula_input2_unit, values=list(CONVERSIONS.keys()), width=12, state='readonly').pack(side='left', padx=2)
        # Coverage row
        coverage_input_row = ttk.Frame(formula_frame)
        coverage_input_row.pack(fill='x', pady=(10,0))
        ttk.Label(coverage_input_row, text="Coverage Rate", width=17, anchor="center").pack(side='left', padx=(0,5))
        ttk.Entry(coverage_input_row, textvariable=self.coverage_rate).pack(side='left', fill='x', expand=True)
        ttk.Label(coverage_input_row, text="sq ft/gallon", width=15, anchor="center").pack(side='left', padx=(5,0))


    def bind_events(self):
        trace_list = [
            (self.input_var,            self.calculate),
            (self.formula_input1,       self.calculate),
            (self.formula_input2,       self.calculate),
            (self.formula_operator,     self.calculate),
            (self.input_unit,           self.calculate),
            (self.output_unit,          self.calculate),
            (self.formula_input1_unit,  self.calculate),
            (self.formula_input2_unit,  self.calculate),
            (self.calc_mode,            self.update_labels),
            (self.coverage_rate,        self.calculate),
            (self.preset_var,           self.on_preset_change),
        ]
        for variable, callback in trace_list:
            variable.trace_add("write", callback)


    def update_labels(self, *args):
        if self.calc_mode.get() == "volume":
            self.input_label_var.set("Liquid Volume")
        else:
            self.input_label_var.set("Chemical Volume")
        self.calculate()


    def convert_to_ml(self, value, from_unit):
        return value * CONVERSIONS[from_unit]


    def convert_from_ml(self, value, to_unit):
        return value / CONVERSIONS[to_unit]


    def set_base_ratio(self):
        try:
            val1_ml = self.convert_to_ml(self.formula_input1.get(), self.formula_input1_unit.get())
            val2_ml = self.convert_to_ml(self.formula_input2.get(), self.formula_input2_unit.get())
            if self.formula_operator.get() == "/":
                self.mixing_ratio = val1_ml / val2_ml
            else:
                self.mixing_ratio = val1_ml * val2_ml
        except:
            pass


    def calculate(self, *args):
        self.set_base_ratio()
        try:
            input_value = self.input_var.get()
            input_in_ml = self.convert_to_ml(input_value, self.input_unit.get())

            if self.calc_mode.get() == "volume":
                result_ml = input_in_ml * self.mixing_ratio
                input_in_gallons = self.convert_from_ml(input_in_ml, "Gallon")
                coverage_area = input_in_gallons * self.coverage_rate.get()
            else:
                result_ml = input_in_ml / self.mixing_ratio
                result_in_gallons = self.convert_from_ml(result_ml, "Gallon")
                coverage_area = result_in_gallons * self.coverage_rate.get()

            result = self.convert_from_ml(result_ml, self.output_unit.get())
            self.output_var.set(f"{result:.3f}")
            self.coverage_output_var.set(f"{coverage_area:.1f}")
            self.result_label_var.set("Chemical Volume" if self.calc_mode.get() == "volume" else "Liquid Volume")

        except (tk.TclError, ValueError, TypeError):
            self.output_var.set("Invalid input")
            self.coverage_output_var.set("Invalid input")


    def on_preset_change(self, *args):
        preset = PRESETS.get(self.preset_var.get())
        if preset:
            self.formula_input1.set(preset["formula_input1"])
            self.formula_input1_unit.set(preset["formula_input1_unit"])
            self.formula_operator.set(preset["formula_operator"])
            self.formula_input2.set(preset["formula_input2"])
            self.formula_input2_unit.set(preset["formula_input2_unit"])
            self.coverage_rate.set(preset["coverage_rate"])


if __name__ == '__main__':
    app = ChemMixCalc()
    app.mainloop()
