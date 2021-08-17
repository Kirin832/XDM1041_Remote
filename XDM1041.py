# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 589,433 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer142 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"NO OPEN", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		self.m_textCtrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "ＭＳ Ｐゴシック" ) )
		self.m_textCtrl4.SetForegroundColour( wx.Colour( 255, 255, 128 ) )
		self.m_textCtrl4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer142.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT|wx.TE_READONLY )
		self.m_textCtrl5.SetFont( wx.Font( 20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "ＭＳ Ｐゴシック" ) )
		self.m_textCtrl5.SetForegroundColour( wx.Colour( 255, 255, 128 ) )
		self.m_textCtrl5.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer142.Add( self.m_textCtrl5, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT|wx.TE_READONLY )
		self.m_textCtrl6.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "ＭＳ Ｐゴシック" ) )
		self.m_textCtrl6.SetForegroundColour( wx.Colour( 255, 255, 128 ) )
		self.m_textCtrl6.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer142.Add( self.m_textCtrl6, 0, wx.EXPAND|wx.ALL, 5 )


		bSizer14.Add( bSizer142, 1, wx.EXPAND, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl71 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer151.Add( self.m_textCtrl71, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl81 = wx.TextCtrl( self, wx.ID_ANY, u"Ver 1.0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer151.Add( self.m_textCtrl81, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer151, 0, wx.EXPAND, 5 )


		bSizer3.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer141 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"OPEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer15.Add( self.m_choice2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer141.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, u"CONNECTION CLOSE", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl7.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer141.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer141, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Baudrate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer11.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice5Choices = [ u"2400", u"4800", u"9600", u"19200", u"38400", u"57600", u"115200", wx.EmptyString ]
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 6 )
		bSizer11.Add( self.m_choice5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer171.Add( self.m_checkBox2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer171.Add( self.m_textCtrl9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Save file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE )
		bSizer171.Add( self.m_filePicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer18.Add( bSizer171, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"SAVE Time Interval", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer16.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_textCtrl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer18.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer18, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Measure function", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer10.Add( self.m_staticText2, 0, 0, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer10.Add( self.m_choice3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Range", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer12.Add( self.m_staticText3, 0, 0, 5 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0|wx.ALWAYS_SHOW_SB )
		self.m_choice4.SetSelection( 0 )
		bSizer12.Add( self.m_choice4, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Measuring speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer13.Add( self.m_staticText41, 0, 0, 5 )

		m_choice6Choices = [ u"FAST", u"MEDIUM", u"SLOW" ]
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 1 )
		bSizer13.Add( self.m_choice6, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer13, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.ExitEvent )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.ComOpenEvent )
		self.m_choice2.Bind( wx.EVT_CHOICE, self.OnSelectCOM )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.SaveActiveEvent )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.SelectSaveFileEvent )
		self.m_choice3.Bind( wx.EVT_CHOICE, self.SelectMeasureEvent )
		self.m_choice4.Bind( wx.EVT_CHOICE, self.SelectRangeEvent )
		self.m_choice6.Bind( wx.EVT_CHOICE, self.OnChangeSpeedEvent )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ExitEvent( self, event ):
		event.Skip()

	def ComOpenEvent( self, event ):
		event.Skip()

	def OnSelectCOM( self, event ):
		event.Skip()

	def SaveActiveEvent( self, event ):
		event.Skip()

	def SelectSaveFileEvent( self, event ):
		event.Skip()

	def SelectMeasureEvent( self, event ):
		event.Skip()

	def SelectRangeEvent( self, event ):
		event.Skip()

	def OnChangeSpeedEvent( self, event ):
		event.Skip()


