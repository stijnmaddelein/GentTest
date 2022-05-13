__version__ = '0.1.0'

from time import sleep
from GetAPiData import getData
from DataComm import ReadData
from DataComm import InsertData
import sys


#try:
#while True:
#    Responsing = getData()
    #added print to check if latest data is not 0. at certain point data returned was empty
#    print(Responsing)
#    for key,value in Responsing.items():
        #value has all dictionaries with all gotten values
        #datafields to send to database will be name, updatetime, occupation , totalcapacity, capacity, is open
#        InsertData(value)
    #wait for 5 minutes to get new data
#    sleep(300)
#use try except with keyboardInterrupt to get out of loop
#except KeyboardInterrupt:
#  sys.exit(0)

ReadData()


#check how to work with cron to make a service instead of simple sleep timer