
import wx
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
	FigureCanvasWxAgg as FigCanvas, \
	NavigationToolbar2WxAgg as NavigationToolbar
from newport import NewportPowerMeter
	
class ExpGUI(wx.Frame):
	""" class to create GUI for Responsivity Experiment """
	def __init__(self, title):
	
		self.data = [5, 6, 9, 14]
		
		self.title = title
		self.createFrame()
		self.createPanel()
		self.show()
		# self.draw_figure()
		
	def createFrame(self):
		# create Frame
		self.frame = wx.Frame(None, title = self.title, size= (700, 600))
		
	def createPanel(self):
		# create Panel
		self.panel = wx.Panel(self.frame)
		
		#create button
		self.createButton('Run')
		
		# create the mpl Figure and FigCanvas objects
		# 5 x 4 inches, 100 dots-per-inch
		self.dpi = 100
		self.fig = Figure((6.0, 5.0), dpi=self.dpi)
		self.canvas = FigCanvas(self.panel, -1, self.fig)
		self.axes = self.fig.add_subplot(111)
		
		# create static text
		# self.createStaticText('Power: ')
		# create power measurement text
		self.measurement = self.createStaticText('Power: ')
		self.measurementFont = self.setFont(20)
		self.measurement.SetFont(self.measurementFont)
		
		# create the navigation toolbar, tied to the canvas
		self.toolbar = NavigationToolbar(self.canvas)

		# create 'min wavelength' text 
		self.min = self.createStaticText('Min Wavelength: ')
		self.minFont = self.setFont(14)
		self.min.SetFont(self.minFont)
		self.wavelenMin = self.createTextCtrl('300')

		# create 'max wavelength' text
		self.max = self.createStaticText('Maximum Wavelength: ')
		self.max.SetFont(self.minFont)
		self.wavelenMax = self.createTextCtrl('1000')
		
		# Layout with box sizers
		
		self.vbox = wx.BoxSizer(wx.VERTICAL)
		self.vbox.Add(self.canvas, 1, wx.LEFT | wx.ALL | wx.GROW)
		self.vbox.AddSpacer(10)
		
		self.hbox = wx.BoxSizer(wx.HORIZONTAL)
		flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
		self.hbox.Add(self.button, 0, border=3, flag=flags)
		
		self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		# flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
		self.hbox2.Add(self.measurement, 0, border=3, flag=flags)

		self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.hbox3.Add(self.min, 0, border=3, flag=flags)
		self.hbox3.Add(self.wavelenMin, 0, border=3, flag=flags)
		self.hbox3.Add(self.max, 0, border=3, flag=flags)
		self.hbox3.Add(self.wavelenMax, 0, border=3, flag=flags)
		
		self.vbox.Add(self.hbox3, 0, flag = wx.ALIGN_LEFT | wx.TOP)
		
		self.vbox.Add(self.hbox2, 0, flag = wx.ALIGN_LEFT | wx.TOP)
		
		self.vbox.Add(self.hbox, 0, flag = wx.ALIGN_LEFT | wx.TOP)
		
		self.panel.SetSizer(self.vbox)
		# self.vbox.Fit(self)

	def createTextCtrl(self, val):
		dft_val = val
		#txtlabel = label
		#wx.StaticText(self.panel, label = txtlabel, style = wx.ALIGN_LEFT)
		# font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
		# self.min.SetFont(font)
		return wx.TextCtrl(self.panel, -1, dft_val)
				
	def createButton(self, name):
		# create button
		self.buttonName = name
		self.button = wx.Button(self.panel, label = self.buttonName)
		#self.panel.Bind(wx.EVT_BUTTON, self.on_draw_button, self.button)

	def setFont(self, fontsize):
		self.fontsize = fontsize
		return  wx.Font(self.fontsize, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
		
	def createStaticText(self, label):
		label = label
		# create static text
		return wx.StaticText(self.panel, label = label, style = wx.ALIGN_LEFT)
		#
		# self.measurement.SetFont(font)
		
	def updateStaticText(self, result):
		self.result = result
		self.measurement.SetLabel('Power: ' + result)
		
	def on_draw_button(self, event):
		event.Skip()
		# self.updateStaticText('22')
		#self.draw_figure()
		
	def draw_figure(self, data):
	
		self.data = data
	
		# clear  the axes amd redraw the plot
		self.axes.clear()
		self.axes.plot(self.data[:,0], self.data[:,1]/1E-9)
		# self.ylabel('Power (nW)')
		# self.fig.xlabel('Wavelength (nm)')
		self.canvas.draw()

	def show(self):
		self.frame.Centre()
		self.frame.Show()
