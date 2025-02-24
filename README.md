# Chem-Mix

A chemical dilution calculator for mixing ratios and coverage calculations.

[cover]()


## 📋 Index
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tips](#tips)


## ✨ Features
- Calculate chemical-to-liquid or liquid-to-chemical ratios
- Built-in conversion support for common measurements
- Coverage area calculation
- Preset mixing formulas
- Real-time calculations
- User-friendly interface


## 🚀 Installation
1. Ensure [Python](https://www.python.org/downloads/) is installed on your system
2. Clone the repository:
   ```bash
   git clone https://github.com/Nenotriple/Chem-Mix.git
   ```
3. Run `Start.bat` to set up the environment and launch the application


## 💡 Usage
1. Select calculation mode:
   - "Get: Chemical from liquid" - Calculate chemical volume needed
   - "Get: Liquid from chemical" - Calculate liquid volume needed
2. Enter the input volume
3. Select input/output units
4. Choose a preset or enter custom mixing ratio
5. View results and coverage area


### Mixing Ratio Format
- Format: `[Value 1] [Unit 1] [Operator] [Value 2] [Unit 2]`
- Example: `1 Ounce / 1 Gallon`
- Operators:
  - `/` (per)
  - `*` (multiply)


## 💭 Tips
- Use presets for common mixing ratios
- Coverage rate is in square feet per gallon
- All calculations update in real-time
- Units can be changed at any time
- Add custom presets in `Chem-Mix\presets.py`

