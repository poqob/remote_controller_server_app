from model.Mouse.MouseModel import MouseModel
from model.Mouse.MouseActions import MouseActions
from model.Mouse.MousePadBehaviour import MousePadBehaviour
from model.Mouse.MousePackageHandler import MousePackageHandler
import mouse

# TODO: changable values, depends on the host application input ~ maybe client side??
SCROLL_POWER_VALUE = 0.06
DRAG_TOLERANCE_VALUE = 20


class MouseController:
    """
    This class is responsible for controlling the mouse actions based on the received MouseModel object.
    """

    currentAction: MouseModel = None
    packageHandler: MousePackageHandler = None

    def __init__(self) -> None:
        """
        Initializes the MouseController object with a MousePackageHandler object.
        """
        self.packageHandler = MousePackageHandler()

    def handle(self, mouseModel: MouseModel):
        """
        Handles the mouse actions based on the received MouseModel object.

        Args:
            mouseModel (MouseModel): The MouseModel object containing the mouse action to be performed.
        """
        self.currentAction = mouseModel
        isCommon = self._common_events()
        if isCommon is False:
            if mouseModel.mouseBehaviour == MousePadBehaviour.STATIC:
                self._static_pad_controller()
            elif mouseModel.mouseBehaviour == MousePadBehaviour.DYNAMIC:
                self._dynamic_pad_controller()

    def _common_events(self) -> bool:
        """
        Handles the common mouse events such as left click, right click, double click, scroll, and release.

        Returns:
            bool: True if the received mouse action is a common event, False otherwise.
        """
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

    def _static_pad_controller(self):
        """
        Handles the mouse actions for static mouse pad behaviour such as move, drag start, drag cancel, and release.
        """
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

    def _dynamic_pad_controller(self):
        """
        Handles the mouse actions for dynamic mouse pad behaviour such as move, drag start, drag cancel, and release.
        """
        ret, res = self.packageHandler.manage(self.currentAction)
        if abs(res[0]) > DRAG_TOLERANCE_VALUE or abs(res[1]) > DRAG_TOLERANCE_VALUE:
            ret = False
        # print(res[0], res[1], ret)

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


# TODO: Drag mode cannot support pencil-draw mode
# To solve this issue: update drag behaviour as: press(once) -> move -> release to pressing -> move -> pressing -> move -> release
# May we add a pencil mode for tablets??????

# TODO: Add Horizontal scroll

# TODO: clean up the code
