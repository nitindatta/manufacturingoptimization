from collections import defaultdict

class Efficiency(object):
    """description of class"""
    def __init__(self,id):
        self.id=id
        self.efficiency=defaultdict(dict)

    def addMachineEfficiency(self,machineid,finishedGoodid,efficiency):
        self.efficiency[machineid][finishedGoodid]=efficiency
