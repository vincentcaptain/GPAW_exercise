from gpaw.tddft import *

time_step = 8.0                  # 1 attoseconds = 0.041341 autime
iterations = 2500                # 2500 x 8 as => 20 fs

# Read restart file with result of previous propagation
td_calc = TDDFT('be_td.gpw')

# Propagate more, appending the time-dependent dipole moment to the
# already existing 'be_dm.dat' and use 'be_td2.gpw' as restart file
td_calc.propagate(time_step, iterations, 'be_dm.dat', 'be_td2.gpw')

# Recalculate photoabsorption spectrum and write it to 'be_spectrum_z2.dat'
photoabsorption_spectrum('be_dm.dat', 'be_spectrum_z2.dat')