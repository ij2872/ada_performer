import serial
import matplotlib.pyplot as plt
from drawnow import *
import pickle 

values = []
save = []
maxValues = 125
i = 0

serialPort = "/dev/cu.usbmodem14201"
baud = 9600
adafruit = serial.Serial(serialPort, baud)
saveFileName = "motion.dat"
saveFile = open(saveFileName, 'w')

def plotValues():
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, 'rx-', label='Values')
    plt.legend(loc='upper right')


# Preload data


for i in range(26):
    values.append(0)

while True:
    while (adafruit.inWaiting() == 0):
        pass
    valueRead = adafruit.readline()

    # print("reading: " + valueRead.decode("utf-8"), end="")
    readInt = float(valueRead) # fix on non ints
    values.append(readInt)
    save.append(readInt)
    values.pop(0)
    drawnow(plotValues)
    i += 1
    if i == maxValues:
        with open(saveFileName, 'wb') as fp:
            pickle.dump(save, fp)
        exit()



