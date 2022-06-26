import enum
import typing
from datetime import datetime

from pydantic import BaseModel, Field


from gutils.services.spreadsheets.v4.objects.general import *
from gutils.services.spreadsheets.v4.objects.cells import CellFormat
from gutils.services.spreadsheets.v4.objects.sheets import Sheet
from gutils.services.spreadsheets.v4.objects.developer_metadata import DeveloperMetadata


class RecalculationInterval(str, enum.Enum):
    RECALCULATION_INTERVAL_UNSPECIFIED = "RECALCULATION_INTERVAL_UNSPECIFIED"
    ON_CHANGE = "ON_CHANGE"
    MINUTE = "MINUTE"
    HOUR = "HOUR"

class DataSourceRefreshScope(str, enum.Enum):
    DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED = "DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED"
    ALL_DATA_SOURCES = "ALL_DATA_SOURCES"

class DayOfWeek(str, enum.Enum):
    DAY_OF_WEEK_UNSPECIFIED = "DAY_OF_WEEK_UNSPECIFIED"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

class IterativeCalculationSettings(BaseModel):
    maxIterations: int
    convergenceThreshold: float

class ThemeColorPair(BaseModel):
    colorType: ThemeColorType
    color: ColorStyle

class SpreadsheetTheme(BaseModel):
    primaryFontFamily: str
    themeColors: typing.List[ThemeColorPair]

class SpreadsheetProperties(BaseModel):
  title: str
  locale: str = None
  autoRecalc: RecalculationInterval = None
  timeZone: str = None
  defaultFormat: CellFormat = None
  iterativeCalculationSettings: IterativeCalculationSettings = None
  spreadsheetTheme: SpreadsheetTheme = None


class NamedRange(BaseModel):
    namedRangeId: str
    name: str
    range: GridRange

class BigQueryQuerySpec(BaseModel):
    rawQuery: str

class BigQueryTableSpec(BaseModel):
    tableProjectId: str
    tableId: str
    datasetId: str
    
class BigQueryDataSourceSpec(BaseModel):
    projectId: str
    querySpec: BigQueryQuerySpec
    tableSpec: BigQueryTableSpec

class DataSourceParameter(BaseModel):
    name: str
    namedRangeId: str
    range: GridRange

class DataSourceSpec(BaseModel):
    parameters: typing.List[DataSourceParameter]
    bigQuery: BigQueryDataSourceSpec
    
class DataSource(BaseModel):
    dataSourceId: str
    spec: DataSourceSpec
    calculatedColumns: DataSourceColumn
    sheetId: int

class TimeOfDay(BaseModel):
    hours: int
    minutes: int
    seconds: int
    nanos: int
class DataSourceRefreshDailySchedule(BaseModel):
    startTime: TimeOfDay

class DataSourceRefreshWeeklySchedule(BaseModel):
    startTime: TimeOfDay
    daysOfWeek: DayOfWeek

class DataSourceRefreshMonthlySchedule(BaseModel):
    startTime: TimeOfDay
    daysOfMonth: int = Field(le=28, ge=1)

class Interval(BaseModel):
    startTime: datetime
    endTime: datetime

class DataSourceRefreshSchedule(BaseModel):
    enabled: bool
    refreshScope: DataSourceRefreshScope
    nextRun: Interval
    dailySchedule: DataSourceRefreshDailySchedule = None
    weeklySchedule: DataSourceRefreshWeeklySchedule = None
    monthlySchedule: DataSourceRefreshMonthlySchedule = None

class Spreadsheet(BaseModel):
    spreadsheetId: str = None
    properties: SpreadsheetProperties
    sheets: typing.List[Sheet] = None
    namedRanges: typing.List[NamedRange] = None
    spreadsheetUrl: str = None
    developerMetadata: typing.List[DeveloperMetadata] = None
    dataSources: typing.List[DataSource] = None
    dataSourceSchedules: typing.List[DataSourceRefreshSchedule] = None
