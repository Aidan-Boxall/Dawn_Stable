# import numpy as np
# import scisoftpy as dnp
# import scitbx.math as scm
# from scitbx.matrix import col as Vector
# from scitbx.matrix import sqr as Rotator
import pickle

# from fluffy_latest import get_q
from fixnexus import fix_scan_file
import peak_finder as fp

data_dir='/dls/i16/data/2015/cm12169-3/'
cif = 'HoFe2_icsd_103499.cif'
peaks = fp.find_peaks('/dls/i16/data/2015/cm12169-3/', 521280, 521311, 6,
                          True, False, 'roi7_sum')#('/dls/i16/data/2015/cm12169-3/', 527359, 527369, 8, False, False, 'roi7_sum')


for peak in peaks:
    scan_number = peak[0][29:35]
    fix_scan_file(data_dir, scan_number)
    file_name = data_dir + scan_number + '_c.nxs'

with open("peaks.pkl", 'wb') as peaksfile:
    pickle.dump(peaks, peaksfile)

print "Done fixing nexus files."



#     q = get_q(file_name ,(0,0))
#     print q
#     print


#     kappa = dat.metadata['kap']
#     ktheta = dat.metadata['kth']
#     kphi = dat.kphi[image_number-1]
#     print kappa
#     print ktheta
#     print kphi
# #     coords = (peak[1],peak[2])
# #     image_centre = (108, 242)
# #     pix_vector = Vector((peak[2] - image_centre[0], peak[1] - image_centre[1]))
# #     pix_vector*=172*10**-6 # in meters
# #     pix_vector = Vector([-pix_vector[1]*np.sin(np.radians(delta + detector_angle)), pix_vector[0], pix_vector[1]*np.cos(np.radians(delta + detector_angle))])
#     beam_out = Vector((np.cos(np.radians(delta)), 0.0, np.sin(np.radians(delta))))*LENGTH # Wave out in meters
# # #     beam_out += pix_vector # In meters
#     beam_out = beam_out.normalize()
#     beam_out = beam_out*wave_vector
# # #     print 'beam', beam_out
#     beam_in = x_axis*wave_vector
# #     print np.degrees(np.arccos(beam_out.normalize().dot(beam_in.normalize())))
#     mom_trans = beam_out - beam_in
#     dot = mom_trans.normalize().dot(z_axis)
#     print beam_in
#     print 'ang', np.rad2deg(np.arccos(dot))
#     print 'mom'
#     print mom_trans.length()
#     print mom_trans
#     print
# 
# #     fig = plt.figure()
# #     ax = fig.add_subplot(111, projection='3d')
# #     f.plot_vectors_as_arrows([beam_in],fig,ax, color = 'red')
# #     f.plot_vectors_as_arrows([beam_out],fig,ax, color = 'blue')
# #     f.plot_vectors_as_arrows([mom_trans],fig,ax, color = 'green')
# #     plt.show()
# 
#     eta_rot =  Rotator(scm.r3_rotation_axis_and_angle_as_matrix(y_axis, eta, deg = True))#+ve eta as left handed rotations
#     mom_trans = eta_rot*mom_trans
#     print 'eta rot',eta
#     print mom_trans
#     print 
# 
# 
# #     fig = plt.figure()
# #     ax = fig.add_subplot(111, projection='3d')
# #     f.plot_vectors_as_arrows([beam_in],fig,ax, color = 'red')
# #     f.plot_vectors_as_arrows([beam_out],fig,ax, color = 'blue')
# #     f.plot_vectors_as_arrows([mom_trans],fig,ax, color = 'green')
# #     plt.show()
# 
#     chi_rot = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(x_axis, -chi, deg = True))
#     mom_trans = chi_rot*mom_trans
# #     print 'chi rot',chi
# #     print mom_trans
# #     print
# #     print 'phi offset', dat.metadata.kphi-dat.metadata.phi
#     phi_rot = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(y_axis, phi, deg = True))#+ve phi as left handed rotations
#     mom_trans = phi_rot*mom_trans
# #     print 'phi rot',phi
# #     print mom_trans
# #     print 
# #     print delta/2
# #     print eta
#     print chi
# #     print phi
# #     print
#     data.append(mom_trans)