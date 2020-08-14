# manufacturingoptimization
Change dates like production startdate from which date will be calculated in below variables in this file.
# Date Of Starting Production
productionStartDate = datetime.datetime(2019, 6, 22)
For tweaking no of hours in day machine will work tweak following
# No of hours machine will work in day this can be at workcenter level as well
noofHoursInDay = 8

for material orders tweak following to test 10, 1 , 1 are quantity of finished good for orders
manufacturingOrders = {}
manufacturingOrders["MO1"] = ManufacturingOrder("MO1",finishedGoods["FG1"],10)
manufacturingOrders["MO2"] = ManufacturingOrder("MO2",finishedGoods["FG2"],1)
manufacturingOrders["MO3"] = ManufacturingOrder("MO3",finishedGoods["FG3"],1)
you can change and test efficiences from 
efficiency currently is defined at no of units of FinishedGood per hour

machineefficiencies.addMachineEfficiency("M1","FG1",3)
machineefficiencies.addMachineEfficiency("M1","FG2",5)

For routes you can change following.
finishedGoods["FG1"] = FinishedGood("FG1")
route1 = Route("R1")
route1.addRoute(workcenters["WC1"])
route1.addRoute(workcenters["WC2"])
route1.addRoute(workcenters["WC3"])
finishedGoods["FG1"].addFinishedGood(route1)
machineefficiencies.addMachineEfficiency("M1","FG3",6)
