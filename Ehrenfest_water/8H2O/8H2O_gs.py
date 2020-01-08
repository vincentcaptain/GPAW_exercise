from ase import Atoms
from gpaw import GPAW
from ase.io import read


name = 'H2O_laser_8'
l = read("water_8.xyz", format = 'xyz')
atoms = l
atoms.set_pbc(True)
atoms.set_cell([9.84,4.92,4.92])

calc = GPAW(h = 0.1, nbands = 64, basis = 'dzp', txt = name + '_gs.txt')
atoms.set_calculator(calc)
atoms.get_potential_energy()
calc.write(name + '_gs.gpw', mode = 'all')
