from gpaw.tddft import TDDFT
from gpaw.tddft.ehrenfest import EhrenfestVelocityVerlet
from gpaw.tddft.laser import CWField
from ase.units import Hartree, Bohr, AUT
from ase.io import Trajectory
from ase.parallel import parprint

name = 'H2O_laser'

# Ehrenfest simulation parameters
timestep = 40.0					# 40 attoseconds
ndiv = 10						# dump traj every 10 timesteps
niter = 500						# up to 500 timesteps = 20 fs

# TDDFT calculator with external potential from intense harmonic laser field
# Laser parameters:
# -- field intensity: E = sqrt(754*Pd) = 8.68E9 V/m = 0.0169 au
# -- field freq: w = 0.057 au
# -- switch on time: 20000 attoseconds = 827 aut
tdcalc = TDDFT(name + '_gs.gpw', 
			   txt = name + '_td_gaussian.txt', 
			   propagator = "EFSICN", 
			   solver = "BiCGStab", 
			   td_potential = CWField(0.0169, 0.057, 827, 2894))

# New object for velocity verlet
ehrenfest = EhrenfestVelocityVerlet(tdcalc)


# Another object to save the dynamics
traj = Trajectory(name + '_td_linear.traj', 'w', tdcalc.get_atoms())

for i in range(1, niter + 1):
	ehrenfest.propagate(timestep)


	# Every ndiv timesteps, save the trajectory
	if i % ndiv == 0:
		# energy, forces, velocities to save.
		print(i)
		epot = tdcalc.get_td_energy() * Hartree
		F_av = ehrenfest.F * Hartree / Bohr
		v_av = ehrenfest.v * Bohr / AUT
		atoms = tdcalc.atoms.copy()
		atoms.set_velocities(v_av)
		traj.write(atoms, energy = epot, forces = F_av)

traj.close()