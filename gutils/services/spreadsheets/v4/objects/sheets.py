import enum
import typing

from pydantic import BaseModel

from gutils.services.spreadsheets.v4.objects.cells import CellData, CellFormat

from gutils.services.spreadsheets.v4.objects.general import *
from gutils.services.spreadsheets.v4.objects.charts import EmbeddedChart
from gutils.services.spreadsheets.v4.objects.developer_metadata import DeveloperMetadata

class SheetType(str, enum.Enum):
    SHEET_TYPE_UNSPECIFIED = "SHEET_TYPE_UNSPECIFIED"
    GRID = "GRID"
    OBJECT = "OBJECT"
    DATA_SOURCE = "DATA_SOURCE"

class InterpolationPointType(str, enum.Enum):
    INTERPOLATION_POINT_TYPE_UNSPECIFIED = "INTERPOLATION_POINT_TYPE_UNSPECIFIED"
    MIN = "MIN"
    MAX = "MAX"
    NUMBER = "NUMBER"
    PERCENT = "PERCENT"
    PERCENTILE = "PERCENTILE"

class GridProperties(BaseModel):
    rowCount: int
    columnCount: int
    frozenRowCount: int
    frozenColumnCount: int
    hideGridlines: bool
    rowGroupControlAfter: bool
    columnGroupControlAfter: bool

class DataSourceSheetProperties(BaseModel):
    dataSourceId: int
    columns: typing.List[DataSourceColumn]
    dataExecutionStatus: DataExecutionStatus

class SheetProperties(BaseModel):
    sheetId: int
    title: str
    index: int
    sheetType: SheetType
    gridProperties: GridProperties
    hidden: bool
    tabColorStyle: ColorStyle
    rightToLeft: bool
    dataSourceSheetProperties: DataSourceSheetProperties

class RowData(BaseModel):
    values: typing.List[CellData]

class DimensionProperties(BaseModel):
    hiddenByFilter: bool
    hiddenByUser: bool
    pixelSize: int
    developerMetadata: typing.List[DeveloperMetadata]
    dataSourceColumnReference: DataSourceColumnReference

class GridData(BaseModel):
    startRow: int
    startColumn: int
    rowData: typing.List[RowData]
    rowMetadata: typing.List[DimensionProperties]
    columnMetadata: typing.List[DimensionProperties]

class BooleanRule(BaseModel):
    condition: BooleanCondition
    format: CellFormat

class InterpolationPoint(BaseModel):
    colorStyle: ColorStyle
    type: InterpolationPointType
    value: str

class GradientRule(BaseModel):
    minpoint: InterpolationPoint
    midpoint: InterpolationPoint
    maxpoint: InterpolationPoint

class ConditionalFormatRule(BaseModel):
    ranges: typing.List[GridRange]
    booleanRule: BooleanRule
    gradientRule: GradientRule

class FilterView(BaseModel):
    pass

class ProtectedRange(BaseModel):
    pass

class BasicFilter(BaseModel):
    pass

class BandedRange(BaseModel):
    pass

class DimensionGroup(BaseModel):
    pass

class Slicer(BaseModel):
    pass

class Sheet(BaseModel):
    properties: SheetProperties
    data: typing.List[GridData]
    merges: typing.List[GridRange]
    conditionalFormats: typing.List[ConditionalFormatRule]
    filterViews: typing.List[FilterView]
    protectedRanges: typing.List[ProtectedRange]
    basicFilter: BasicFilter
    charts: typing.List[EmbeddedChart]
    bandedRanges: typing.List[BandedRange]
    developerMetadata: typing.List[DeveloperMetadata]
    rowGroups: typing.List[DimensionGroup]
    columnGroups: typing.List[DimensionGroup]
    slicers: typing.List[Slicer]
