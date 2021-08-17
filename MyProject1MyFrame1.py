"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

from re import S, sub
import wx
import re
import csv
import time
import sys
import datetime
import threading
import XDM1041
from XDM1041_1 import XDM1041_1

RANGELABELS = {
    "DC VOLTAGE": ["50mV", "500mV", "5V", "50V", "500V", "1000V", "AUTO"],
    "DC CURRENT": ["500uA", "5mA", "50mA", "500mA", "5A", "10A", "AUTO"],
    "AC VOLTAGE": ["500mV", "5V", "50V", "500V", "750V", "AUTO"],
    "AC CURRENT": ["500uA", "5mA", "50mA", "500mA", "5A", "10A", "AUTO"],
    "RESISTANCE": ["500Ω", "5kΩ", "50kΩ", "500kΩ", "5MΩ", "50MΩ", "AUTO"],
    "CAPACITANCE": ["50nF", "500nF", "5uF", "50uF", "500uF", "5mF", "50mF", "AUTO"],
}

CSVLABEL = ["NO", "DATE", "TIME", "FUNCTION", "RANGE", "SPEED", "VALUE"]

FUNCTIOLIST = [
    "DC VOLTAGE",
    "DC CURRENT",
    "AC VOLTAGE",
    "AC CURRENT",
    "RESISTANCE",
    "CAPACITANCE",
]

FIRSTFUNCTION = "DC VOLTAGE"
FIRSTRANGE = "AUTO"


MULDICT = {
    "50mV": 1e3,
    "500mV": 1e3,
    "5V":1,
    "50V": 1,
    "1000V": 1,
    "AUTO": 1,
    "500uA": 1e6,
    "5mA": 1e3,
    "50mA": 1e3,
    "500mA": 1e3,
    "5A": 1,
    "10A": 1,
    "AUTO": 1,
    "500Ω": 1,
    "5kΩ": 1e-3,
    "50kΩ": 1e-3,
    "500kΩ": 1e-3,
    "5MΩ": 1e-6,
    "50MΩ": 1e-3,
    "AUTO": 1,
    "50nF": 1e-9,
    "500nF": 1e-9,
    "5uF": 1e-9,
    "50uF": 1e-6,
    "500uF": 1e-6,
    "5mF": 1e-3,
    "50mF": 1e-3,
    "AUTO": 1,
}
# Implementing MyFrame1
class MyProject1MyFrame1(XDM1041.MyFrame1):
    def __init__(self, parent):
        XDM1041.MyFrame1.__init__(self, parent)
        self.XDM = XDM1041_1
        self.SaveFileName = ""
        self.WriteNum = 0
        self.IsWriteLable = False
        self.MeasuredValue = 0.0
        self.MeasuredFunction = FIRSTFUNCTION
        self.SleepTime = 2.0

        self.m_choice3.Append(FUNCTIOLIST)
        self.m_choice3.Select(FUNCTIOLIST.index(FIRSTFUNCTION))  # DC VOLTAGE
        self.m_choice4.Append(RANGELABELS.get(FIRSTFUNCTION, None))
        self.m_choice4.Select(
            (RANGELABELS.get(FIRSTFUNCTION, None)).index(FIRSTRANGE)
        )  # AUTO

        self.CSVthread = threading.Thread(target=self.LoopWriteCSV)
        self.Measurethread = threading.Thread(target=self.LoopPrintMeasureValue)
        self.Timethread = threading.Thread(target=self.LoopTimePrint)

        self.CSVthread.setDaemon(True)
        self.Measurethread.setDaemon(True)
        self.Timethread.setDaemon(True)

        self.CSVthread.start()
        self.Measurethread.start()
        self.Timethread.start()

    def LoopTimePrint(self):
        while True:
            Date = datetime.datetime.now()
            Day = Date.strftime("%Y-%m-%d")
            Time = Date.strftime("%H:%M:%S")
            
            self.m_textCtrl71.Value = "{} {}".format(Day, Time)
            time.sleep(1)

    def LoopPrintMeasureValue(self):
        while True:
            if self.m_checkBox1.Value:
                if self.m_checkBox2:
                    Value = self.XDM.GetMeasureValue(self)
                else:
                    Value = 0

                self.MeasuredValue = Value
                Func = self.m_choice3.GetStringSelection()
                Range = self.m_choice4.GetStringSelection()

                self.m_textCtrl4.Value = Range
                if Value >= 1000000000:
                    self.m_textCtrl5.Value = "OVER LOAD"
                else:
                   
                    Mul = MULDICT.get(Range, None)
                    #Res = re.match(Range, "[a-zA-Z]+")
                    Unit = re.sub("[^a-zA-Z]", "", Range)
                    #if Unit == "AUTO":

                    Val = "{:.5f}".format(Value * Mul)

                    self.m_textCtrl5.Value = Val + Unit

                self.m_textCtrl6.Value = Func
            else:
                self.m_textCtrl4.Value = "NO OPEN"
                self.m_textCtrl4.Value = ""
                self.m_textCtrl4.Value = ""

            time.sleep(1)

    def LoopWriteCSV(self):
        while True:
            if self.m_checkBox2.Value:
                Value = self.MeasuredValue
                if Value == 1000000000:  # overload
                    Value = "OVER LOAD"

                Date = datetime.datetime.now()
                Day = Date.strftime("%Y-%m-%d")
                Time = Date.strftime("%H:%M:%S:%f")
                Func = self.m_choice3.GetStringSelection()
                Range = self.m_choice4.GetStringSelection()
                Speed = self.m_choice6.GetStringSelection()

                Num = self.WriteNum
                row = [Num, Day, Time, Func, Range, Speed, Value]
                if self.IsWriteLable:
                    self.Writer.writerow(row)
                else:
                    self.Writer.writerow(CSVLABEL)
                    self.IsWriteLable = True

                self.WriteNum = self.WriteNum + 1
            else:
                self.WriteNum = 0
                self.IsWriteLable = False

            time.sleep(self.SleepTime)

    # Handlers for MyFrame1 events.
    def ComOpenEvent(self, event):
        # TODO: Implement ComOpenEvent

        if self.m_checkBox1.Value:
            COM = self.m_choice2.GetStringSelection()
            Baud = self.m_choice5.GetStringSelection()

            try:
                self.XDM.OpenCOM(self, COM, Baudrate=int(Baud))

            except:
                self.m_textCtrl7.Value = "CONNECTION  FAILE"
                self.m_textCtrl7.ForegroundColour = (255, 0, 0)
                self.m_checkBox1.Value = False

            else:
                self.XDM.SwitchToRemoto(self)
                self.m_textCtrl7.Value = "CONNECTION  OPEN"
                self.m_textCtrl7.ForegroundColour = (0, 255, 0)

                self.SelectMeasureEvent(self)

        else:
            self.m_textCtrl7.Value = "CONNECTION CLOSE"
            self.m_textCtrl7.ForegroundColour = (0, 0, 0)
            self.XDM.SwitchToLocal(self)
            self.XDM.CloseCOM(self)

        pass

    def OnSelectCOM(self, event):
        # TODO: Implement OnSelectCOM
        pass

    def SelectSaveFileEvent(self, event):
        # TODO: Implement SelectSaveFileEvent
        self.m_textCtrl9.Value = self.m_filePicker1.GetPath()
        pass

    def SaveActiveEvent(self, event):
        # TODO: Implement SaveActiveEvent

        if self.m_checkBox2.Value:
            self.SaveFileName = self.m_filePicker1.GetPath()
            self.CSVFile = open(self.SaveFileName, "w", encoding="utf-8", newline="")
            self.Writer = csv.writer(self.CSVFile)
            try:
                self.SleepTime = int(self.m_textCtrl8.Value)

            except:
                self.SleepTime = 2

        else:
            self.CSVFile.close()

        pass

    def SelectMeasureEvent(self, event):
        # TODO: Implement SelectMeasureEvent
        Func = self.m_choice3.GetStringSelection()
        Label = RANGELABELS.get(Func, None)

        Cnt = self.m_choice4.GetCount()
        for i in range(Cnt):
            self.m_choice4.Delete(0)

        self.m_choice4.Append(Label)
        self.m_choice4.Select((Label.index("AUTO")))  # AUTO

        if self.m_checkBox1.Value:
            self.XDM.ConfigureFunction(self, Func, "AUTO")

        pass

    def SelectRangeEvent(self, event):
        # TODO: Implement SelectRangeEvent
        Func = self.m_choice3.GetStringSelection()
        Range = self.m_choice4.GetStringSelection()

        if self.m_checkBox1.Value:
            self.XDM.ConfigureFunction(self, Func, Range)

        pass

    def OnChangeSpeedEvent(self, event):
        # TODO: Implement OnChangeSppedEvent
        if self.m_checkBox1.Value:
            self.XDM.ChangeMeasureSpeed(self, self.m_choice6.GetStringSelection())
        pass

    # Handlers for MyFrame1 events.
    def ExitEvent(self, event):
        # TODO: Implement ExitEvent
        if self.m_checkBox2.Value:
            self.CSVFile.close()

        if self.m_checkBox1.Value:
            self.XDM.SwitchToLocal(self)
            self.XDM.CloseCOM(self)

        
        sys.exit(0)
        pass