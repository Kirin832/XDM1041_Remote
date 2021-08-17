#! env python
# -*- coding: utf-8 -*-

import os
import sys
import wx
import serial
from serial.tools import list_ports
from MyProject1MyFrame1 import MyProject1MyFrame1


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyProject1MyFrame1(None)

    ports = list_ports.comports()
    devices = [info.device for info in ports]
    frame.m_choice2.Append(devices)

    frame.Show(True)
    app.MainLoop()



