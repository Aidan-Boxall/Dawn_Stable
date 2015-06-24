import Crystal as c
import numpy as np

import functions as r


LENGTH = 0.502 # The length between the sample and the detector.
WIDTH = 195*172*10**-6  # Width of the detector 195 pixels times 172 microns
ENERGY = 8  # photon energy in keV

# Loads the crystal data
MYCRYS = c.Crystal()
MYCRYS.load_cif('NiCO3_icsd_61067.cif')

# Produces delta_chi for each reflection
MYLIST = MYCRYS.reflection_list(ENERGY, print_list=False)
two_thetas = []

for lists in MYLIST:
    two_thetas.append(lists[4])

thetas = [two_theta / 2.0 * (np.pi / 180) for two_theta in two_thetas]

radii = [LENGTH * np.sin(theta) for theta in thetas]

delta_chis = [WIDTH / radius for radius in radii]
for i, theta in enumerate(two_thetas):
    print i + 1, theta, delta_chis[i] * (180 / np.pi)
