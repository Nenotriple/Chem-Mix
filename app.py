import tkinter as tk
from functools import wraps

from presets import PRESETS
from conversions import CONVERSIONS
import widgets


WINDOW_TITLE = "Chemical Dilution Calculator"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 315


class ChemMixCalc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root = self
        self.title(WINDOW_TITLE)
        self.resizable(False, False)
        self.center_window()
        self.initialize_variables()
        self.create_widgets()
        self.bind_events()
        self.calculate()


    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}')


    def initialize_variables(self):
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
        self.debounce_timer = None


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
            self.preset_var,
        ]
        for variable in trace_list:
            variable.trace_add("write", self.calculate)


    def update_labels(self, *args):
        if self.calc_mode.get() == "volume":
            self.input_label_var.set("Liquid Volume")
        else:
            self.input_label_var.set("Chemical Volume")
        self.result_label_var.set("Chemical Volume" if self.calc_mode.get() == "volume" else "Liquid Volume")


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


    def on_preset_change(self, *args):
        preset = PRESETS.get(self.preset_var.get())
        if preset:
            self.formula_input1.set(preset["formula_input1"])
            self.formula_input1_unit.set(preset["formula_input1_unit"])
            self.formula_operator.set(preset["formula_operator"])
            self.formula_input2.set(preset["formula_input2"])
            self.formula_input2_unit.set(preset["formula_input2_unit"])
            self.coverage_rate.set(preset["coverage_rate"])


    def debounce(self, delay=100):
        def decorator(func):
            @wraps(func)
            def debounced(*args, **kwargs):
                if self.debounce_timer is not None:
                    self.after_cancel(self.debounce_timer)
                self.debounce_timer = self.after(delay, lambda: func(*args, **kwargs))
            return debounced
        return decorator


    @property
    def calculate(self):
        @self.debounce(delay=250)
        def _calculate(*args):
            self.on_preset_change()
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
                self.update_labels()
            except (tk.TclError, ValueError, TypeError):
                self.output_var.set("Invalid input")
                self.coverage_output_var.set("Invalid input")
        return _calculate


if __name__ == '__main__':
    app = ChemMixCalc()
    app.mainloop()
