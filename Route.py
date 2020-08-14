class Route(object):
    """description of class"""
    def __init__(self,id):
        self.id=id
        self.RouteSequence=[]

    def addRoute(self,workcenter):
        self.RouteSequence.append(workcenter)


