from model.Mouse.MouseModel import MouseModel
from queue import Queue


class MousePackageHandler:
    """
    A class that handles mouse packages.

    Attributes:
    model0 (MouseModel): The first called mouse action.
    model1 (MouseModel): The last called mouse action.
    res (tuple): The result of the mouse action.
    isReadyToGetPackage (bool): A flag indicating whether the package is ready to be received or not.
    """

    model0: MouseModel = None
    model1: MouseModel = None
    res: tuple = (0, 0)
    isReadyToGetPackage: bool = False

    def __init__(self) -> None:
        pass

    def manage(self, model: MouseModel):
        """
        Manages the mouse package.

        Args:
        model (MouseModel): The mouse model to be managed.

        Returns:
        A tuple containing a flag indicating whether the package is ready to be received or not, and the result of the mouse action.
        """
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
