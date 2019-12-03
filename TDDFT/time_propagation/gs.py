from ase import Atoms
from gpaw import GPAW

# Beryllium atom
atoms = Atoms(symbols = "Be", 
			  positions = [(0, 0, 0)], 
			  pbc = False)

# 6.0 A vacuum around the atom
atoms.center(vacuum = 6.0)

# Create GPAW calculator
calc = GPAW(nbands = 1, h = 0.3)
# Attach calculator to atoms
atoms.set_calculator(calc)

# Calculate the ground state
energy = atoms.get_potential_energy()

# Save the ground state
calc.write('be_gs.gpw', 'all')