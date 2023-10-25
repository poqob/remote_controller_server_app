from model.model import Model
from model.Mouse.MouseModel import MouseModel
from model.Mouse.MouseController import MouseController


class Action:
    """
    Represents an action that can be performed by the remote controller.

    Attributes:
    - mouseController: The mouse controller object used to handle mouse actions.
    """

    mouseController = None

    def __init__(self) -> None:
        self.mouseController = MouseController()

    def _behaviour(self, model: Model):
        """
        Defines the behavior of the action based on the input type of the model.

        Args:
        - model: The model object containing the input type and body.

        Returns:
        - None
        """
        if model.inputType.value == 0:
            m = MouseModel(model.body)
            self.mouseController.handle(m)
        elif model.inputType.value == 1:
            pass
