
import serial

class NewportPowerMeter(object):
	""" A class for the Nwerport 1830-R Optical Power Meter"""
	def __init__ (self, address):
		self.addr = address
		self.ser = serial.Serial( 'COM6', 9600, timeout=0.5 )
		# set mode as controller
		cmd = '++mode 1'
		self.ser.write(cmd + '\n')
		# turn off read-after-write
		cmd = '++auto 0'
		self.ser.write(cmd + '\n')
		# don't append CR or LF to GPIB data
		cmd = '++eos 3'
		self.ser.write(cmd + '\n')
		#  set newport address
		cmd = '+addr' + str(self.addr)
		self.ser.write(cmd + '\n')

	def getReading(self):
		self.ser.write('++read eoi' + '\n')
		s = self.ser.read(256)
		return s
		
	def idn(self):
		#self.ser = serial.Serial( 'COM6', 9600, timeout=0.5 )
		cmd = '*IDN?'
		self.ser.write(cmd + '\n')
		return self.getReading()
		
	def getAddr(self):
		return self.addr

	def setWavelen(self, wlen):
		self.wlen = wlen
		if self.wlen < 200:
			print 'Error: Wavelenth below 200nm!'
		elif self.wlen > 1100:
			print 'Error: Wavelength above 1100nm!'
		else:
			cmd = 'W' + str(self.wlen)
			self.ser.write(cmd + '\n')

	def getWavelen(self):
		cmd = 'W?'
		self.ser.write(cmd + '\n')
		return self.getReading()

	def getPower(self):
		cmd = 'D?'
		self.ser.write(cmd + '\n')
		return self.getReading()

	def setAttenuator(self, v):
		self.v = v
		if self.v == 1:
			cmd = 'A1'
		elif self.v == 0:
			cmd = 'A0'
		else: 
			print  'error'
		self.ser.write(cmd + '\n')

	def clearInst(self):
		cmd = 'C'
		self.ser.write(cmd + '\n')

	def getFilter(self):
		cmd = 'F?'
		self.ser.write(cmd + '\n')
		return self.getReading()

	def setFilter(self, f):
		self.f = f
		if f == 1:
			cmd = 'F1' #Slow
		elif f == 2:
			cmd = 'F2' #Medium
		elif f == 3:
			cmd = 'F3' # Fast
		else:
			print error
		self.ser.write(cmd + '\n')

	def getRange(self):
		cmd = 'R?'
		self.ser.write(cmd + '\n')
		return self.getReading()

	def getUnits(self):
		cmd = 'U?'
		self.ser.write(cmd + '\n')
		return self.getReading()

	def setUnits(self, units):
		self.units = units
		if self.units == 1:
			cmd = 'U1' # Watts
		elif self.units == 2:
			cmd = 'U2' # dB
		elif self.units == 3:
			cmd = 'U3' # dBm
		elif self.units == 4:
			cmd = 'U4' # Relative
		else:
			print error
		self.ser.write(cmd + '\n')

	def getZero(self):
		cmd = 'Z?'
		self.ser.write(cmd + '\n')
		return self.getReading()

	def setZero(self, z):
		self.z = z
		if z == 0:
			cmd = 'Z0'
		elif z == 1:
			cmd = 'Z1'
		else:
			print error
		self.ser.write(cmd + '\n')
