# Drug-discovery-essentials
Random snippets of code

Of course! Here are the docstrings for your functions and a sample GitHub README description for the script.

Python Code with Docstrings
Here's your code, now with docstrings added to explain what each part does.

Python

from docx import Document
import math
import csv

def calculate_pIC50(binding_energy):
    """Calculates pIC50 from binding energy (in kcal/mol).

    This conversion uses the approximate relationship derived from the Gibbs free
    energy equation at room temperature (298K): pIC50 ≈ -ΔG / 1.364.

    Args:
        binding_energy (str or float): The binding energy value, typically in kcal/mol.

    Returns:
        float: The calculated pIC50 value.
    """
    return -float(binding_energy) / 1.364

def calculate_IC50(pIC50):
    """Converts a pIC50 value to an IC50 value in Molar units.

    The conversion is based on the formula: IC50 = 10^(-pIC50).

    Args:
        pIC50 (float): The pIC50 value.

    Returns:
        float: The calculated IC50 value in Molar (M).
    """
    return 10 ** (-pIC50)  # IC50 in Molar

# --- Main script execution ---

# Load your document
# Assumes the Word document is named 'binding enrgy.docx' and is in the same directory.
doc = Document('binding enrgy.docx')

data = []
# Iterate through all tables in the document
for table in doc.tables:
    # Iterate through rows, skipping the header row (table.rows[1:])
    for row in table.rows[1:]:
        name = row.cells[0].text.strip()
        energy = row.cells[1].text.strip()

        # Skip rows with empty cells for name or energy
        if not name or not energy:
            continue
        
        # Calculate values and handle potential errors (e.g., non-numeric energy)
        try:
            pIC50 = calculate_pIC50(energy)
            IC50 = calculate_IC50(pIC50)
            data.append([name, float(energy), round(pIC50, 4), f"{IC50:.4e}"])
        except Exception as e:
            print(f"Skipping row for '{name}' due to error: {e}")

# Write the processed data to a CSV file
with open('results_from_docx.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Write the header row for the CSV file
    writer.writerow(['compound_name', 'binding_energy', 'pIC50', 'IC50 (M)'])
    # Write all the processed data rows
    writer.writerows(data)

print("✅ Done! Check the output file: results_from_docx.csv")

GitHub README Description
Here is a template you can use for your README.md file on GitHub.

Docking Results to IC50 Converter 🔬
A simple yet powerful Python script to extract molecular docking results (compound name and binding energy) from a Microsoft Word (.docx) file, calculate the corresponding pIC50 and IC50 values, and export the data into a clean CSV file.

Features ✨
Parses .docx Files: Directly reads tables from a Word document, eliminating the need for manual copy-pasting.

Automated Calculations: Converts binding energy (kcal/mol) to pIC50 and IC50 (Molar).

Error Handling: Gracefully skips rows with invalid or missing data.

Structured Output: Generates a tidy, analysis-ready .csv file.

How It Works 🧪
The script uses two key pharmacological formulas for its conversions:

Binding Energy to pIC50: The pIC50 is estimated from the binding free energy (
DeltaG) using the following approximation, which is valid at room temperature (298K):

$$$$$$pIC50 \\approx -\\frac{\\Delta G (\\text{kcal/mol})}{1.364} $$
$$$$

pIC50 to IC50: The IC50 value (in Molar concentration) is calculated from the pIC50 using its standard definition:

$$$$$$IC50 (M) = 10^{-pIC50} $$
$$$$

Usage Guide 🚀
1. Prerequisites
Make sure you have Python installed. You will need to install the python-docx library.

Bash

pip install python-docx
2. Input File Format
Create a Microsoft Word file named binding enrgy.docx in the same directory as the script.

Inside the document, create a table with at least two columns.

The first column should contain the Compound Name.

The second column should contain the Binding Energy (in kcal/mol).

The script is designed to skip the header row of the table.

Example Input Table in binding enrgy.docx:

Compound Name	Binding Energy (kcal/mol)
Compound-A	-9.8
Compound-B	-10.5
Compound-C	-8.2

Export to Sheets
3. Run the Script
Open your terminal or command prompt, navigate to the script's directory, and run:

Bash

python your_script_name.py
4. Check the Output
The script will generate a file named results_from_docx.csv.

Example results_from_docx.csv Output:

Code snippet

compound_name,binding_energy,pIC50,IC50 (M)
Compound-A,-9.8,7.1847,6.5352e-08
Compound-B,-10.5,7.6979,2.0047e-08
Compound-C,-8.2,6.0117,9.7335e-07
