<h1 align="center"> Chem-Mix</h1>
<p align="center">A chemical dilution calculator for mixing ratios and coverage calculations.</p>
<p align="center"><img src="https://github.com/user-attachments/assets/9460f32f-19f0-4a5e-8e5a-fc5ee835a271" alt="cover"></p>


## 📋 Index
- [Features](#features)
- [Usage](#usage)
- [Tips](#tips)
- [Installation](#installation)


## ✨ Features
- Calculate chemical-to-liquid or liquid-to-chemical amounts
- Adjust the unit of measure for any input/output
- Easy to add your own preset formulas `presets.py`
- Description of the selected preset (via `?` button)
- Coverage area calculation
- User-friendly interface
- Results are updated instantly as you adjust the values


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
- Coverage rate is in square feet per gallon
- Add custom presets in `Chem-Mix\presets.py`
- Add additional units or measure in `Chem-Mix\conversions.py`


## 🚀 Installation
1. Ensure [Python](https://www.python.org/downloads/) is installed on your system
2. Clone the repository:
   ```bash
   git clone https://github.com/Nenotriple/Chem-Mix.git
   ```
3. Run `Start.bat` to set up the environment and launch the application
