#region - Imports


# Standard
import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional, List

# Local
import widgets
from preset_manager import load_presets, save_preset, get_preset_names
from conversions import CONVERSIONS


#endregion
#region - Constants


WINDOW_TITLE = "Chem-Mix"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400


#endregion
#region - App


class Main(tk.Tk):
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
        # App variables
        self.primary_mode = tk.StringVar(value="volume")  # "volume" or "ratio"
        self.calc_mode = tk.StringVar(value="partB")
        self.input_label_var = tk.StringVar(value="Part B Volume")
        self.input_var = tk.DoubleVar(value=1)
        self.input_unit = tk.StringVar(value="Gallon")
        self.output_unit = tk.StringVar(value="Ounce")
        self.result_label_var = tk.StringVar(value="Part A Volume")
        self.output_var = tk.StringVar()
        self.coverage_output_var = tk.StringVar()
        self.formula_input1 = tk.DoubleVar()
        self.formula_operator = tk.StringVar()
        self.formula_input1_unit = tk.StringVar()
        self.formula_input2 = tk.DoubleVar()
        self.formula_input2_unit = tk.StringVar()
        self.coverage_rate = tk.DoubleVar()
        self.preset_names = get_preset_names()
        self.preset_var = tk.StringVar(value=self.preset_names[1] if len(self.preset_names) > 1 else "")
        self.ratio_input = tk.StringVar(value="50:1")
        self.mixing_ratio = None

        # Widget references
        self.preset_label: Optional[ttk.Label] = None
        self.preset_combo: Optional[ttk.Combobox] = None
        self.preset_help_button: Optional[ttk.Button] = None
        self.ratio_label: Optional[ttk.Label] = None
        self.ratio_entry: Optional[ttk.Entry] = None
        self.formula_label: Optional[ttk.Label] = None
        self.formula_widgets: List[ttk.Widget] = []


    def create_widgets(self):
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
            self.primary_mode,
            self.ratio_input,
        ]
        for variable in trace_list:
            variable.trace_add("write", self.calculate)
        self.preset_var.trace_add("write", self.set_preset_formula)
        self.primary_mode.trace_add("write", self.update_widget_states)


#endregion
#region - Helpers


    def update_results(self, result_ml, coverage_area):
        result = self.convert_from_ml(result_ml, self.output_unit.get())
        self.output_var.set(f"{result:.3f}")
        if self.primary_mode.get() == "ratio":
            self.coverage_output_var.set("")
        else:
            self.coverage_output_var.set(f"{coverage_area:.1f}")
        self.update_labels()


    def update_labels(self, *args):
        if self.calc_mode.get() == "partB":
            self.input_label_var.set("Part B Volume")
        else:
            self.input_label_var.set("Part A Volume")
        self.result_label_var.set("Part A Volume" if self.calc_mode.get() == "partB" else "Part B Volume")

    def update_widget_states(self, *args):
        """Enable/disable ratio widgets based on primary mode"""
        if hasattr(self, 'ratio_entry') and hasattr(self, 'ratio_label'):
            if self.primary_mode.get() == "ratio":
                self.ratio_entry.config(state='normal')
                self.ratio_label.config(state='normal')
                if hasattr(self, 'formula_widgets'):
                    for widget in self.formula_widgets:
                        widget.config(state='disabled')
                if hasattr(self, 'formula_label'):
                    self.formula_label.config(state='disabled')
                if hasattr(self, 'preset_combo'):
                    self.preset_combo.config(state='disabled')
                if hasattr(self, 'preset_label'):
                    self.preset_label.config(state='disabled')
                if hasattr(self, 'preset_help_button'):
                    self.preset_help_button.config(state='disabled')
            else:
                self.ratio_entry.config(state='disabled')
                self.ratio_label.config(state='disabled')
                if hasattr(self, 'formula_widgets'):
                    for widget in self.formula_widgets:
                        widget.config(state='normal')
                if hasattr(self, 'formula_label'):
                    self.formula_label.config(state='normal')
                if hasattr(self, 'preset_combo'):
                    self.preset_combo.config(state='readonly')
                if hasattr(self, 'preset_label'):
                    self.preset_label.config(state='normal')
                if hasattr(self, 'preset_help_button'):
                    self.preset_help_button.config(state='normal')


    def convert_to_ml(self, value, from_unit):
        return value * CONVERSIONS[from_unit]


    def convert_from_ml(self, value, to_unit):
        return value / CONVERSIONS[to_unit]


    def set_base_ratio(self):
        try:
            if self.primary_mode.get() == "ratio":
                ratio_parts = self.ratio_input.get().split(':')
                if len(ratio_parts) == 2:
                    partB_ratio = float(ratio_parts[0])
                    partA_ratio = float(ratio_parts[1])
                    self.mixing_ratio = partA_ratio / partB_ratio
                else:
                    self.mixing_ratio = None
            else:
                val1_ml = self.convert_to_ml(self.formula_input1.get(), self.formula_input1_unit.get())
                val2_ml = self.convert_to_ml(self.formula_input2.get(), self.formula_input2_unit.get())
                if self.formula_operator.get() == "/":
                    self.mixing_ratio = val1_ml / val2_ml
                else:
                    self.mixing_ratio = val1_ml * val2_ml
        except:
            pass


    def set_preset_formula(self, *args):
        presets = load_presets()
        preset = presets.get(self.preset_var.get())
        if preset:
            self.formula_input1.set(preset["input1"])
            self.formula_input1_unit.set(preset["input1_unit"])
            self.formula_operator.set(preset["operator"])
            self.formula_input2.set(preset["input2"])
            self.formula_input2_unit.set(preset["input2_unit"])
            self.coverage_rate.set(preset["coverage_rate"])


    def show_preset_info(self):
        presets = load_presets()
        preset = presets.get(self.preset_var.get())
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
        if mode == "partB":
            result_ml = input_in_ml * self.mixing_ratio
            if self.primary_mode.get() == "volume":
                input_in_gallons = self.convert_from_ml(input_in_ml, "Gallon")
                coverage_area = input_in_gallons * self.coverage_rate.get()
            else:
                coverage_area = 0
        elif mode == "partA":
            result_ml = input_in_ml / self.mixing_ratio
            if self.primary_mode.get() == "volume":
                result_in_gallons = self.convert_from_ml(result_ml, "Gallon")
                coverage_area = result_in_gallons * self.coverage_rate.get()
            else:
                coverage_area = 0
        return result_ml, coverage_area


#endregion
#region - Framework


if __name__ == '__main__':
    app = Main()
    app.run()
    app.mainloop()
