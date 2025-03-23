#region - Imports


# Standard
import tkinter as tk
from tkinter import messagebox

# Local
import widgets
from presets import PRESETS
from conversions import CONVERSIONS


#endregion
#region - Constants


WINDOW_TITLE = "Chem-Mix - Chemical Dilution Calculator"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 315


#endregion
#region - App


class ChemMixCalc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root = self


    def run(self):
        self.setup_window()
        self.initialize_variables()
        self.create_widgets()
        self.bind_events()
        self.set_preset_formula()
        self.calculate()


#endregion
#region - Setup


    def setup_window(self):
        self.title(WINDOW_TITLE)
        self.resizable(False, False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}')


    def initialize_variables(self):
        self.calc_mode = tk.StringVar(value="liquid")
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
        self.preset_var = tk.StringVar(value=list(PRESETS.keys())[1])
        self.mixing_ratio = None


    def create_widgets(self):
        self.config(padx=5, pady=5)
        widgets.create_all_widgets(self)


    def bind_events(self):
        trace_list = [
            self.input_var,
            self.formula_input1,
            self.formula_input2,
            self.formula_operator,
            self.input_unit,
            self.output_unit,
            self.formula_input1_unit,
            self.formula_input2_unit,
            self.calc_mode,
            self.coverage_rate,
        ]
        for variable in trace_list:
            variable.trace_add("write", self.calculate)
        self.preset_var.trace_add("write", self.set_preset_formula)


#endregion
#region - Helpers


    def update_results(self, result_ml, coverage_area):
        result = self.convert_from_ml(result_ml, self.output_unit.get())
        self.output_var.set(f"{result:.3f}")
        self.coverage_output_var.set(f"{coverage_area:.1f}")
        self.update_labels()


    def update_labels(self, *args):
        if self.calc_mode.get() == "liquid":
            self.input_label_var.set("Liquid Volume")
        else:
            self.input_label_var.set("Chemical Volume")
        self.result_label_var.set("Chemical Volume" if self.calc_mode.get() == "liquid" else "Liquid Volume")


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


    def set_preset_formula(self, *args):
        preset = PRESETS.get(self.preset_var.get())
        if preset:
            self.formula_input1.set(preset["input1"])
            self.formula_input1_unit.set(preset["input1_unit"])
            self.formula_operator.set(preset["operator"])
            self.formula_input2.set(preset["input2"])
            self.formula_input2_unit.set(preset["input2_unit"])
            self.coverage_rate.set(preset["coverage_rate"])


    def show_preset_info(self):
        preset = PRESETS.get(self.preset_var.get())
        if preset:
            info = preset.get("info", "No information available.")
            messagebox.showinfo("Information", info)


#endregion
#region - Calculation


    def calculate(self, *args):
        self.set_base_ratio()
        try:
            input_in_ml = self.convert_to_ml(self.input_var.get(), self.input_unit.get())
            result_ml, coverage_area = self.calculate_volume(input_in_ml)
            self.update_results(result_ml, coverage_area)
        except (tk.TclError, ValueError, TypeError):
            self.output_var.set("Invalid input")
            self.coverage_output_var.set("Invalid input")


    def calculate_volume(self, input_in_ml):
        mode = self.calc_mode.get()
        if mode == "liquid":
            result_ml = input_in_ml * self.mixing_ratio
            input_in_gallons = self.convert_from_ml(input_in_ml, "Gallon")
            coverage_area = input_in_gallons * self.coverage_rate.get()
        elif mode == "chemical":
            result_ml = input_in_ml / self.mixing_ratio
            result_in_gallons = self.convert_from_ml(result_ml, "Gallon")
            coverage_area = result_in_gallons * self.coverage_rate.get()
        return result_ml, coverage_area


#endregion
#region - Framework


if __name__ == '__main__':
    app = ChemMixCalc()
    app.run()
    app.mainloop()
