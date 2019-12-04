from gpaw.tddft import TDDFT
from gpaw.tddft.ehrenfest import EhrenfestVelocityVerlet
from gpaw.tddft.laser import CWField
from ase.units import Hartree, Bohr, AUT
from ase.io import Trajectory
from ase.parallel import parprint

name = 'H2O_laser'

# Ehrenfest simulation parameters
