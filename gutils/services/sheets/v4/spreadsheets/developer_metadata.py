# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from gutils.services.sheets.v4.objects.developer_metadata import \
    DeveloperMetadata
from gutils.services.sheets.v4.objects.others import *

# pylint: disable=line-too-long
# pylint: disable=no-member
class DeveloperMetadata:
    """
    This class adds access to API resources under `spreadsheets.developerMetadata`
    """
    service_name = "sheets"
    resource_name = "spreadsheets.developerMetadata"
    version = "v4"

    def __init__(self, service: object) -> None:
        self.service = service

    def get_developer_metadata(self, spreadsheet_id: str, metadata_id: str) -> DeveloperMetadata:
        response = self.service.spreadsheets().developerMetadata().get(
            spreadsheetId=spreadsheet_id, metadataId=metadata_id).execute()
        return DeveloperMetadata(**response)

    def search_developer_metadata(self, spreadsheet_id: str, body: DataFilters) -> MatchedDeveloperMetadata:
        """
        Retrivies all developer meta data matching the Data Filter
        """
        response = self.service.spreadsheets().developerMetadata().search(
            spreadsheetId=spreadsheet_id, body=body.dict()).execute()
        return MatchedDeveloperMetadata(**response)
