class FinishedGood(object):
    """description of class"""
    def __init__(self,id):
        self.id=id
        self.Route=''
        self.Units=0
    def addFinishedGood(self,route):
        self.Route = route
        self.Units=0