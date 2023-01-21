# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from gutils.services.sheets.v4.objects.others import *
from gutils.services.sheets.v4.objects.spreadsheets import Spreadsheet
from gutils.services.sheets.v4.types import *
from gutils.services.sheets.v4.spreadsheets.developer_metadata import DeveloperMetadata
from gutils.services.sheets.v4.spreadsheets.sheets import Sheets
from gutils.services.sheets.v4.spreadsheets.values import Values



# pylint: disable=line-too-long
# pylint: disable=no-member
class Spreadsheets:
    """
    This class adds access to API resources under `spreadsheets`
    """
    service_name = "sheets"
    resource_name = "spreadsheets"
    version = "v4"

    def __init__(self, service: object) -> None:
        self.service = service

    @property
    def developer_metadata(self) -> DeveloperMetadata:
        return DeveloperMetadata(self.service)

    @property
    def sheets(self) -> Sheets:
        return Sheets(self.service)

    @property
    def values(self) -> Values:
        return Values(self.values)

    def create(self, body: Spreadsheet) -> Spreadsheet:
        """
        Creates a new Google Sheet with the given title.
        """
        response = self.service.spreadsheets().create(body=body.dict()).execute()
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
