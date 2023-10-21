from model.model import Model
from model.Mouse.MouseModel import MouseModel
from model.Mouse.MouseController import MouseController


class Action:
    @staticmethod
    def _behaviour(model: Model):
        if model.inputType.value == 0:
            m = MouseModel(model.body)
            MouseController.controllMouse(m)
        elif model.inputType.value == 1:
            pass
