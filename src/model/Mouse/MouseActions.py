from enum import Enum


from enum import Enum


class MouseActions(Enum):
    """
    An enumeration of possible mouse actions that can be performed by the remote controller.
    """

    LEFT_CLICK = 0
    RIGHT_CLICK = 1
    DOUBLE_CLICK_LEFT = 2
    DOUBLE_CLICK_RIGHT = 3
    DRAG_START = 4  # clicks left button then moves the cursor to the given position
    DRAG_CANCEL = 5
    SCROLL_DOWN = 6
    SCROLL_UP = 7
    MOVE = 8  # only moves the cursor
    SCALE_UP = 9
    SCALE_DOWN = 10
    RELEASE = 11
