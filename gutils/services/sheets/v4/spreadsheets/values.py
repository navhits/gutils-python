from gutils.services.sheets.v4.objects.others import *
from gutils.services.sheets.v4.types import *

# pylint: disable=line-too-long
# pylint: disable=no-member
class Values:
    """
    This class adds access to API resources under `spreadsheets.values`
    """
    service_name = "sheets"
    resource_name = "spreadsheets.values"
    version = "v4"

    def __init__(self, service: object) -> None:
        self.service = service

    # pylint: disable=too-many-arguments
    def get(self, spreadsheet_id: str, sheet_range: str,
        dimension: Dimension = Dimension.ROWS,
        value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
        datetime_render_option: DateTimeRenderOption = DateTimeRenderOption.SERIAL_NUMBER) -> ValueRange:
        """
        Reads a given range of data from a Google Sheet.
        """
        response = self.service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                range=sheet_range, majorDimension=dimension.value,
                valueRenderOption=value_render_option.value,
                dateTimeRenderOption=datetime_render_option.value).execute()
        return ValueRange(**response)

    def update(self, spreadsheet_id: str, body: ValueRange, sheet_range: str,
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
                    body=body.dict()).execute()
        return UpdateValuesResponse(**response)

    def append(self, spreadsheet_id: str, body: ValueRange,
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
                        body=body.dict()).execute()
        return AppendValueResponse(**response)

    def clear(self, spreadsheet_id: str, sheet_range: str) -> ClearValuesResponse:
        """
        Clears a spreadsheet for the given reange.
        Clears fully if no range is given.
        """
        response = self.service.spreadsheets().values().clear(
            spreadsheetId=spreadsheet_id, range=sheet_range).execute()
        return ClearValuesResponse(**response)
        
    def batch_get(self, spreadsheet_id: str, ranges: list, 
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

    def batch_get_by_data_filter(self, spreadsheet_id: str, 
                                        body: BatchGetValuesByDataFilterRequest) -> BatchGetValuesByDataFilterRequest:
        """
        Updates a set of values for the given set of ranges
        """
        response = self.service.spreadsheets().values().batchGetByDataFilter(
            spreadsheetId=spreadsheet_id, body=body.dict()).execute()
        return BatchGetValuesByDataFilterRequest(**response)
    
    def batch_update(self, spreadsheet_id: str, body: BatchUpdateValuesRequest) -> BatchUpdateValuesResponse:
        """
        Updates a set of values for the given set of ranges
        """
        response = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body.dict()).execute()
        return BatchUpdateValuesResponse(**response)

    def batch_update_by_data_filter(self, spreadsheet_id: str,
                                body: BatchUpdateValuesByDataFilterRequest) -> BatchUpdateValuesByDataFilterResponse:
        """
        Updates a set of values for the given filter sets
        """
        response = self.service.spreadsheets().values().batchUpdateByDataFilter(
            spreadsheetId=spreadsheet_id, body=body.dict()).execute()
        return BatchUpdateValuesByDataFilterResponse(**response)

    def batch_clear(self, spreadsheet_id: str, body: BatchClearValuesRequest) -> BatchClearValuesResponse:
        """
        Clears a sheet for the given set of ranges.
        Clears fully if no range is given
        """
        response = self.service.spreadsheets().values().batchClear(
            spreadsheetId=spreadsheet_id, body=body.dict()).execute()
        return BatchClearValuesResponse(**response)

    def batch_clear_by_data_filter(self, spreadsheet_id: str, body: DataFilters) -> BatchClearValuesResponse:
        response = self.service.spreadsheets().values().batchClearByDataFilter(
            spreadsheetId=spreadsheet_id, body=body.dict())
        return BatchClearValuesResponse(**response)
