"""
Enums for the sheets service.
"""
import enum

from pydantic import BaseModel

from gutils.services.spreadsheets.v4.objects.developer_metadata import (DeveloperMetadataLocationType,
                                                                     DeveloperMetadataLocation,
                                                                     DeveloperMetadataVisibility)
from gutils.services.spreadsheets.v4.objects.general import GridRange

class ErrorCode(str, enum.Enum):
    ERROR_CODE_UNSPECIFIED = "ERROR_CODE_UNSPECIFIED"
    DOCUMENT_TOO_LARGE_TO_EDIT = "DOCUMENT_TOO_LARGE_TO_EDIT"
    DOCUMENT_TOO_LARGE_TO_LOAD = "DOCUMENT_TOO_LARGE_TO_LOAD"
    
class ValueInputOption(str, enum.Enum):
    """
    Enum for the value input options.
    """
    RAW = "RAW"
    USER_ENTERED = "USER_ENTERED"

class InsertDataOption(str, enum.Enum):
    """
    Enum for the insert data options.
    """
    OVERWRITE = "OVERWRITE"
    INSERT_ROWS = "INSERT_ROWS"

class ValueRenderOption(str, enum.Enum):
    """
    Enum for the value render options.
    """
    FORMATTED_VALUE = "FORMATTED_VALUE"
    UNFORMATTED_VALUE = "UNFORMATTED_VALUE"
    FORMULA = "FORMULA"

class DateTimeRenderOption(str, enum.Enum):
    """
    Enum for the date time render options.
    """
    SERIAL_NUMBER = "SERIAL_NUMBER"
    FORMATTED_STRING = "FORMATTED_STRING"

class DeveloperMetadataLocationMatchingStrategy(str, enum.Enum):
    DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED = "DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED"
    EXACT_LOCATION = "EXACT_LOCATION"
    INTERSECTING_LOCATION = "INTERSECTING_LOCATION"

class DeveloperMetadataLookup(BaseModel):
    locationType: DeveloperMetadataLocationType
    metadataLocation: DeveloperMetadataLocation
    locationMatchingStrategy: DeveloperMetadataLocationMatchingStrategy
    metadataId: int
    metadataKey: str
    metadataValue: str
    visibility: DeveloperMetadataVisibility

class DataFilter(BaseModel):
    developerMetadataLookup: DeveloperMetadataLookup
    a1Range: str
    gridRange: GridRange
    
class ErrorDetails(BaseModel):
    errorDetails = ErrorCode
