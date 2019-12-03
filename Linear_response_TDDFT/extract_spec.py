from gpaw.lrtddft import LrTDDFT, photoabsorption_spectrum
from gpaw.lrtddft.convergence import check_convergence

lr = LrTDDFT('lr.dat.gz')
lr.diagonalize()

photoabsorption_spectrum(lr, 'spectrum_w.05eV.dat', 
							width = 0.05)

# testing convergence of the KS transition basis size by
# restricting the basis in the diagonalization step

lr = LrTDDFT('lr.dat.gz')
check_convergence(lr, 
				  'linear_response', 
				  'convergence', 
				  dE = .2, 
				  emax = 6.)
lr.diagonalize(energy_range = 2.)

# Analyzing the single transitions:

lr = LrTDDFT('lr.dat.gz')
lr.diagonalize()

# Analyze transition 1
lr.analyse(1)
# Analyze transition 0-10
lr.analyse(range(11))

