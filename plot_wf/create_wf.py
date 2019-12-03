# Plot wave functions of CO molecule
from ase import Atoms
from gpaw import GPAW

d = 1.1 # bondlength of H2
a = 5.0 # unit cell size
c = a / 2
atoms = Atoms("CO",
				positions = [(c - d / 2, c, c), 
							(c + d / 2, c, c)],
				cell = (a, a, a))

calc = GPAW(nbands = 5, h = 0.2, txt = None)
atoms.set_calculator(calc)

# Start calculation
energy = atoms.get_potential_energy()

# Save WF
calc.write("CO.gpw", mode = "all")

