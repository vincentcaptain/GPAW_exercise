from ase import Atoms
from gpaw import GPAW
from ase.build import molecule

name = 'H2O_laser'

atoms = molecule('H2O')

atoms.set_pbc(False)
atoms.center(vacuum = 4.0)

calc = GPAW(h = 0.2, nbands = 4, basis = 'dzp', txt = name + '_gs.txt')
atoms.set_calculator(calc)
atoms.get_potential_energy()
calc.write(name + '_gs.gpw', mode = 'all')