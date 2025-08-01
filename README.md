# Drug-discovery-essentials
Random snippets of code

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
