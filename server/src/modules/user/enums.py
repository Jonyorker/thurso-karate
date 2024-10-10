import enum

class Genders(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class Belt(enum.Enum):
    WHITE = "WHITE"
    WHITE_1 = "WHITE_1"
    WHITE_2 = "WHITE_2"
    WHITE_3 = "WHITE_3"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    GREEN = "GREEN"
    BLUE = "BLUE"
    BROWN = "BROWN"
    BLACK = "BLACK"
    BLACK_2 = "BLACK_2"
    BLACK_3 = "BLACK_3"

class AddressType(enum.Enum):
    MOM = 'MOM'
    DAD = 'DAD'
    HOME = 'HOME'