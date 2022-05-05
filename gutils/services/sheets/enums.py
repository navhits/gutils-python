import enum

class MajorDimension(str, enum.Enum):
    """
    Enum for the major dimensions of a sheet.
    """
    ROWS = "ROWS"
    COLUMNS = "COLUMNS"

class ValueInputOption(str, enum.Enum):
    """
    Enum for the value input options.
    """
    RAW = "RAW"
    USER_ENTERED = "USER_ENTERED"

class InsertDataOption(str, enum.Enum):
    """
    Enum for the insert data options.
    """
    OVERWRITE = "OVERWRITE"
    INSERT_ROWS = "INSERT_ROWS"

class ValueRenderOption(str, enum.Enum):
    """
    Enum for the value render options.
    """
    FORMATTED_VALUE = "FORMATTED_VALUE"
    UNFORMATTED_VALUE = "UNFORMATTED_VALUE"
    FORMULA = "FORMULA"

class DateTimeRenderOption(str, enum.Enum):
    """
    Enum for the date time render options.
    """
    SERIAL_NUMBER = "SERIAL_NUMBER"
    FORMATTED_STRING = "FORMATTED_STRING"
    