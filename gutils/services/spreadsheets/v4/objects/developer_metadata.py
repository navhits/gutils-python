import enum
import typing


from pydantic import BaseModel

from gutils.services.spreadsheets.v4.objects.general import *


class DeveloperMetadataLocationType(str, enum.Enum):
    DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED = "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED"
    ROW = "ROW"
    COLUMN = "COLUMN"
    SHEET = "SHEET"
    SPREADSHEET = "SPREADSHEET"

class DeveloperMetadataVisibility(str, enum.Enum):
    DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED = "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED"
    DOCUMENT = "DOCUMENT"
    PROJECT = "PROJECT"

class DeveloperMetadataLocation(BaseModel):
    locationType: DeveloperMetadataLocationType
    spreadsheet: bool
    sheetId: str
    dimensionRange: DimensionRange

class DeveloperMetadata(BaseModel):
    metadataId: str
    metadataKey: str
    metadataValue: str
    location: DeveloperMetadataLocation
    visibility: DeveloperMetadataVisibility
