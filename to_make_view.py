from ase.io import read
from ase.visualize import view

cif_file = "test_water_mol.cif"
molecule = read(cif_file)

view(molecule)