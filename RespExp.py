
import sys
import numpy as np
import matplotlib.pyplot as plt
import wx

app = wx.App()

# create frame
frame= wx.Frame(None, -1, 'QE Measurement', size = (400,400))
frame.Show()
frame.Centre()

# create panel
pnl = wx.Panel()

# create buttom
btm = wx.Button(pnl, label = 'Run', pos=(20, 30))

app.MainLoop()