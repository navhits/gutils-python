import enum
import typing

from pydantic import BaseModel, HttpUrl



class ThemeColorType(str, enum.Enum):
    THEME_COLOR_TYPE_UNSPECIFIED = "THEME_COLOR_TYPE_UNSPECIFIED"
    TEXT = "TEXT"
    ACCENT1 = "ACCENT1"
    ACCENT2 = "ACCENT2"
    ACCENT3 = "ACCENT3"
    ACCENT4 = "ACCENT4"
    ACCENT5 = "ACCENT5"
    ACCENT6 = "ACCENT6"
    LINK = "LINK"   

class DataExecutionState(str, enum.Enum):
    DATA_EXECUTION_STATE_UNSPECIFIED = "DATA_EXECUTION_STATE_UNSPECIFIED"
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"

class DataExecutionErrorCode(str, enum.Enum):
    DATA_EXECUTION_ERROR_CODE_UNSPECIFIED = "DATA_EXECUTION_ERROR_CODE_UNSPECIFIED"
    TIMED_OUT = "TIMED_OUT"
    TOO_MANY_ROWS = "TOO_MANY_ROWS"
    TOO_MANY_COLUMNS = "TOO_MANY_COLUMNS"
    TOO_MANY_CELLS = "TOO_MANY_CELLS"
    ENGINE = "ENGINE"
    PARAMETER_INVALID = "PARAMETER_INVALID"
    UNSUPPORTED_DATA_TYPE = "UNSUPPORTED_DATA_TYPE"
    DUPLICATE_COLUMN_NAMES = "DUPLICATE_COLUMN_NAMES"
    INTERRUPTED = "INTERRUPTED"
    CONCURRENT_QUERY = "CONCURRENT_QUERY"
    OTHER = "OTHER"
    TOO_MANY_CHARS_PER_CELL = "TOO_MANY_CHARS_PER_CELL"
    DATA_NOT_FOUND = "DATA_NOT_FOUND"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    MISSING_COLUMN_ALIAS = "MISSING_COLUMN_ALIAS"
    OBJECT_NOT_FOUND = "OBJECT_NOT_FOUND"
    OBJECT_IN_ERROR_STATE = "OBJECT_IN_ERROR_STATE"
    OBJECT_SPEC_INVALID = "OBJECT_SPEC_INVALID"

class ConditionType(str, enum.Enum):
    CONDITION_TYPE_UNSPECIFIED = "CONDITION_TYPE_UNSPECIFIED"
    NUMBER_GREATER = "NUMBER_GREATER"
    NUMBER_GREATER_THAN_EQ = "NUMBER_GREATER_THAN_EQ"
    NUMBER_LESS = "NUMBER_LESS"
    NUMBER_LESS_THAN_EQ = "NUMBER_LESS_THAN_EQ"
    NUMBER_EQ = "NUMBER_EQ"
    NUMBER_NOT_EQ = "NUMBER_NOT_EQ"
    NUMBER_BETWEEN = "NUMBER_BETWEEN"
    NUMBER_NOT_BETWEEN = "NUMBER_NOT_BETWEEN"
    TEXT_CONTAINS = "TEXT_CONTAINS"
    TEXT_NOT_CONTAINS = "TEXT_NOT_CONTAINS"
    TEXT_STARTS_WITH = "TEXT_STARTS_WITH"
    TEXT_ENDS_WITH = "TEXT_ENDS_WITH"
    TEXT_EQ = "TEXT_EQ"
    TEXT_IS_EMAIL = "TEXT_IS_EMAIL"
    TEXT_IS_URL = "TEXT_IS_URL"
    DATE_EQ = "DATE_EQ"
    DATE_BEFORE = "DATE_BEFORE"
    DATE_AFTER = "DATE_AFTER"
    DATE_ON_OR_BEFORE = "DATE_ON_OR_BEFORE"
    DATE_ON_OR_AFTER = "DATE_ON_OR_AFTER"
    DATE_BETWEEN = "DATE_BETWEEN"
    DATE_NOT_BETWEEN = "DATE_NOT_BETWEEN"
    DATE_IS_VALID = "DATE_IS_VALID"
    ONE_OF_RANGE = "ONE_OF_RANGE"
    ONE_OF_LIST = "ONE_OF_LIST"
    BLANK = "BLANK"
    NOT_BLANK = "NOT_BLANK"
    CUSTOM_FORMULA = "CUSTOM_FORMULA"
    BOOLEAN = "BOOLEAN"
    TEXT_NOT_EQ = "TEXT_NOT_EQ"
    DATE_NOT_EQ = "DATE_NOT_EQ"

class RelativeDate(str, enum.Enum):
    RELATIVE_DATE_UNSPECIFIED = "RELATIVE_DATE_UNSPECIFIED"
    PAST_YEAR  = "PAST_YEAR"
    PAST_MONTH = "PAST_MONTH"
    PAST_WEEK = "PAST_WEEK"
    YESTERDAY = "YESTERDAY"
    TODAY = "TODAY"
    TOMORROW = "TOMORROW"

class SortOrder(str, enum.Enum):
    SORT_ORDER_UNSPECIFIED = "SORT_ORDER_UNSPECIFIED"
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"

class Color(BaseModel):
    red: float
    blue: float
    green: float
    alpha: float

class HorizontalAlign(str, enum.Enum):
    HORIZONTAL_ALIGN_UNSPECIFIED = "HORIZONTAL_ALIGN_UNSPECIFIED"
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"

class ErrorType(str, enum.Enum):
    ERROR_TYPE_UNSPECIFIED = "ERROR_TYPE_UNSPECIFIED"
    ERROR = "ERROR"
    NULL_VALUE = "NULL_VALUE"
    DIVIDE_BY_ZERO = "DIVIDE_BY_ZERO"
    VALUE = "VALUE"
    REF = "REF"
    NAME = "NAME"
    NUM = "NUM"
    N_A = "N_A"
    LOADING = "LOADING"

class Dimension(str, enum.Enum):
    """
    Indicates which dimension an operation should apply to
    """
    DIMENSION_UNSPECIFIED = "DIMENSION_UNSPECIFIED"
    ROWS = "ROWS"
    COLUMNS = "COLUMNS"

class DimensionRange(BaseModel):
    sheetId: int
    dimension: Dimension
    startIndex: int
    endIndex: int

class ColorStyle(BaseModel):
    rgbColor: Color
    themeColor: ThemeColorType

class Link(BaseModel):
    url: HttpUrl

class TextFormat(BaseModel):
    foregroundColorStyle: ColorStyle
    fontFamily: str
    fontSize: int
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    link: Link

class DataSourceColumnReference(BaseModel):
    name: str

class DataSourceColumn(BaseModel):
    reference: DataSourceColumnReference
    formula: str

class DataExecutionStatus(BaseModel):
    state: DataExecutionState
    errorCode: DataExecutionErrorCode
    errorMessage: str
    lastRefreshTime: str

class GridRange(BaseModel):
    sheetId: int
    startRowIndex: int
    endRowIndex: int
    startColumnIndex: int
    endColumnIndex: int

class ConditionValue(BaseModel):
    relativeDate: RelativeDate
    userEnteredValue: str

class BooleanCondition(BaseModel):
    type: ConditionType
    values: typing.List[ConditionValue]

class FilterCriteria(BaseModel):
    hiddenValues: str
    condition: BooleanCondition

class FilterSpec(BaseModel):
    filterCriteria: FilterCriteria
    columnIndex: int
    dataSourceColumnReference: DataSourceColumnReference

class SortSpec(BaseModel):
    sortOrder: SortOrder
    foregroundColorStyle: ColorStyle
    backgroundColorStyle: ColorStyle
    dimensionIndex: int
    dataSourceColumnReference: DataSourceColumnReference

class GridCoordinate(BaseModel):
    sheetId: int
    rowIndex: int
    columnIndex: int

class OverlayPosition(BaseModel):
    anchorCell: GridCoordinate
    offsetXPixels: int
    offsetYPixels: int
    widthPixels: int
    heightPixels: int

class EmbeddedObjectPosition(BaseModel):
    sheetId: int
    overlayPosition: OverlayPosition
    newSheet: bool

class ErrorValue(BaseModel):
    type: ErrorType
    message: str

class ExtendedValue(BaseModel):
    numberValue: float
    stringValue: str
    boolValue: bool
    formulaValue: str
    errorValue: ErrorValue
