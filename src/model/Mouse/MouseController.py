from model.Mouse.MouseModel import MouseModel
from model.Mouse.MouseActions import MouseActions
from model.Mouse.MousePadBehaviour import MousePadBehaviour
from model.Mouse.MousePackageHandler import MousePackageHandler
import mouse

SCROLL_POWER_VALUE = 0.06


class MouseController:
    currentAction: MouseModel = None
    packageHandler: MousePackageHandler = None

    def __init__(self) -> None:
        self.packageHandler = MousePackageHandler()
        pass

    def handle(self, mouseModel: MouseModel):
        print(mouseModel.mouseBehaviour)
        self.currentAction = mouseModel
        if mouseModel.mouseBehaviour == MousePadBehaviour.STATIC:
            self._static_pad_controller()
        elif mouseModel.mouseBehaviour == MousePadBehaviour.DYNAMIC:
            self._dynamic_pad_controller()

    def _static_pad_controller(self):
        match self.currentAction.action:
            case MouseActions.LEFT_CLICK:
                mouse.click(button="left")
            case MouseActions.RIGHT_CLICK:
                mouse.click(button="right")
            case MouseActions.DOUBLE_CLICK_LEFT:
                mouse.double_click(button="left")
            case MouseActions.DOUBLE_CLICK_RIGHT:
                mouse.double_click(button="right")
            case MouseActions.SCROLL_DOWN:
                mouse.wheel(delta=-SCROLL_POWER_VALUE)
            case MouseActions.SCROLL_UP:
                mouse.wheel(delta=SCROLL_POWER_VALUE)
            case MouseActions.MOVE:  ## static move
                mouse.move(
                    self.currentAction.x,
                    self.currentAction.y,
                    absolute=True,
                    duration=0,
                )
            case MouseActions.DRAG_START:  ## later updates
                # mouse.drag(start_x, start_y, end_x, end_y, absolute=True, duration=0)
                if mouse.is_pressed(button="left") is False:
                    mouse.press(button="left")
                mouse.move(
                    self.currentAction.x,
                    self.currentAction.y,
                    absolute=True,
                    duration=0,
                )
            case MouseActions.DRAG_CANCEL:
                if mouse.is_pressed(button="left") is True:
                    mouse.release(button="left")
            case MouseActions.RELEASE:
                if mouse.is_pressed(button="left") is True:
                    mouse.release(button="left")
                if mouse.is_pressed(button="right") is True:
                    mouse.release(button="right")
            case _:
                pass

    dynamicPadCompanent: MouseModel = None

    # TODO: dynamic move
    # take packages to a structure
    # p0, p1, p2
    # then calculate difference between p2 and p1.
    # then return an (x,y)
    # add new (x,y) to mouse position.
    # apply new possition to move~drag
    # action2 is currentAction
    # suppose have x,y,action space:(0,0)(0,1)(1,0)(1,1)||(0,0)(0,-1)(-1,0)(-1,-1)
    def _dynamic_pad_controller(self):
        print("TEST")
        ret, self.dynamicPadCompanent = self.packageHandler.manage(self.currentAction)
        print(self.dynamicPadCompanent)
        if ret is True:
            match self.currentAction.action:
                case MouseActions.LEFT_CLICK:
                    mouse.click(button="left")
                case MouseActions.RIGHT_CLICK:
                    mouse.click(button="right")
                case MouseActions.DOUBLE_CLICK_LEFT:
                    mouse.double_click(button="left")
                case MouseActions.DOUBLE_CLICK_RIGHT:
                    mouse.double_click(button="right")
                case MouseActions.SCROLL_DOWN:
                    mouse.wheel(delta=-SCROLL_POWER_VALUE)
                case MouseActions.SCROLL_UP:
                    mouse.wheel(delta=SCROLL_POWER_VALUE)
                case MouseActions.MOVE:  ## dynamic move
                    x, y = mouse.get_position()
                    mouse.move(
                        x + self.dynamicPadCompanent[0],
                        y + self.dynamicPadCompanent[1],
                        absolute=True,
                        duration=0,
                    )
                case MouseActions.DRAG_START:  ## later updates
                    x, y = mouse.get_position()
                    # mouse.drag(start_x, start_y, end_x, end_y, absolute=True, duration=0)
                    if mouse.is_pressed(button="left") is False:
                        mouse.press(button="left")
                    mouse.move(
                        x + self.dynamicPadCompanent[0],
                        y + self.dynamicPadCompanent[1],
                        absolute=True,
                        duration=0,
                    )
                case MouseActions.DRAG_CANCEL:
                    if mouse.is_pressed(button="left") is True:
                        mouse.release(button="left")
                        self.packageHandler.dequeue()

                case MouseActions.RELEASE:
                    if mouse.is_pressed(button="left") is True:
                        mouse.release(button="left")
                    if mouse.is_pressed(button="right") is True:
                        mouse.release(button="right")
                    self.packageHandler.dequeue()
                case _:
                    pass
