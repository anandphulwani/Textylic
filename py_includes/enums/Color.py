from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    GREEN = 3
    PINK = 4
    
    def to_string(self):
        return self.name

    def label(self):
        return self.name.capitalize()
