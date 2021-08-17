import serial
import time

CONFIGFUNCTIONDICT = {
    "DC VOLTAGE": "CONF:VOLT:DC ",
    "AC VOLTAGE": "CONF:VOLT:AC ",
    "DC CURRENT": "CONF:CURR:DC ",
    "AC CURRENT": "CONF:CURR:AC ",
    "RESISTANCE": "CONF:RES ",
    "CAPACITANCE": "CONF:CAP ",
}

DCVOLTAGERANGEDICT = {
    "50mV": "50E-3",
    "500mV": "500E-3",
    "5V": "5",
    "50V": "50",
    "500V": "500",
    "1000V": "1000",
    "AUTO": "AUTO",
}

DCCURRENTRANGEDICT = {
    "500uA": "500E-6",
    "5mA": "5E-3",
    "50mA": "50E-3",
    "500mA": "500E-3",
    "5A": "5",
    "10A": "10",
    "AUTO": "AUTO",
}

ACVOLTAGERANGEDICT = {
    "500mV": "500E-3",
    "5V": "5",
    "50V": "50",
    "500V": "500",
    "750V": "750",
    "AUTO": "AUTO",
}

ACCURRENTRANGEDICT = {
    "500uA": "500E-6",
    "5mA": "5E-3",
    "50mA": "50E-3",
    "500mA": "500E-3",
    "5A": "5",
    "10A": "10",
    "AUTO": "AUTO",
}

RESITANCERANGEDICT = {
    "500Ω": "500",
    "5kΩ": "5E3",
    "50kΩ": "50E3",
    "500kΩ": "500E3",
    "5MΩ": "5E6",
    "50MΩ": "50E6",
    "AUTO": "AUTO",
}

CAPACITANCERANGEDICT = {
    "50nF": "50E-9",
    "500nF": "500E-9",
    "5uF": "5E-6",
    "50uF": "50E-6",
    "500uF": "500E-6",
    "5mF": "5E-3",
    "50mF": "50E-3",
    "AUTO": "AUTO",
}


RANGEDICT = {
    "DC VOLTAGE": DCVOLTAGERANGEDICT,
    "DC CURRENT": DCCURRENTRANGEDICT,
    "AC VOLTAGE": ACVOLTAGERANGEDICT,
    "AC CURRENT": ACCURRENTRANGEDICT,
    "RESISTANCE": RESITANCERANGEDICT,
    "CAPACITANCE" : CAPACITANCERANGEDICT
}

SPEEDDICT = {"FAST": "F", "MEDIUM": "M", "SLOW": "S"}


class XDM1041_1:
    def __init__(self):
        self.Open = False

    def OpenCOM(self, COM, Baudrate=115200):
        self.Serial = serial.Serial(COM, Baudrate)
        self.Open = True

    def CloseCOM(self):
        self.Open = False
        self.Serial.close()

    def GetIDN(self):
        self.Serial.write(b"*IDN?\n")
        return self.Serial.readline()

    def SwitchToRemoto(self):
        self.Serial.write(b"SYST:REM\n")

    def SwitchToLocal(self):
        self.Serial.write(b"SYST:LOC\n")

    def ChangeMeasureSpeed(self, Speed):
        Rate = SPEEDDICT.get(Speed, None)
        self.Serial.write(bytearray(("Rate " + Rate + "\n"), "utf-8"))

    def GetMeasureValue(self):
        self.Serial.write(b"MEAS?\n")
        time.sleep(0.5)
        Val = self.Serial.readline()
        try:
            data = float(Val[0:-2])
        except:
            data = 0.0  # とりあえず

        return data

    def ConfigureFunction(self, Function, Range):

        Func = CONFIGFUNCTIONDICT.get(Function, None)
        Ranges = RANGEDICT.get(Function, None)
        Index = Ranges.get(Range, None)
        if Index == None:
            return

        self.Serial.write(bytearray((Func + Index + "\n"), "utf-8"))
