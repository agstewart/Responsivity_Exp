

import sys
from newport import NewportPowerMeter
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

	opt_meter = NewportPowerMeter(15)
	
	opt_meter.setFilter(3)
	
	wavelengths = np.linspace(200, 1000, 6)
	
	power = np.zeros(len(wavelengths)) # generate a python list
	
	for i in np.arange(len(wavelengths)):
		opt_meter.setWavelen(wavelengths[i])
		wavelen = opt_meter.getWavelen()
		# repr( opt_meter.getPower().replace('\x00','').replace('\n','')  )
		power[i] = float(opt_meter.getPower().replace('\x00','').replace('\n', ''))
		print power[i]
		
	
	fig=plt.figure()
	rect = fig.patch
	rect.set_facecolor('w')
	ax = fig.add_subplot(111)
	plt.plot(wavelengths, power/1E-9, 'o-g')
	plt.ylabel('Optical Power (nW)')
	plt.show()
	