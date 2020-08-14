class MaterialOrder(object):
    """description of class"""
    def __init__(self,id,finishedGood,quantity):
        self.id=id
        self.FinishedGood=finishedGood
        self.Quantity=quantity
    def addFinishedGood(self,finishedGood,quantity):
        self.FinishedGood = finishedGood
        self.Quantity=quantity


