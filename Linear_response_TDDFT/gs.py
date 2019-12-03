from ase import Atoms
from gpaw import GPAW

# Same Be atom
atoms = Atoms(symbols = "Be", 
			  positions = [(0, 0, 0)], 
			  pbc = False)

# same box size
atoms.center(vacuum = 4.0)

# GPAW calculator
calc = GPAW(nbands = 10, h = 0.3)
# Attach calculator to atoms
atoms.set_calculator(calc)

# Compute GS
energy = atoms.get_potential_energy()

# converge the empty states as well
calc.set(convergence = {'bands': 8}, 
		 fixdensity = True, 
		 eigensolver = "cg")
atoms.get_potential_energy()

# save gs
calc.write("Be_gs_8bands.gpw", 'all')