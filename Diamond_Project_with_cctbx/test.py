import matplotlib.pyplot as plt
import functions as f
hkl_list = [(0, 1, 5), (-2, 2, 0), (-2, 0, 0)]
f.plot_by_hkl('Hexagonal.cif', hkl_list, refl='allowed')
plt.show()
