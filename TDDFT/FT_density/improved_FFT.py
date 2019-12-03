from gpaw.tddft import TDDFT
from gpaw.tddft.fourier import DensityFourierTransform

time_step = 4.0                  # 1 attoseconds = 0.041341 autime
iterations = 5000                # 5000 x 4 as => 20 fs
frequencies = [4.26,6.27,13.0, \
               16.9,18.1,19.9]   # Pre-determined peak frequencies in eV
sigma = 0.05                     # Width of Gaussian envelope in

# Read restart file with result of previous propagation
td_calc = TDDFT('bda_td.gpw')

# Create and attach Fourier transform observer
obs = DensityFourierTransform(timestep, frequencies, sigma)
obs.initialize(td_calc)

# Read previous result of the corresponding Fourier transformations
obs.read('bda_fourier.ftd')

# Propagate more, appending the time-dependent dipole moment to the
# already existing 'bda_dm.dat' and use 'bda_td2.gpw' as restart file
td_calc.propagate(time_step, iterations, 'bda_dm.dat', 'bda_td2.gpw')

# Save result of the improved Fourier transformations to an .ftd file
obs.write('bda_fourier2.ftd')