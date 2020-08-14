import datetime
from datetime import timedelta 

# finish good - FG1
# work center - WC
from Machine import Machine
from WorkCenter import WorkCenter
from Efficiency import Efficiency
from MaterialOrder import MaterialOrder
from FinishedGood import FinishedGood
from Route import Route
# routing FG1 - WC1 , WC2 
# WC1 - M1,M2
# WC2 - M3,M4
# WC3 - M5,M6
# FG2  - WC2,WC3
# production efficiency M1 : fg1 - > 8 units/hrs
# M1 : FG1 = 8 units/hrs - (8)*24 units per day
# M2 : FG1 = 10 units/hrs
# M3 : FG1 = 5 units/hrs
# Require qty FG1 = 100 units
# FG1 time: (1/8)*100 + (1/10)*100 + (1/5)*100

# Prepare Data

# Date Of Starting Production
productionStartDate = datetime.datetime(2019, 6, 22)

# No of hours machine will work in day this can be at workcenter level as well
noofHoursInDay = 8


# Add Workcenters
workcenters = {}

workcenters["WC1"] = WorkCenter("WC1",40)
workcenters["WC2"] = WorkCenter("WC2",40)
workcenters["WC3"] = WorkCenter("WC3",40)

# Work Center Machines
workcenters["WC1"].addMachine(Machine("M1"))
workcenters["WC1"].addMachine(Machine("M2"))

workcenters["WC2"].addMachine(Machine("M3"))
workcenters["WC2"].addMachine(Machine("M4"))

workcenters["WC3"].addMachine(Machine("M5"))
workcenters["WC3"].addMachine(Machine("M6"))
workcenters["WC3"].addMachine(Machine("M7"))

# Finished Good Configurations
materialOrders = {}
finishedGoods = {}
finishedGoods["FG1"] = FinishedGood("FG1")
route1 = Route("R1")
route1.addRoute(workcenters["WC1"])
route1.addRoute(workcenters["WC2"])
route1.addRoute(workcenters["WC3"])
finishedGoods["FG1"].addFinishedGood(route1)

finishedGoods["FG2"] = FinishedGood("FG2")
route2 = Route("R2")
route2.addRoute(workcenters["WC2"])
route2.addRoute(workcenters["WC3"])

finishedGoods["FG2"].addFinishedGood(route2)

finishedGoods["FG3"] = FinishedGood("FG3")
route3 = Route("R3")
route3.addRoute(workcenters["WC3"])
route3.addRoute(workcenters["WC2"])
route3.addRoute(workcenters["WC1"])
finishedGoods["FG3"].addFinishedGood(route3)

# Machine Efficiences
machineefficiencies=Efficiency("E1")
machineefficiencies.addMachineEfficiency("M1","FG1",3)
machineefficiencies.addMachineEfficiency("M1","FG2",5)
machineefficiencies.addMachineEfficiency("M1","FG3",6)

machineefficiencies.addMachineEfficiency("M2","FG1",4)
machineefficiencies.addMachineEfficiency("M2","FG2",5)
machineefficiencies.addMachineEfficiency("M2","FG3",3)

machineefficiencies.addMachineEfficiency("M3","FG1",6)
machineefficiencies.addMachineEfficiency("M3","FG2",7)
machineefficiencies.addMachineEfficiency("M3","FG3",4)

machineefficiencies.addMachineEfficiency("M4","FG1",3)
machineefficiencies.addMachineEfficiency("M4","FG2",3)
machineefficiencies.addMachineEfficiency("M4","FG3",3)

machineefficiencies.addMachineEfficiency("M5","FG1",3)
machineefficiencies.addMachineEfficiency("M5","FG2",3)
machineefficiencies.addMachineEfficiency("M5","FG3",3)

machineefficiencies.addMachineEfficiency("M6","FG1",3)
machineefficiencies.addMachineEfficiency("M6","FG2",3)
machineefficiencies.addMachineEfficiency("M6","FG3",3)

machineefficiencies.addMachineEfficiency("M7","FG1",3)
machineefficiencies.addMachineEfficiency("M7","FG2",3)
machineefficiencies.addMachineEfficiency("M7","FG3",3)


# Set Up Material Orders
materialOrders["MO1"] = MaterialOrder("MO1",finishedGoods["FG1"],10)
materialOrders["MO2"] = MaterialOrder("MO2",finishedGoods["FG2"],1)
materialOrders["MO3"] = MaterialOrder("MO3",finishedGoods["FG3"],1)

# first get machines of wc fg needs from routing table
# get there efficiency
def date_by_adding_business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

finishedGoodTime={};
cumilativeMachineTime={};

def calculateTime():
    # loop through material order
    # loop through finished good
    # get routes
    # from routes get workcenter
    # from workcenter get machines
    # schedule machines
    # after scheduling machines calculate finished goods ttc (time to complete)
    
    for materialOrder in materialOrders.values():        # Loop through all orders
        print (materialOrder.FinishedGood.id)
        currentFinishedGood=materialOrder.FinishedGood
        currentFGId=currentFinishedGood.id
        finishedGoodTime[currentFGId]=0
        for workCenter in currentFinishedGood.Route.RouteSequence: # Loop routes for FG
            print ('--' + workCenter.id)    
            for machine in workCenter.machines:
                print ('----' + machine.id) 
                currentMachineId=machine.id;
                # efficiency = capacity for # of 1 finished good
                # e.g. if machine has efficiency of 8 fg in one hour then this is no 1 fg in how much time.
                efficiency=1/machineefficiencies.efficiency[currentMachineId][currentFGId]
                timeforMachineInHours = efficiency*materialOrder.Quantity
                if cumilativeMachineTime.get(machine.id,-1)==-1:
                    cumilativeMachineTime[machine.id]=0
                cumilativeMachineTime[machine.id] =timeforMachineInHours+cumilativeMachineTime[currentMachineId]
                finishedGoodTime[currentFGId]=finishedGoodTime[currentFGId]+cumilativeMachineTime[currentMachineId]
    return;

def calculateSchedule():
    for finishedGood in finishedGoodTime:
        hoursToComplete =finishedGoodTime[finishedGood]        
        daystoComplete = hoursToComplete/noofHoursInDay    
        daystoCompleteInHours = daystoComplete*24
        dateOfCompletion = date_by_adding_business_days(productionStartDate , 
                                                        daystoComplete);
        print ('time for production in days '+ finishedGood + ':'+ str(daystoComplete))
        print ('time for production in hours '+ finishedGood + ':'+ str(finishedGoodTime[finishedGood]))
        print ('Date for completing of  '+ finishedGood + ':'+ str(dateOfCompletion))
    return;

calculateTime()
calculateSchedule()

