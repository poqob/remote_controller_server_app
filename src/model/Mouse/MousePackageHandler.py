from model.Mouse.MouseModel import MouseModel
from queue import Queue


class MousePackageHandler:
    queue = Queue(maxsize=3)
    model0: MouseModel = None  # firstly called mouse action.
    model1: MouseModel = None  # lastly called mouse action.
    isReadyToGetPackage: bool = False

    def __init__(self) -> None:
        pass

    def manage(self, model: MouseModel):
        if self.queue.full():
            self.model0 = self.queue.get()
            self.model1 = self.queue.get()
            res = self.model1.x - self.model0.x, self.model1.y - self.model0.y  # x, y
            self.isReadyToGetPackage = True
            if abs(res[0]) > 5 or abs(res[1]) > 5:
                self.isReadyToGetPackage = False
        else:
            res = None
            self.isReadyToGetPackage = False
        self.queue.put(model)
        return self.isReadyToGetPackage, res

    def dequeue(self):
        self.queue = Queue(maxsize=3)
