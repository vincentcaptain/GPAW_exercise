from ase import Atoms
from gpaw.fdtd.poisson_fdtd import QSFDTD
from gpaw.fdtd.polarizable_material import (PermittivityPlus, 
											PolarizableMaterial,
											PolarizableAtomisticRegion)
from gpaw.tddft import photoabsorption_spectrum
import numpy as np
from ase.io import read

# Permittivity of water 
eps_water = PermittivityPlus(data = 2)

# Geometry
atom_center = np.array([15, 15, 15])
simulation_cell = np.array(50, 50, 50)

# 1. optical spectrum of 1 H2O to benchmark
# GS calculation
from ase.build import molecule
from gpaw import GPAW
H2O_1 = Atoms("H2O", atom_center + np.array([-1.62952, 0.502285, 3.96505],
											[2.42786, 0.724159, 4.37206],
											[-1.81684, 0.317217, 3.01169]))

calc_H2O_1 = GPAW(nbands = 1, h = 0.25)
H2O_1.set_calculator(calc_H2O_1)

energy = atoms.get_potential_energy()
calc_H2O_1.write("H2O_1_gs.gpw", 'all')
# Optical spectrum GS:
time_step = 8.0
iterations = 2500
# Optical spectrum TDDFT:
time_step = 8.0
iterations = 2500
calc_H2O_1_td tdcalc = TDDFT('H2O_1_gs.gpw', 
			   txt = 'H2O_1_td.txt', 
			   propagator = "EFSICN", 
			   solver = "BiCGStab", 
			   td_potential = CWField(0.0169, 0.057, 0, 50000))
calc_H2O_1_td.propagate(time_step, iterations, 'H2O_1_dm.dat', 'H2O_1.gpw')
photoabsorption_spectrum('H2O_1_dm.dat', 'H2O_1_spectrum.dat', width = 0.15)

# 2. optical spectrum of 1 H2O + environment
H2O_1 = Atoms("H2O", atom_center + np.array([-1.62952, 0.502285, 3.96505],
											[2.42786, 0.724159, 4.37206],
											[-1.81684, 0.317217, 3.01169]))
classical = PolarizableMaterial()
classical.add_component(PolarizableAtomisticRegion(atoms = H2O_1, 
												   distance = 2.3, 
												   permittivity = eps_water))
qsfdtd = QSFDTD(classical_material = classical, 
				atoms = H2O_1,
				cells = (simulation_cell, 2.3), #vacuum = 2.3 surrounding 
				spacings = (1, 0.25)) 
energy = qsfdtd.ground_state("H2O_1_HQC.gpw", nbands = -1)
qsfdtd.time_propagation("H2O_1_HQC.gpw", 
						txt = "H2O_1_HQC.txt"
						time_step = 8, 
						iterations = 2500, 
						ndiv = 50,
						propagator = "EFSICN",
						solver = "BiCGStab",
						td_potential = CWField(0.0169, 0.057, 0, 50000),
						dipole_moment_file = "H2O_1_HQC_dm.dat")
photoabsorption_spectrum("H2O_1_HQC_dm.dat", "H2O_1_HQC_spectrum.dat", width = 0.15)



