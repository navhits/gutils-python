# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from gutils.services.enums import *
from gutils.services.spreadsheets.v4.types import *
from gutils.services.spreadsheets.v4.objects.others import *
from gutils.services.spreadsheets.v4.objects.developer_metadata import DeveloperMetadata
from gutils.services.spreadsheets.v4.objects.sheets import SheetProperties
from gutils.services.spreadsheets.v4.objects.spreadsheets import Spreadsheet

# pylint: disable=line-too-long
# pylint: disable=no-member
class SpreadsheetClient:
    """
    This class adds access to API resources under `spreadsheets`
    """
    resource_name = "sheets"
    version = "v4"

    def __init__(self, service: object) -> None:
        self.service = service

    def create(self, body: Spreadsheet) -> Spreadsheet:
        """
        Creates a new Google Sheet with the given title.
        """
        response = self.service.spreadsheets().create(body=body.json()).execute()
        return Spreadsheet(**response)

    def get(self, spreadsheet_id: str, ranges: list, include_grid_data: bool = None) -> Spreadsheet:
        """
        Retrive a Google Sheet info with the Sheet ID.
        """
        response = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=ranges,
                                               includeGridData=include_grid_data).execute()
        return Spreadsheet(**response)

    def get_by_data_filter(self, spreadsheet_id: str, body: dict = None):
        """
        Retrive a Google Sheet info with the Sheet ID with options to apply filters.
        """
        return self.service.spreadsheets().getByDataFilter(spreadsheetId=spreadsheet_id, body=body).execute()

    def batch_update(self):
        """
        Applies one or more updates to the spreadsheet
        """
        #TODO: Implement this method.
        # Reference: https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate
        pass
    
    def get_developer_metadata(self, spreadsheet_id: str, metadata_id: str) -> DeveloperMetadata:
        response = self.service.spreadsheets().developerMetadata().get(
            spreadsheetId=spreadsheet_id, metadataId=metadata_id).execute()
        return DeveloperMetadata(**response)

    def search_developer_metadata(self, spreadsheet_id: str, body: DataFilters) -> MatchedDeveloperMetadata:
        """
        Retrivies all developer meta data matching the Data Filter
        """
        response = self.service.spreadsheets().developerMetadata().search(
            spreadsheetId=spreadsheet_id, body=body.json()).execute()
        return MatchedDeveloperMetadata(**response)

    def copy_to(self, spreadsheet_id: str, sheet_id: str, destination_spreadsheet_id: str) -> SheetProperties:
        body = {
            "destinationSpreadsheetId": destination_spreadsheet_id
        }
        resposne = self.service.spreadsheets().sheets().copyTo(
            spreadsheetId=spreadsheet_id, sheetId=sheet_id, body=body).execute()
        return SheetProperties(**resposne)

    # pylint: disable=too-many-arguments
    def get_values(self, spreadsheet_id: str, sheet_range: str,
        dimension: Dimension = Dimension.ROWS,
        value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
        datetime_render_option: DateTimeRenderOption = DateTimeRenderOption.SERIAL_NUMBER) -> ValueRange:
        """
        Reads a given range of data from a Google Sheet.
        """
        response = self.service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                range=sheet_range, Dimension=dimension.value,
                valueRenderOption=value_render_option.value,
                dateTimeRenderOption=datetime_render_option.value).execute()
        return ValueRange(**response)

    def update_values(self, spreadsheet_id: str, body: ValueRange, sheet_range: str,
        dimension: Dimension = Dimension.ROWS,
        input_option: ValueInputOption = ValueInputOption.RAW,
        response_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
        response_datetime_render_option: DateTimeRenderOption = DateTimeRenderOption.SERIAL_NUMBER) -> UpdateValuesResponse:
        """
        Writes or updates a given range of data to a Google Sheet.
        """
        response = self.service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                    range=sheet_range, valueInputOption=input_option.value,
                    responseValueRenderOption=response_render_option.value,
                    responseDateTimeRenderOption=response_datetime_render_option.value,
                    body=body.json()).execute()
        return UpdateValuesResponse(**response)

    def append_values(self, spreadsheet_id: str, body: ValueRange,
        input_option: ValueInputOption = ValueInputOption.RAW,
        insert_data_option: InsertDataOption = InsertDataOption.OVERWRITE,
        response_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
        response_datetime_render_option: DateTimeRenderOption = DateTimeRenderOption.SERIAL_NUMBER) -> AppendValueResponse:
        """
        Appends a given list of values to a Google Sheet.
        """
        
        response = self.service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                        valueInputOption=input_option.value,
                        insertDataOption=insert_data_option.value,
                        responseValueRenderOption=response_render_option.value,
                        responseDateTimeRenderOption=response_datetime_render_option.value,
                        body=body.json()).execute()
        return AppendValueResponse(**response)

    def clear_values(self, spreadsheet_id: str, sheet_range: str) -> ClearValuesResponse:
        """
        Clears a spreadsheet for the given reange.
        Clears fully if no range is given.
        """
        response = self.service.spreadsheets().values().clear(
            spreadsheetId=spreadsheet_id, range=sheet_range).execute()
        return ClearValuesResponse(**response)
        
    def batch_get_values(self, spreadsheet_id: str, ranges: list, 
        dimension: Dimension = Dimension.ROWS,
        date_time_render_option: DateTimeRenderOption = DateTimeRenderOption.SERIAL_NUMBER,
        value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE) -> BatchGetValuesResponse:
        """
        Reads a given set of ranges and returns the values
        """
        ranges = ",".join(ranges)
        response = self.service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, 
                    majorDimension=dimension, ranges=ranges, valueRenderOption=value_render_option, 
                    dateTimeRenderOption=date_time_render_option).execute()
        return BatchGetValuesResponse(**response)

    def batch_get_values_by_data_filter(self, spreadsheet_id: str, 
                                        body: BatchGetValuesByDataFilterRequest) -> BatchGetValuesByDataFilterRequest:
        """
        Updates a set of values for the given set of ranges
        """
        response = self.service.spreadsheets().values().batchGetByDataFilter(
            spreadsheetId=spreadsheet_id, body=body.json()).execute()
        return BatchGetValuesByDataFilterRequest(**response)
    
    def batch_update_values(self, spreadsheet_id: str, body: BatchUpdateValuesRequest) -> BatchUpdateValuesResponse:
        """
        Updates a set of values for the given set of ranges
        """
        response = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body.json()).execute()
        return BatchUpdateValuesResponse(**response)

    def batch_update_values_by_data_filter(self, spreadsheet_id: str,
                                body: BatchUpdateValuesByDataFilterRequest) -> BatchUpdateValuesByDataFilterResponse:
        """
        Updates a set of values for the given filter sets
        """
        response = self.service.spreadsheets().values().batchUpdateByDataFilter(
            spreadsheetId=spreadsheet_id, body=body.json()).execute()
        return BatchUpdateValuesByDataFilterResponse(**response)

    def batch_clear_values(self, spreadsheet_id: str, body: BatchClearValuesRequest) -> BatchClearValuesResponse:
        """
        Clears a sheet for the given set of ranges.
        Clears fully if no range is given
        """
        response = self.service.spreadsheets().values().batchClear(
            spreadsheetId=spreadsheet_id, body=body.json()).execute()
        return BatchClearValuesResponse(**response)

    def batch_clear_values_by_data_filter(self, spreadsheet_id: str, body: DataFilters) -> BatchClearValuesResponse:
        response = self.service.spreadsheets().values().batchClearByDataFilter(
            spreadsheetId=spreadsheet_id, body=body.json())
        return BatchClearValuesResponse(**response)
