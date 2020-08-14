class Schedule(object):
    """description of class"""
    def __init__(self,id):
        self.id=id
        self.weeklyHours=[]
    def addMachine(self,machine):
        self.machines.append(machine)
