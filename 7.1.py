#!/usr/bin/python
#-*- coding: utf-8 -*-
import wx
import os
import wx.lib.buttons as buttons
import example

class StaticTextFrame(wx.Frame):
		def __init__(self):
			#将窗口放置屏幕中央
				wx.Frame.__init__(self,None,-1,'豆瓣',size=(800,600),pos=(wx.DisplaySize()[0]/2-400,wx.DisplaySize()[1]/2-300))
				self.panel  = wx.Panel(self,-1)
				#设置背景颜色 （默认为灰色）
				self.panel.SetBackgroundColour('White')
				#创建状态栏
				statusBar = self.CreateStatusBar()
				sizer = wx.FlexGridSizer(1, 3, 0, 0)
				self.button1 = buttons.GenButton(self.panel, -1, "同步")#通用开关按钮
				sizer.Add(self.button1)
				self.button2 = buttons.GenButton(self.panel, -1, "下载")#通用开关按钮
				sizer.Add(self.button2)
				self.Bind(wx.EVT_BUTTON,self.ClickButtonOne,self.button1)
				self.Bind(wx.EVT_BUTTON,self.ClickButtonTwo,self.button2)
				self.panel.SetSizer(sizer)
				
		def ClickButtonOne(self,event):
					panel = wx.Panel(self,-1,pos=(0,30),size=(800,600))
					self.floderLabel  = wx.StaticText(panel,-1,"选择目录",pos=(0,40))
					self.floderText = wx.TextCtrl(panel,-1,pos=(0,70),size=(250,-1))
					self.button3 = buttons.GenButton(panel,-1,"浏览",pos=(260,65))
					self.Bind(wx.EVT_BUTTON,self.OpenFloder,self.button3)
					#self.floderText.SetInsertionPoint(0)
					
					self.filLabel = wx.StaticText(panel,-1,"选择文件",pos=(0,100))
					self.fileText = wx.TextCtrl(panel,-1,pos=(0,130),size=(250,-1))
					self.button4 = buttons.GenButton(panel,-1,"浏览",pos=(260,125))
					self.Bind(wx.EVT_BUTTON,self.OpenFile,self.button4)					
					
					self.button5 = buttons.GenButton(panel,-1,"启动",pos=(0,160))
					self.Bind(wx.EVT_BUTTON,self.StartUp,self.button5)
						
		def ClickButtonTwo(self,event):
					panel = wx.Panel(self,-1,pos=(0,30),size=(800,600))
					self.nameLaber = wx.StaticText(panel,-1,"用户名",pos=(0,40))
					self.floderText = wx.TextCtrl(panel,-1,pos=(0,70),size=(250,-1))
					
					self.filLabel = wx.StaticText(panel,-1,"密码",pos=(0,100))
					self.fileText = wx.TextCtrl(panel,-1,pos=(0,130),size=(250,-1),style=wx.TE_PASSWORD)
					
					self.button6 = buttons.GenButton(panel,-1,"登录",pos=(0,160))
					self.Bind(wx.EVT_BUTTON,self.Login,self.button6)
		
		def OpenFloder(self,event):
					dialog = wx.DirDialog(None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
					if dialog.ShowModal() == wx.ID_OK:
							self.floderText.WriteText(dialog.GetPath())
					dialog.Destroy()
					
		def OpenFile(self,event):
					wildcard = "mp3 source (*.mp3)|*.mp3|" \
					"All files (*.*)|*.*"
					dialog = wx.FileDialog(None, "Choose a file:",os.getcwd()," ",wildcard,wx.OPEN)
					if dialog.ShowModal() == wx.ID_OK:
							self.fileText.WriteText(dialog.GetPath())
					dialog.Destroy()
					
		def StartUp(self,event):
					a = example.example("asdf")
					a.Func()
					
		def Login(self,event):
			print "b";
					
										
app = wx.PySimpleApp()
frame = StaticTextFrame()
frame.Show()
app.MainLoop()