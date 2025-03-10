# This file contains the formula presets for the application.
# The presets include the formula inputs, operators, and coverage rates for each chemical product.
# The presets are used to populate the formula input fields in the application and calculate the chemical dilution/mix ratio based on the selected preset.


"""
"NAME": {
    formula_input1 = Value of the first input
    formula_input1_unit = Unit of Measure
    formula_operator = Operator of the formula, can be "/", or "*".
    formula_input2 = Value of the second input
    formula_input2_unit = Unit of Measure
    coverage_rate = (sq ft. per gallon)
},
"""


PRESETS = {
    "Custom": "",
    "Spectracide: Triazicide": {
        "formula_input1":       2,
        "formula_input1_unit":  "Tablespoon",
        "formula_operator":     "/",
        "formula_input2":       3,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        120
    },
    "Spectracide: Weed Stop": {
        "formula_input1":       5,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        500
    },
    "Spectracide: Immunox - Lawn": {
        "formula_input1":       7,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        500
    },
    "Spectracide: Immunox - Garden": {
        "formula_input1":       1,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        120
    },
    "Roundup: Weed & Grass": {
        "formula_input1":       6,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        300
    },
}
