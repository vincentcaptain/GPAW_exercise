from ase import Atoms
from gpaw.fdtd.poisson_fdtd import QSFDTD
from gpaw.fdtd.polarizable_material import (PermittivityPlus, 
											PolarizableMaterial,
											PolarizableAtomisticRegion)
from gpaw.tddft import photoabsorption_spectrum
import numpy as np
from ase.io import read
from gpaw.tddft import photoabsorption_spectrum

# Read atom objects
atoms = read("water_8.xyz", format = 'xyz')

# Permittivity of water 
eps_water = PermittivityPlus(data = 2)

# 1. optical spectrum of 1 H2O to benchmark
