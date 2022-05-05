from ..api_client import GoogleApiClient
from .enums import *
from ..enums import *


class Sheets(GoogleApiClient):
    
    resource_name = "sheets"
    version = "v4"
    
    def initialize(self):
        if self.login_type == LoginType.OAUTH2:
            self.oauth2_login()
        elif self.login_type == LoginType.SERVICE_ACCOUNT:
            self.service_account_auth()
        self.set_service(self.resource_name, self.version)

    def create(self, title: str = None) -> dict:
        """
        Creates a new Google Sheet with the given title.
        """
        title = title if title else 'Sheet created by Google API client'
        return self.service.spreadsheets().create(body={'properties': {'title': title}}).execute()

    def read(self, sheet_id: str, sheet_range: str = "Sheet1",
                dimension: MajorDimension = MajorDimension.ROWS,
                value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
                datetime_render_option: DateTimeRenderOption = DateTimeRenderOption.FORMATTED_STRING) -> list:
        """
        Reads a given range of data from a Google Sheet.
        """
        return self.service.spreadsheets().values().get(spreadsheetId=sheet_id,
                                range=sheet_range, majorDimension=dimension.value,
                                valueRenderOption=value_render_option.value,
                                dateTimeRenderOption=datetime_render_option.value).execute().get('values', [])
    
    def update(self, sheet_id: str, values: list = None, sheet_range: str = "Sheet1",
            dimension: MajorDimension = MajorDimension.ROWS,
            input_option: ValueInputOption = ValueInputOption.RAW,
            response_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
            response_datetime_render_option: DateTimeRenderOption = DateTimeRenderOption.FORMATTED_STRING) -> dict:
        """
        Writes or updates a given range of data to a Google Sheet.
        """
        body = {
            "majorDimension": dimension.value,
            "values": values if values else []
        }
        return self.service.spreadsheets().values().update(spreadsheetId=sheet_id, 
                                    range=sheet_range, valueInputOption=input_option.value, 
                                    responseValueRenderOption=response_render_option.value,
                                    responseDateTimeRenderOption=response_datetime_render_option.value,
                                    body=body).execute()

    def append(self, sheet_id: str, values: list = None, sheet_range: str = None,
            input_option: ValueInputOption = ValueInputOption.RAW,
            insert_data_option: InsertDataOption = InsertDataOption.OVERWRITE,
            response_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE,
            response_datetime_render_option: DateTimeRenderOption = DateTimeRenderOption.FORMATTED_STRING) -> dict:
        """
        Appends a given list of values to a Google Sheet.
        """
        body = {
            'values': values
        }
        return self.service.spreadsheets().values().append(spreadsheetId=sheet_id,
                                    range=sheet_range, valueInputOption=input_option.value,
                                    insertDataOption=insert_data_option.value,
                                    responseValueRenderOption=response_render_option.value,
                                    responseDateTimeRenderOption=response_datetime_render_option.value,
                                    body=body).execute()
