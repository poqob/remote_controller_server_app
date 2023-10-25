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
        # print(mouseModel.mouseBehaviour)
        self.currentAction = mouseModel
        if self._common_events() is False:
            if mouseModel.mouseBehaviour == MousePadBehaviour.STATIC:
                self._static_pad_controller()
            elif mouseModel.mouseBehaviour == MousePadBehaviour.DYNAMIC:
                self._dynamic_pad_controller()

    def _static_pad_controller(self):
        match self.currentAction.action:
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

    def _common_events(self) -> bool:
        match self.currentAction.action:
            case MouseActions.LEFT_CLICK:
                mouse.click(button="left")
                return True
            case MouseActions.RIGHT_CLICK:
                mouse.click(button="right")
                return True
            case MouseActions.DOUBLE_CLICK_LEFT:
                mouse.double_click(button="left")
                return True
            case MouseActions.DOUBLE_CLICK_RIGHT:
                mouse.double_click(button="right")
                return True
            case MouseActions.SCROLL_DOWN:
                mouse.wheel(delta=-SCROLL_POWER_VALUE)
                return True
            case MouseActions.SCROLL_UP:
                mouse.wheel(delta=SCROLL_POWER_VALUE)
                return True
            case MouseActions.RELEASE:
                if mouse.is_pressed(button="left") is True:
                    mouse.release(button="left")
                if mouse.is_pressed(button="right") is True:
                    mouse.release(button="right")
                return True
            case _:
                return False

    def _dynamic_pad_controller(self):
        ret, res = self.packageHandler.manage(self.currentAction)
        # print(res[0], res[1], ret)
        DRAG_TOLERANCE_VALUE = 20
        if abs(res[0]) > DRAG_TOLERANCE_VALUE or abs(res[1]) > DRAG_TOLERANCE_VALUE:
            ret = False

        if ret is True:
            match self.currentAction.action:
                case MouseActions.MOVE:  ## dynamic move
                    x, y = mouse.get_position()
                    mouse.move(
                        x + res[0],
                        y + res[1],
                        absolute=True,
                        duration=0,
                    )
                case MouseActions.DRAG_START:  ## later updates
                    x, y = mouse.get_position()
                    if mouse.is_pressed(button="left") is False:
                        mouse.press(button="left")
                    mouse.move(
                        x + res[0],
                        y + res[1],
                        absolute=True,
                        duration=0,
                    )
                case MouseActions.DRAG_CANCEL:
                    if mouse.is_pressed(button="left") is True:
                        mouse.release(button="left")

                case _:
                    pass
