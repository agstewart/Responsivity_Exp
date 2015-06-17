

import sys
from newport import NewportPowerMeter
import numpy as np
import matplotlib.pyplot as plt
import wx
from ExpGUI import ExpGUI
from newport import NewportPowerMeter
	
class Experiment():
		
		def __init__ (self,address,title):
		
			self.newportAddress = address 	
			self.title = title
		
			# create ExpGUI object
			self.t = ExpGUI(self.title)
			
			# create Newport object
			self.optMeter = NewportPowerMeter(self.newportAddress)
			
			self.t.panel.Bind(wx.EVT_BUTTON, self.on_draw_button, self.t.button)

			min_wavelen = self.t.wavelenMin.GetValue()

			self.wavelengths = np.linspace(float(min_wavelen), 1000, 6)
			self.power = np.zeros(len(self.wavelengths))
			
		def getReading(self):
			
			r = self.optMeter.getPower().replace('\x00','').replace('\n','')
			return r
			
		def setWavelength(self, wlen):
			self.wlen =wlen
			self.optMeter.setWavelen(self.wlen)

		def on_draw_button(self, event):
			for i in np.arange(len(self.wavelengths)):
			
				# clear instr
				# self.optMeter.clearInst()
				# set wavelength
				self.setWavelength( self.wavelengths[i] )
				
				# get power reading
				reading = self.getReading()
				# print float ( reading )
				self.power[i] = float( reading )
				self.t.updateStaticText(reading)
				
			self.result = np.column_stack(( np.reshape(self.wavelengths,(len(self.wavelengths), 1)), self.power ))
			self.t.draw_figure(self.result)
		
				

if __name__ == '__main__':

	app = wx.App(redirect=True)
	
	# power = optMeter.getPower().replace('\x00','').replace('\n','')
	
	# t.updateStaticText(power)
	
	exp = Experiment(15, 'Responsivity')
	app.MainLoop()