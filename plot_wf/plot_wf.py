from ase.io import write
from gpaw import restart

basename = "CO"

# load binary to get calculator
atoms, calc = restart(basename + ".gpw")

# loop over all wfs and write corresponding cube files

nbands = calc.get_number_of_bands()
for band in range(nbands):
	wf = calc.get_pseudo_wave_function(band = band)
	fname = "{0}_{1}.cube".format(basename, band)
	print("writing wf", band, "to file", fname)
	write(fname, atoms, data = wf)

