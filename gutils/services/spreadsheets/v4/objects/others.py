import typing

from pydantic import BaseModel

from gutils.services.spreadsheets.v4.types import (DataFilter, ValueInputOption, ValueRenderOption, DateTimeRenderOption)
                                                   
from gutils.services.spreadsheets.v4.objects.developer_metadata import DeveloperMetadata
from gutils.services.spreadsheets.v4.objects.general import Dimension


class DataFilters(BaseModel):
    dataFilters: typing.List[DataFilter]

class MatchedDeveloperMetadata(BaseModel):
    developerMetadata: DeveloperMetadata
    dataFilters: typing.List[DataFilter]

class ValueRange(BaseModel):
    values: list

class DataFilterValueRange(BaseModel):
    dataFilter: DataFilter
    majorDimension: Dimension
    values: list

class MatchedValueRange(BaseModel):
    valueRange: ValueRange
    dataFilters: typing.List[DataFilter]

class GetByDataFiltersRequest(BaseModel):
    dataFilters: typing.List[DataFilter]
    includeGridData: bool = False

class UpdateValuesResponse(BaseModel):
    spreadsheetId: str
    updatedRange: str
    updatedRows: str
    updatedColumns: str
    updatedCells: int
    updatedData: typing.Optional[ValueRange] = None

class UpdateValuesByDataFilterResponse(BaseModel):
    updatedRange: str
    updatedRows: str
    updatedColumns: str
    updatedCells: int
    dataFilter: DataFilter
    updatedData: ValueRange

class AppendValueResponse(BaseModel):
    spreadsheetId: str
    tableRange: str
    updates: UpdateValuesResponse

class ClearValuesResponse(BaseModel):
    spreadsheetId: str
    clearedRange: str

class BatchClearValuesRequest(BaseModel):
    ranges: typing.List[str]

class BatchClearValuesResponse(BaseModel):
    spreadsheetId: str
    clearedRanges: typing.List[str]

class BatchGetValuesResponse(BaseModel):
    spreadsheetId: str
    valueRanges: typing.List[ValueRange]

class BatchGetValuesByDataFilterRequest(BaseModel):
    dataFilters: typing.List[DataFilter]
    majorDimension: Dimension
    valueRenderOption: ValueRenderOption
    dateTimeRenderOption: DateTimeRenderOption

class BatchGetValuesByDataFilterResponse(BaseModel):
    spreadsheetId: str
    valueRanges: typing.List[MatchedValueRange]

class BatchUpdateValuesRequest(BaseModel):
    valueInputOption: ValueInputOption
    data: typing.List[ValueRange]
    includeValuesInResponse: bool
    responseValueRenderOption: ValueRenderOption
    responseDateTimeRenderOption: DateTimeRenderOption

class BatchUpdateValuesResponse(BaseModel):
    spreadsheetId: str
    totalUpdatedRows: int
    totalUpdatedColumns: int
    totalUpdatedCells: int
    totalUpdatedSheets: int
    responses: typing.List[UpdateValuesResponse]

class BatchUpdateValuesByDataFilterRequest(BaseModel):
    valueInputOption: ValueInputOption
    data: typing.List[DataFilterValueRange]
    includeValuesInResponse: bool
    responseValueRenderOption: ValueRenderOption
    responseDateTimeRenderOption: DateTimeRenderOption

class BatchUpdateValuesByDataFilterResponse(BaseModel):
    spreadsheetId: str
    totalUpdatedRows: int
    totalUpdatedColumns: int
    totalUpdatedCells: int
    totalUpdatedSheets: int
