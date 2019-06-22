import os
import datetime

"""
function to get the Date data from system.
"""
def getFolderDateWeekAndDay():
    now = datetime.datetime.now()
    weekDay = now.strftime("%A")
    timeOfDay = now.strftime("%H")
    weekOfYear= now.strftime("%W")
    return weekDay,timeOfDay,weekOfYear

'''create  directory'''
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
     
### week number wise folder 0 to 53        
def createWeekFolder(weekNo):
    createFolder('./'+weekNo)
    os.chdir('./'+weekNo)
        
### day name wise folder Monday - Sunday    
def createDayFolder(day):
    createFolder('./'+day)
    os.chdir('./'+day)
    
## hour wise folder i.e 00 to 23    
def createHourFolder(time):
    createFolder('./'+time)
    os.chdir('./'+time)
    
## calling function initially   
weekDay,timeOfDay,weekOfYear = getFolderDateWeekAndDay()
createWeekFolder(weekOfYear)
createDayFolder(weekDay)
createHourFolder(timeOfDay)

## working in infinite loop.
i=0;   
while(True):
    print (i)
    i=i+1
    dirpath = os.getcwd()
    strDir = dirpath.split('/')
    size=len(strDir)
    prevDay = strDir[size-2]
    prevWeek = strDir[size-3]
    prevTime = os.path.basename(dirpath)
    
    #getting actual time
    weekDay,timeOfDay,weekOfYear = getFolderDateWeekAndDay()

    #updating folders according to time 
    if(weekOfYear!=prevWeek):
        os.chdir('../../..')
        createWeekFolder(weekOfYear)
        createDayFolder(weekDay)
        createHourFolder(timeOfDay)
    elif(weekDay!=prevDay):
        os.chdir('../..')
        createDayFolder(weekDay)
        createHourFolder(timeOfDay)
    elif(timeOfDay!=prevTime):
        os.chdir('../')
        createHourFolder(timeOfDay)
    else:
        pass
