from model.Mouse.MouseModel import MouseModel
from model.Mouse.MouseActions import MouseActions
import mouse

data = {
    "mMode": "STATIC",
    "X": 100,
    "Y": 100,
    "ACTION": 1,
}


class MouseController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def controllMouse(mouseModel: MouseModel):
        match mouseModel.action:
            case MouseActions.LEFT_CLICK:
                mouse.click(button="left")
            case MouseActions.RIGHT_CLICK:
                mouse.click(button="right")
            case MouseActions.DOUBLE_CLICK_LEFT:
                mouse.double_click(button="left")
            case MouseActions.DOUBLE_CLICK_RIGHT:
                mouse.double_click(button="right")
            case MouseActions.SCROLL_DOWN:
                mouse.wheel(delta=-0.1)
            case MouseActions.SCROLL_UP:
                mouse.wheel(delta=1)
            case MouseActions.MOVE:  ## static move
                mouse.move(
                    mouseModel.x,
                    mouseModel.y,
                    absolute=True,
                    duration=0,
                )
            case MouseActions.DRAG_START:  ## later updates
                # mouse.drag(start_x, start_y, end_x, end_y, absolute=True, duration=0)
                if mouse.is_pressed(button="left") is False:
                    mouse.press(button="left")
                mouse.move(
                    mouseModel.x,
                    mouseModel.y,
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
