#from __future__ import division 
import numpy as np
#import scipy
import math
import matplotlib.pyplot as plt
#import sys
#import matplotlib 
#from scipy.stats import multivariate_normal
#from scipy import integrate
#from mpl_toolkits.mplot3d import Axes3D 
#from scipy.integrate import quad
#from mpl_toolkits.basemap import Basemap
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import fits
from astropy.stats import LombScargle
from astropy.modeling import models, fitting

hdulist = fits.open('kplr005780885-2009166043257_llc.fits')
print hdulist.info()

# for i in hdulist[1].header:
# 	print i, hdulist[1].header[i], hdulist[1].header.comments[i]

scidata = hdulist[1].data

#scidata[0]
time_temp= scidata.field(0)
output_temp = scidata.field(3)

time = []
output = []
for i in range(len(time_temp)):
	if not math.isnan(output_temp[i]):
		time.append(time_temp[i])
		output.append(output_temp[i])



#print list(time)
polynoom = np.polyfit(time, output, 5)
f = np.poly1d(polynoom)

xx = np.linspace(time[0],time[-1],len(time))
print xx	
yy = f(xx)

yy=np.array(yy)
output= np.array(output)

output_substracted = output-yy 
#print np.mean(output_substracted)
output_substracted = output_substracted - np.mean(output_substracted)
np.savetxt('fitsdata.txt', np.c_[time,output])

#frequency, power = LombScargle(time, output).autopower()

plt.plot(time,output)
plt.plot(xx,yy)
plt.show()

plt.plot(time,output_substracted)
plt.show()



# t_init = models.Trapezoid1D(amplitude=1., x_0=0., width=1., slope=0.5)
# fit_t = fitting.LevMarLSQFitter()
# t = fit_t(t_init, x, y)





#rand = np.random.RandomState(42)
#t = 100 * rand.rand(100)
#y = np.sin(2 * np.pi * t) + 0.1 * rand.randn(100)

#frequency2, power2 = LombScargle(time, output).autopower()
# plt.plot(frequency2,power2)
# plt.plot(t,y,'bo')
# plt.show()


hdulist.close()


# data = np.genfromtxt('planets.csv', delimiter=',', names=True,skip_header=32,dtype=None) #32 lines of headers
# rowupdate = data['rowupdate']
# pl_hostname = data['pl_hostname']
# pl_letter = data['pl_letter']

# #print rowupdate[1:30]
# print rowupdate
# print np.sort(rowupdate)
# sort_index = np.argsort(rowupdate)
# print sort_index[0]

# print pl_hostname[0]
# print pl_letter[0]

#print np.argmin(rowupdate)

