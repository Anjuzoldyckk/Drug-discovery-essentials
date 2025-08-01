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
