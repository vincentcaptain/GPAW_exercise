from ase import Atoms
from gpaw import GPAW

name = "h2_diss"

d_bond = 0.754
atoms = Atoms("H2", positions = [(0, 0, 0), (0, 0, d_bond)])
atoms.set_pbc(False)
atoms.center(vacuum = 4.0)

calc = GPAW(h = 0.3, nbands = 1, basis = 'dzp', txt = name + '_gs.txt')
atoms.set_calculator(calc)
atoms.get_potential_energy()
calc.write(name + "_gs.gpw", mode = 'all')