import scisoftpy as dnp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dat = dnp.io.load('/dls/i16/data/2015/cm12169-3/518477.dat', warn=False)
dat2 = dnp.io.load('/dls/i16/data/2015/cm12169-3/518478.dat', warn=False)
cmd = dat.metadata.cmd
cmd2 = dat2.metadata.cmd  # Scans kphi in 2 alternating directions therefore
#                            different commands.
chi = None
kphi = None
sums = None
path_index = 518477
while dat.metadata.cmd == cmd or dat.metadata.cmd == cmd2:
    if chi is None:
        chi = np.array([dat.metadata.chi]*len(dat.kphi))
    else:
        chi = np.append(chi, np.array([dat.metadata.chi]*len(dat.kphi)))
    if kphi is None:
        kphi = np.array(dat.kphi)
    else:
        kphi = np.append(kphi, dat.kphi)
    if sums is None:
        sums = np.array(dat.sum)
    else:
        sums = np.append(sums, dat.sum)
    try:
        dat = dnp.io.load('/dls/i16/data/2015/cm12169-3/{0:.0f}.dat'.format(
            path_index), warn=False)
    except ValueError:
        break
    path_index += 1
    print path_index, dat.metadata.cmd
print 'done'
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(chi,kphi,sums)
ax.set_xlabel('Chi Angle')
ax.set_ylabel('Kphi Angle')
ax.set_zlabel('Total Sum')
plt.show()
fig.savefig('/home/ljh75651/DAWN_stable/fig.png')
# dh = dnp.io.load('/dls/i16/data/2015/cm12169-3/518477.nxs')
# print dat.keys()
# dnp.plot.plot(dat.kphi,dat.sum)
# print max(dat.sum)
# print list(dat.sum).index(max(dat.sum))
# image_data = dh[0].instrument.pil100k.image_data
# im = dnp.io.load('/dls/i16/data/2015/cm12169-3/518477-pilatus100k-files/00000_01584.tif', warn=False)
# im2 = dnp.io.load('/dls/i16/data/2015/cm12169-3/518477-pilatus100k-files/00000_01583.tif', warn=False)
# print im[0].size
# intergrals = dnp.array([dnp.zeros((195))])
# #dnp.io.load('/dls/i16/data/2015/cm12169-3/'+image_data[0][0][:25]+'0000_'+image_data[0][0][25:])
# dnp.plot.clear()
# for i in range(image_data.shape[0]-1):
#     print i
#     im = dnp.io.load('/dls/i16/data/2015/cm12169-3/518477-pilatus100k-files/00000_'+image_data[i][0][25:],warn=False)
# #    dnp.plot.image(im[0])
#     im_des= im[1].image_description
#     im_des = im_des.split()
#     intergral = dnp.array([[]])
#     for x in range(im[0].shape[0]):
#         intergral = dnp.append(intergral, sum(im[0][x]))
#     intergral = dnp.array([intergral])
#     intergrals = dnp.append(intergrals, intergral, axis=0)
#     dnp.plot.addpoints(dnp.array([float(im_des[im_des.index('Chi')+1])]), dnp.array([sum(intergral[0])]))
#  
# intergrals = intergrals[1:]
# # l = []
# # for i , item in enumerate(intergrals):
# #     dnp.plot.addline(item)