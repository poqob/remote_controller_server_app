from model.Mouse.MouseModel import MouseModel
from queue import Queue


class MousePackageHandler:
    model0: MouseModel = None  # firstly called mouse action.
    model1: MouseModel = None  # lastly called mouse action.
    res: tuple = (0, 0)
    isReadyToGetPackage: bool = False

    def __init__(self) -> None:
        pass

    def manage(self, model: MouseModel):
        if self.model0 == None:
            self.model0 = model
            self.isReadyToGetPackage = False
        if self.model1 == None and self.model0 != None:
            self.model1 = model
            self.res = (self.model1.x - self.model0.x, self.model1.y - self.model0.y)
            self.isReadyToGetPackage = True
            self.model0 = self.model1
            self.model1 = None
            return self.isReadyToGetPackage, self.res
