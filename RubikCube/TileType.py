from enum import Enum


class TyleType(Enum):
    TOP_LEFT_CORNER = 0
    TOP_RIGHT_CORNER = 1
    BOTTOM_LEFT_CORNER = 2
    BOTTOM_RIGHT_CORNER = 3
    LEFT_EDGE = 4
    RIGHT_EDGE = 5
    TOP_EDGE = 6
    BOTTOM_EDGE = 7
    INNER_CELL = 8
