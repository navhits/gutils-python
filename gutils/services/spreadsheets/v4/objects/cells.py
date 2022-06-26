import enum

from pydantic import BaseModel

from gutils.services.spreadsheets.v4.objects.general import *
from gutils.services.spreadsheets.v4.objects.pivot_tables import PivotTable

class NumberFormatType(str, enum.Enum):
    NUMBER_FORMAT_TYPE_UNSPECIFIED = "NUMBER_FORMAT_TYPE_UNSPECIFIED"
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    PERCENT = "PERCENT"
    CURRENCY = "CURRENCY"
    DATE = "DATE"
    TIME = "TIME"
    DATE_TIME = "DATE_TIME"
    SCIENTIFIC = "SCIENTIFIC"

class VerticalAlign(str, enum.Enum):
    VERTICAL_ALIGN_UNSPECIFIED = "VERTICAL_ALIGN_UNSPECIFIED"
    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"

class WrapStrategy(str, enum.Enum):
    WRAP_STRATEGY_UNSPECIFIED = "WRAP_STRATEGY_UNSPECIFIED"
    OVERFLOW_CELL = "OVERFLOW_CELL"
    LEGACY_WRAP = "LEGACY_WRAP"
    CLIP = "CLIP"
    WRAP = "WRAP"

class TextDirection(str, enum.Enum):
    TEXT_DIRECTION_UNSPECIFIED = "TEXT_DIRECTION_UNSPECIFIED"
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"

class HyperlinkDisplayType(str, enum.Enum):
    HYPERLINK_DISPLAY_TYPE_UNSPECIFIED = "HYPERLINK_DISPLAY_TYPE_UNSPECIFIED"
    LINKED = "LINKED"
    PLAIN_TEXT = "PLAIN_TEXT"


class Style(str, enum.Enum):
    STYLE_UNSPECIFIED = "STYLE_UNSPECIFIED"
    DOTTED = "DOTTED"
    DASHED = "DASHED"
    SOLID = "SOLID"
    SOLID_MEDIUM = "SOLID_MEDIUM"
    SOLID_THICK = "SOLID_THICK"
    NONE = "NONE"
    DOUBLE = "DOUBLE"

class DataSourceTableColumnSelectionType(str, enum.Enum):
    DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED = "DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED"
    SELECTED = "SELECTED"
    SYNC_ALL = "SYNC_ALL"
 
class NumberFormat(BaseModel):
    type: NumberFormatType
    pattern: str

class Border(BaseModel):
    style: Style
    colorStyle: ColorStyle

class Borders(BaseModel):
    top: Border
    right: Border
    bottom: Border
    left: Border

class Padding(BaseModel):
    top: float
    right: float
    bottom: float
    left: float

class TextRotation(BaseModel):
    angle: int
    vertical: bool

class TextFormatRun(BaseModel):
    startIndex: int
    format: TextFormat

class CellFormat(BaseModel):
    numberFormat: NumberFormat
    backgroundColorStyle: ColorStyle
    borders: Borders
    padding: Padding
    horizontalAlignment: HorizontalAlign
    verticalAlignment: VerticalAlign
    wrapStrategy: WrapStrategy
    textDirection: TextDirection
    textFormat: TextFormat
    hyperlinkDisplayType: HyperlinkDisplayType
    textRotation: TextRotation

class DataValidationRule(BaseModel):
    condition: BooleanCondition
    inputMessage: str
    strict: bool
    showCustomUi: bool

class DataSourceFormula(BaseModel):
    dataSourceId: str
    dataExecutionStatus: DataExecutionStatus

class DataSourceTable(BaseModel):
    dataSourceId: str
    columnSelectionType: DataSourceTableColumnSelectionType
    columns: typing.List[DataSourceColumnReference]
    filterSpecs: typing.List[FilterSpec]
    sortSpecs: typing.List[SortSpec]
    rowLimit: int
    dataExecutionStatus: DataExecutionStatus

class CellData(BaseModel):    
    userEnteredValue: ExtendedValue
    effectiveValue: ExtendedValue
    formattedValue: str
    userEnteredFormat: CellFormat
    effectiveFormat: CellFormat
    hyperlink: str
    note: str
    textFormatRuns: typing.List[TextFormatRun]
    dataValidation: DataValidationRule
    pivotTable: PivotTable
    dataSourceTable: DataSourceTable
    dataSourceFormula: DataSourceFormula
    
    
