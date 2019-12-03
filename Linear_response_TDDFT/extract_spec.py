from gpaw.lrtddft import LrTDDFT, photoabsorption_spectrum
from gpaw.lrtddft.convergence import check_convergence

lr = LrTDDFT('lr.dat.gz')
lr.diagonalize()

photoabsorption_spectrum(lr, 'spectrum_w.05eV.dat', 
							width = 0.05)

# Analyze transition 1
lr.analyse(1)
# Analyze transition 0-10
lr.analyse(range(11))

