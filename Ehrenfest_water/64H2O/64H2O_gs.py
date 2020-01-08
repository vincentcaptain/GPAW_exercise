from ase import Atoms
from gpaw import GPAW
from ase.io import read


name = 'H2O_laser_64'
l = read("water_64.xyz", format = 'xyz')
atoms = l
atoms.set_pbc(True)
atoms.set_cell([9.80,9.80,19.37])

calc = GPAW(h = 0.1, nbands = 512, basis = 'dzp', txt = name + '_gs.txt')
atoms.set_calculator(calc)
atoms.get_potential_energy()
calc.write(name + '_gs.gpw', mode = 'all')
