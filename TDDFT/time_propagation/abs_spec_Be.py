from gpaw.tddft import *

time_step = 8.0                  # 1 attoseconds = 0.041341 autime
iterations = 2500                # 2500 x 8 as => 20 fs
kick_strength = [0.0,0.0,1e-3]   # Kick to z-direction

# Read ground state
td_calc = TDDFT('be_gs.gpw')

# Kick with a delta pulse to z-direction
td_calc.absorption_kick(kick_strength=kick_strength)

# Propagate, save the time-dependent dipole moment to 'be_dm.dat',
# and use 'be_td.gpw' as restart file
td_calc.propagate(time_step, iterations, 'be_dm.dat', 'be_td.gpw')

# Calculate photoabsorption spectrum and write it to 'be_spectrum_z.dat'
photoabsorption_spectrum('be_dm.dat', 'be_spectrum_z.dat')