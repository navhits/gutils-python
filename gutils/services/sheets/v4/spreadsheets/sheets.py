from gutils.services.sheets.v4.objects.sheets import SheetProperties

# pylint: disable=line-too-long
# pylint: disable=no-member
class Sheets:
    """
    This class adds access to API resources under `spreadsheets.sheets`
    """
    service_name = "sheets"
    resource_name = "spreadsheets.sheets"
    version = "v4"

    def __init__(self, service: object) -> None:
        self.service = service

    def copy_to(self, spreadsheet_id: str, sheet_id: str, destination_spreadsheet_id: str) -> SheetProperties:
        body = {
            "destinationSpreadsheetId": destination_spreadsheet_id
        }
        resposne = self.service.spreadsheets().sheets().copyTo(
            spreadsheetId=spreadsheet_id, sheetId=sheet_id, body=body).execute()
        return SheetProperties(**resposne)
