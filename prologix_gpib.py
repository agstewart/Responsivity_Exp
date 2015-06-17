
import os.path
import serial
import sys

if __name__ == '__main__':

	if len(sys.argv) != 3:
		print "Usage: ", os.path.basename( sys.argv[0] ), "<COM port> <GPIB address>"
		sys.exit(1)
		
	comport = sys.argv[1]
	addr = sys.argv[2]
	
	ser = serial.Serial()
	
	try:
	
		success = True
		
		# open serial port
		ser = serial.Serial( comport, 9600, timeout=0.5 )
		
		# set mode as controller
		cmd = '++mode 1'
		print 'Sending:', cmd
		ser.write(cmd + '\n')
		s = ser.read(256)
		
		#  set newport address
		cmd = '+addr' +addr
		print 'Sending:', cmd
		ser.write(cmd + '\n')
		
		# turn off read-after-write
		cmd = '++auto 0'
		print 'Sending:', cmd
		ser.write(cmd + '\n')
		
		# don't append CR of LF to GPIB data
		cmd = '++eos 3'
		print 'Sending:', cmd
		ser.write(cmd + '\n')
		
		cmd = '*IDN?'
		print 'Sending:', cmd
		ser.write(cmd  + '\n')
		
		cmd = '++read eoi'
		print 'Sending:', cmd
		ser.write(cmd + '\n')
		
		s = ser.read(256)
		print s
		
	except serial.SerialException, e:
		print e