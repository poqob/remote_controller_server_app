from model.Mouse.MouseActions import MouseActions
from model.Mouse.MousePadBehaviour import MousePadBehaviour


class MouseModel:
    mouseBehaviour: MousePadBehaviour = None
    x: int = 0
    y: int = 0
    action: MouseActions = None

    def __init__(self, body: map = None):
        if body is not None:
            self.mouseBehaviour = MousePadBehaviour(int(body.get("mMode")))
            self.x = body.get("X")
            self.y = body.get("Y")
            self.action = MouseActions(int(body.get("ACTION")))
        else:
            pass

    def decode(self, body: map):
        self.mouseBehaviour = MousePadBehaviour(int(body.get("mMode")))
        self.x = body.get("X")
        self.y = body.get("Y")
        self.action = MouseActions(int(body.get("ACTION")))
        return self

    def __str__(self) -> str:
        return self.action.__str__() + " " + self.mouseBehaviour.__str__()


if __name__ == "__main__":
    map = {"mMode": 0, "X": 100, "Y": 100, "ACTION": 1}
    model = MouseModel()
    print(model.decode(map))
