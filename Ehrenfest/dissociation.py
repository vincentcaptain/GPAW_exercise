from gpaw.tddft import TDDFT
from gpaw.tddft.ehrenfest import EhrenfestVelocityVerlet
from gpaw.tddft.laser import CWField
from ase.units import Hartree, Bohr, AUT
from ase.io import Trajectory
from ase.parallel import parprint

name = 'h2_diss'

# Ehrenfest simulation parameters
timestep = 10.0 				# 10 attoseconds
ndiv = 10						# dump traj every 10 timesteps
niter = 500						# up to 500 timesteps = 5 fs.

# TDDFT calculator with external potential from intense harmonic laser field aligned
tdcalc = TDDFT(name + '_gs.gpw', 
			   txt = name + '_td.txt', 
			   propagator = "EFSICN", 
			   solver = "BiCGStab", 
			   td_potential = CWField(1000 * Hartree, 1 * AUT, 10))

# New object for velocity verlet 
ehrenfest = EhrenfestVelocityVerlet(tdcalc)

# Another object to save the dynamics
traj = Trajectory(name + '_td.traj', 'w', tdcalc.get_atoms())

# Iterate over n timesteps

for i in range(1, niter + 1):
	ehrenfest.propagate(timestep)

	if tdcalc.atoms.get_distance(0, 1) > 2.0:
		parprint("Dissociated!")
		break

	# Every ndiv timesteps, save the trajectory
	if i % ndiv == 0:
		# energy, forces, velocities to save.
		epot = tdcalc.get_td_energy() * Hartree
		F_av = ehrenfest.F * Hartree / Bohr
		v_av = ehrenfest.v * Bohr / AUT
		atoms = tdcalc.atoms.copy()
		atoms.set_velocities(v_av)
		traj.write(atoms, energy = epot, forces = F_av)

traj.close()