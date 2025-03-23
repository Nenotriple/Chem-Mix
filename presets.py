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
    "input1":           :Value of the first input (int/float)
    "input1_unit":      :Unit of Measure (e.g., "Ounce", "Gallon")
    "operator":         :Operator of the formula, can be "/", or "*".
    "input2":           :Value of the second input (int/float)
    "input2_unit":      :Unit of Measure (e.g., "Ounce", "Gallon")
    "coverage_rate":    :(sq ft. per gallon) (int)
    "info":             :Any additional information about the preset or chemical product (optional) (str)
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
    "input1":           2,
    "input1_unit":      "Tablespoon",
    "operator":         "/",
    "input2":           3,
    "input2_unit":      "Gallon",
    "coverage_rate":    120,
    "info":             "A broad-spectrum insecticide that kills over 260 listed insects by contact, including fleas, ticks, and Japanese beetles, providing up to three months of protection for lawns and landscapes."
},

"Spectracide: Weed Stop": {
    "input1":           5,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    500,
    "info":             "A herbicide designed to eliminate various broadleaf weeds, ensuring a healthier lawn by targeting unwanted plants without harming grass."
},

"Spectracide: Immunox - Lawn": {
    "input1":           7,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    500,
    "info":             "A systemic fungicide that protects lawns from common fungal diseases, promoting greener and healthier grass."
},

"Spectracide: Immunox - Garden": {
    "input1":           1,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    120,
    "info":             "A fungicide formulated to safeguard gardens against a range of fungal infections, ensuring the vitality of vegetables, flowers, trees, and shrubs."
},

"Roundup: Weed & Grass": {
    "input1":           6,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    300,
    "info":             "A non-selective herbicide that kills tough weeds and grasses to the root, including dandelion, large crabgrass, poison ivy, and clover."
},

"Miracle-Gro: Liquid Plant Food - Garden": {
    "input1":           1.2,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           2,
    "input2_unit":      "Gallon",
    "coverage_rate":    20,
    "info":             "A liquid fertilizer that provides essential nutrients to promote vigorous growth and abundant blooms."
                        "\n\nThis preset is suitable for outdoor plants and flowers."
},

"Miracle-Gro: Liquid Plant Food - Houseplant": {
    "input1":           5,
    "input1_unit":      "Milliliter",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    10,
    "info":             "A liquid fertilizer that provides essential nutrients to promote vigorous growth and abundant blooms."
                        "\n\nThis preset is suitable for indoor plants and flowers."
},

"Bleach: 10,000 ppm (1min Sanitize)": {
    "input1":           18,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    200,
    "info":             "A high-concentration bleach solution intended for rapid sanitation, achieving effective disinfection in one minute."
                        "\n\nSuch high concentrations are typically used for disinfecting surfaces contaminated with bodily fluids or during outbreak control situations."
},

"Bleach: 5,000 ppm (1min Sanitize)": {
    "input1":           14,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    160,
    "info":             "A bleach solution with a concentration of 5,000 ppm, suitable for quick sanitation needs with a one-minute contact time."
                        "\n\nThis concentration is also appropriate for disinfecting areas with high contamination levels."
},

"Bleach: 2400 ppm (1min Sanitize)": {
    "input1":           6,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    140,
    "info":             "A moderately concentrated bleach solution effective for sanitizing surfaces within one minute."
                        "\n\nThis level is often used in healthcare settings for routine disinfection of non-critical surfaces."
},

"Bleach: 800 ppm (1-2min Sanitize)": {
    "input1":           2,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    130,
    "info":             "A bleach solution with 800 ppm concentration, ideal for general sanitation purposes with a contact time of one to two minutes."
                        "\n\nThis concentration is suitable for disinfecting surfaces in childcare and similar environments."
},

"Bleach: 200 ppm (2min Sanitize)": {
    "input1":           0.5,
    "input1_unit":      "Ounce",
    "operator":         "/",
    "input2":           1,
    "input2_unit":      "Gallon",
    "coverage_rate":    120,
    "info":             "A dilute bleach solution suitable for light sanitization tasks, requiring a two-minute contact time for effectiveness."
                        "\n\nThis level is often used for sanitizing dishes, utensils, and food-contact surfaces."
},

"Bleach: 5 ppm (Drinkable)": {
    "input1":           1,
    "input1_unit":      "Teaspoon",
    "operator":         "/",
    "input2":           10,
    "input2_unit":      "Gallon",
    "coverage_rate":    100,
    "info":             "A minimal concentration bleach solution used to disinfect drinking water, ensuring safety for consumption."
                        "\n\nThis low concentration effectively eliminates harmful pathogens without posing health risks."
                        "\n\nIt's important to note that active chlorine will be used up faster in dirtier, cloudier water, especially water with algae."
                        "\n\nChlorine test strips are recommended to ensure proper disinfection and safety."
                        "\n\nIf the water is especially dirty and you need to drink, and you can't filter it, you may need to add more. Stop adding bleach the moment you smell or taste it in the water."
},
}
