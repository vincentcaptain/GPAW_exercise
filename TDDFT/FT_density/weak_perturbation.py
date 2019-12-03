from gpaw.tddft import TDDFT
from gpaw.tddft.fourier import DensityFourierTransform

time_step = 4.0						# 1 as = 0.041341 au time
iterations = 5000					# 20 fs pulse
kick_strength = [0.0, 5e-3, 0.0]	# y-direction perturbation
frequencies = [4.26,6.27,13.0, \
               16.9,18.1,19.9]   	# Pre-determined peak frequencies in eV
sigma = 0.05                     	# Width of Gaussian envelope in eV

# Read gs
td_calc = TDDFT("be_gs.gpw")

# Kick with a delta pulse to y-direction
td_calc.absorption_kick(kick_strength=kick_strength)

# Create and attach Fourier transform observer
obs = DensityFourierTransform(timestep, frequencies, sigma)
obs.initialize(td_calc)

# Propagate, save the time-dependent dipole moment to 'bda_dm.dat',
# (just for comparison) and use 'bda_td.gpw' as restart file
td_calc.propagate(time_step, iterations, 'bda_dm.dat', 'bda_td.gpw')

# Save result of the Fourier transformations to a .ftd file
obs.write('bda_fourier.ftd')