class WorkCenter(object):
    """description of class"""
    def __init__(self,id,hoursInWeek):
        self.id=id
        self.machines=[]
        self.HoursInWeek=hoursInWeek

    def addMachine(self,machine):
        self.machines.append(machine)
