import json
from model.InputType import InputType
from model.Mouse.MouseModel import MouseModel


class Model:
    """
    A class representing a model that can be converted from a JSON string.

    Attributes:
    -----------
    inputType : InputType
        The type of input for the model.
    body : map
        The body of the model.

    Methods:
    --------
    jsonToModel(json_string: str) -> Model
        Converts a JSON string to a Model object.
    """

    # fields
    inputType: InputType = None
    body: map = None

    # constructor
    def __init__(self) -> None:
        pass

    def jsonToModel(self, json_string: str) -> "Model":
        """
        Converts a JSON string to a Model object.

        Parameters:
        -----------
        json_string : str
            The JSON string to convert.

        Returns:
        --------
        Model
            The Model object created from the JSON string.
        """
        _json_string = json.loads(json_string)
        temp = _json_string["INPUT_TYPE"]
        self.inputType = InputType(int(temp))
        self.body = _json_string["BODY"]
        return self
