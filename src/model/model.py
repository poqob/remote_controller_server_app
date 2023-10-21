import json
from model.InputType import InputType
from model.Mouse.MouseModel import MouseModel


class Model:
    # fields
    inputType: InputType = None
    body: map = None

    # constructor
    def __init__(self) -> None:
        pass

    def jsonToModel(self, json_string):
        _json_string = json.loads(json_string)
        temp = _json_string["INPUT_TYPE"]
        self.inputType = InputType(int(temp))
        self.body = _json_string["BODY"]
        return self


data = {
    "INPUT_TYPE": 0,
    "BODY": {"MMode": 0, "X": 100, "Y": 100, "ACTION": 1},
}

if __name__ == "__main__":
    model = Model()
    json_data = json.dumps(data)  # Convert the Python dictionary to a JSON string
    model.jsonToModel(json_data)  # Deserialize the JSON content into the Model class
    content = None
    if model.inputType.value == 0:
        content = MouseModel(model.body)
    elif model.inputType.value == 1:
        # content = KeyboardModel(model.body)
        pass
    else:
        TypeError()
    print(content.__str__())
