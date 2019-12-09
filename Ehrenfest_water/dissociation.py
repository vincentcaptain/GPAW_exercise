from gpaw.tddft import TDDFT
from gpaw.tddft.ehrenfest import EhrenfestVelocityVerlet
from gpaw.tddft.laser import CWField
from ase.units import Hartree, Bohr, AUT
from ase.io import Trajectory
from ase.parallel import parprint

name = 'H2O_laser'

# Ehrenfest simulation parameters
timestep = 40.0					# 10 attoseconds
ndiv = 10						# dump traj every 10 timesteps
niter = 500						# up to 500 timesteps = 20 fs

# TDDFT calculator with external potential from intense harmonic laser field
# Laser parameters:
# -- field intensity: E = sqrt(377*Pd) = 6.14E9 V/m = 0.0119 au
# -- field freq: w = 0.057 au
# -- switch on time: 40 attoseconds = 1.654 aut
tdcalc = TDDFT(name + '_gs.gpw', 
			   txt = name + '_td.txt', 
			   propagator = "EFSICN", 
			   solver = "BiCGStab", 
			   td_potential = CWField(0.0119, 0.057, 1.654))

# New object for velocity verlet
ehrenfest = EhrenfestVelocityVerlet(tdcalc)

# Another object to save the dynamics
traj = Trajectory(name + '_td.traj', 'w', tdcalc.get_atoms())