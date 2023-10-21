from enum import Enum


class MouseActions(Enum):
    LEFT_CLICK = 0
    RIGHT_CLICK = 1
    DOUBLE_CLICK_LEFT = 2
    DOUBLE_CLICK_RIGHT = 2
    DRAG = 3  # clicks left button then moves the cursor to the given position
    SCROLL_DOWN = 4
    SCROLL_UP = 5
    MOVE = 6  # only moves the cursor
