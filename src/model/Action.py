from model.model import Model
from model.Mouse.MouseModel import MouseModel
from model.Mouse.MouseController import MouseController


class Action:
    mouseController = None

    def __init__(self) -> None:
        self.mouseController = MouseController()

    def _behaviour(self, model: Model):
        if model.inputType.value == 0:
            m = MouseModel(model.body)
            self.mouseController.handle(m)
        elif model.inputType.value == 1:
            pass
