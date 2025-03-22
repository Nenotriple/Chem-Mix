"""
------------
Description:
------------
This file contains the formula presets for the application.
The presets include the formula inputs, operators, and coverage rates for each chemical product.
The presets are used to populate the formula input fields in the application and calculate the chemical dilution/mix ratio based on the selected preset.


--------------
Preset Format:
--------------
"NAME": {
    formula_input1 = Value of the first input
    formula_input1_unit = Unit of Measure
    formula_operator = Operator of the formula, can be "/", or "*".
    formula_input2 = Value of the second input
    formula_input2_unit = Unit of Measure
    coverage_rate = (sq ft. per gallon)
},


-----------------
Units of Measure:
-----------------
Milliliter
Teaspoon
Tablespoon
Ounce
Cup
Pint
Quart
Liter
Gallon
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

    "Miracle-Grow: Liquid Plant Food - Garden": {
        "formula_input1":       1.2,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       2,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        20
    },

    "Miracle-Grow: Liquid Plant Food - Houseplant": {
        "formula_input1":       5,
        "formula_input1_unit":  "Milliliter",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        10,
    },

    "Bleach: 10,000 ppm (1min Sanitize)": {
        "formula_input1":       18,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        200,
    },

    "Bleach: 5,000 ppm (1min Sanitize)": {
        "formula_input1":       14,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        160,
    },

    "Bleach: 2400 ppm (1min Sanitize)": {
        "formula_input1":       6,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        140,
    },

    "Bleach: 800 ppm (1-2min Sanitize)": {
        "formula_input1":       2,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        130,
    },

    "Bleach: 200 ppm (2min Sanitize)": {
        "formula_input1":       0.5,
        "formula_input1_unit":  "Ounce",
        "formula_operator":     "/",
        "formula_input2":       1,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        120,
    },

    "Bleach: 5 ppm (Drinkable)": {
        "formula_input1":       1,
        "formula_input1_unit":  "Teaspoon",
        "formula_operator":     "/",
        "formula_input2":       10,
        "formula_input2_unit":  "Gallon",
        "coverage_rate":        100,
    },
}
