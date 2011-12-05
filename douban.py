#!/usr/bin/python
#-*- coding: utf-8 -*-
import wx
import os
import wx.lib.buttons as buttons
from lib import main
from lib import *

class StaticTextFrame(wx.Frame):
		
		def __init__(self):
			#将窗口放置屏幕中央
				wx.Frame.__init__(self,None,-1,'豆瓣',size=(800,600),pos=(wx.DisplaySize()[0]/2-400,wx.DisplaySize()[1]/2-300))
				self.panel  = wx.Panel(self,-1)
				#设置背景颜色 （默认为灰色）
				self.panel.SetBackgroundColour('White')
				#创建状态栏
				statusBar = self.CreateStatusBar()
				
				wildcard = "mp3 source (*.mp3)|*.mp3|" \
					"All files (*.*)|*.*"
				self.dialog1 = wx.DirDialog(None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
				self.dialog2 = wx.FileDialog(None, "Choose a file:",os.getcwd()," ",wildcard,wx.OPEN)
				
				self.floderLabel  = wx.StaticText(self.panel,-1,"选择目录",pos=(0,40))
				self.floderText = wx.TextCtrl(self.panel,-1,pos=(0,70),size=(250,-1))
				self.button1 = buttons.GenButton(self.panel,-1,"浏览",pos=(260,65))
				self.Bind(wx.EVT_BUTTON,self.OpenFloder,self.button1)
				self.filLabel = wx.StaticText(self.panel,-1,"选择文件",pos=(0,100))
				self.fileText = wx.TextCtrl(self.panel,-1,pos=(0,130),size=(250,-1))
				self.button2 = buttons.GenButton(self.panel,-1,"浏览",pos=(260,125))
				self.Bind(wx.EVT_BUTTON,self.OpenFile,self.button2)
				self.button3= buttons.GenButton(self.panel,-1,"启动",pos=(0,160))
				self.Bind(wx.EVT_BUTTON,self.StartUp,self.button3)
				sizer = wx.FlexGridSizer(1, 3, 0, 0)
				self.panel.SetSizer(sizer)
					
		def OpenFloder(self,event):
					if self.dialog1.ShowModal() == wx.ID_OK:
							self.floderText.WriteText(self.dialog1.GetPath())
		#			self.dialog1.Destroy()
					
		def OpenFile(self,event):
					if self.dialog2.ShowModal() == wx.ID_OK:
							self.fileText.WriteText(self.dialog2.GetPath())
	#				self.dialog2.Destroy()
					
		def StartUp(self,event):
					#print self.dialog1.GetPath()
					main.main(self.dialog1.GetPath())

app = wx.PySimpleApp()
frame = StaticTextFrame()
frame.Show()
app.MainLoop()
