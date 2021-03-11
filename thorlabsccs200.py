import os, sys, clr
from System import *
import numpy as np
import matplotlib.pyplot as plt
#MUST HAVE pythonNET installed!
sys.path.append(r"C:\Program Files (x86)\Microsoft.NET\Primary Interop Assemblies\\")
clr.AddReference("Thorlabs.ccs.interop64")
#import the NET reference
import Thorlabs.ccs.interop64
#create the spectrometer object
spec = Thorlabs.ccs.interop64.TLCCS("USB0::0x1313::0x8089::M00458735::RAW",Boolean(True),Boolean(True))
#set integration time
integrationTime = Double(.1)
spec.setIntegrationTime(integrationTime)
#obtain wavelength array from spectrometer
ref16 = Int16(0)
nullable_double =Nullable[Double](0)
wvdata = Array.CreateInstance(Double,3648)
spec.getWavelengthData(ref16,wvdata,nullable_double,nullable_double)
wavelengths = np.asarray(list(wvdata))
#start scan
spec.startScan()
#obtain scan data
scan = Array.CreateInstance(Double,3648)
spec.getScanData(scan)
scandata = np.asarray(list(scan))
#plot
plt.plot(wavelengths,scandata)
