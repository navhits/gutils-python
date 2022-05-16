"""
All global enums goes here.
"""
import enum

class LoginType(str, enum.Enum):
    """
    Enum for the login types.
    """
    SERVICE_ACCOUNT = "SERVICE_ACCOUNT"
    OAUTH2 = "OAUTH2"

class MimeType(str, enum.Enum):
    """
    Common Mime types including Google Drive and Google Workspace.
    """
    APPLICATION_ = "application/"
    IMAGE_ = "image/"
    VIDEO_ = "video/"
    AUDIO_ = "audio/"
    TEXT_ = "text/"
    APPLICATION_GAUDIO = "application/vnd.google-apps.audio"
    APPLICATION_GDOCS = "application/vnd.google-apps.document"
    APPLICATION_3RD_PARTY_SHORTCUT = "application/vnd.google-apps.drive-sdk"
    APPLICATION_GDRAWING = "application/vnd.google-apps.drawing"
    APPLICATION_GDRIVE_FILE = "application/vnd.google-apps.file"
    APPLICATION_GDRIVE_FOLDER = "application/vnd.google-apps.folder"
    APPLICATION_GFORM = "application/vnd.google-apps.form"
    APPLICATION_GFUSION_TABLES = "application/vnd.google-apps.fusiontable"
    APPLICATION_GMAP = "application/vnd.google-apps.map"
    APPLICATION_GPHOTOS = "application/vnd.google-apps.photo"
    APPLICATION_GSLIDES = "application/vnd.google-apps.presentation"
    APPLICATION_GAPP_SCRIPT = "application/vnd.google-apps.script"
    APPLICATION_GDRIVE_SHORTCUT = "application/vnd.google-apps.shortcut"
    APPLICATION_GSITE = "application/vnd.google-apps.site"
    APPLICATION_GSHEETS = "application/vnd.google-apps.spreadsheet"
    APPLICATION_UNKNOWN = "application/vnd.google-apps.unknown"
    APPLICATION_GVIDEO = "application/vnd.google-apps.video"
    APPLICATION_BINARY = "application/octet-stream"
    APPLICATION_JS = "application/javascript"
    APPLICATION_PDF = "application/pdf"
    APPLICATION_RTF = "application/rtf"
    APPLICATION_DOC = "application/msword"
    APPLICATION_DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    APPLICATION_XLS = "application/vnd.ms-excel"
    APPLICATION_XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    APPLICATION_PPT = "application/vnd.ms-powerpoint"
    APPLICATION_PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    APPLICATION_ZIP = "application/zip"
    APPLICATION_XML = "application/xml"
    APPLICATION_TAR = "application/x-tar"
    APPLICATION_JAR = "application/java-archive"
    APPLICATION_SQLITE = "application/x-sqlite3"
    APPLICATION_GZIP = "application/x-gzip"
    IMAGE_SVG = "image/svg+xml"
    IMAGE_GIF = "image/gif"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    VIDEO_AVI = "video/avi"
    VIDEO_MP4 = "video/mp4"
    VIDEO_MPEG = "video/mpeg"
    AUDIO_MP3 = "audio/mp3"
    AUDIO_WAV = "audio/wav"
    AUDIO_MP4 = "audio/mp4"
    AUDIO_M4A = "audio/x-m4a"
    TEXT_CSV = "text/csv"
    TEXT_HTML = "text/html"
    TEXT_CSS = "text/css"
    TEXT_PLAIN = "text/plain"
    TEXT_TSV = "text/tab-separated-values"

class Operator(str, enum.Enum):
    """
    Enum for the query operations.
    """
    EQUALS = "="
    NOT_EQUALS = "!="
    CONTAINS = "contains"
    NOT = "not"
    IN = "in"
    AND = "and"
    OR = "or"
    HAS = "has"
    LESS_THAN = "<"
    LESS_THAN_EQUALS = "<="
    GREATER_THAN = ">"
    GREATER_THAN_EQUALS = ">="

class QueryFields(str, enum.Enum):
    """
    Enum for the query fields.
    """
    NAME = "name"
    FULLTEXT = "fullText"
    MIME_TYPE = "mimeType"
    MODIFIED_TIME = "modifiedTime"
    VIEWED_BY_ME_TIME = "viewedByMeTime"
    TRASHED = "trashed"
    STARRED = "starred"
    PARENTS = "parents"
    OWNERS = "owners"
    WRITERS = "writers"
    READERS = "readers"
    SHARED_WITH_ME = "sharedWithMe"
    MODIFIED_BY_ME_TIME = "modifiedByMeTime"
    LAST_VIEWED_TIME = "lastViewedByMeTime"
    SHARED_WITH_ME_TIME = "sharedWithMeTime"
    CREATED_TIME = "createdTime"
    PROPERTIES = "properties"
    APP_PROPERTIES = "appProperties"
    VISIBILITY = "visibility"
    MIME_TYPE_LABEL = "mimeTypeLabel"
    SHORTCUT_DETAILS_TARGET_ID = "shortcutDetails.targetId"
    HIDDEN = "hidden"
    MEMBER_COUNT = "memberCount"
    ORGANIZER_COUNT = "organizerCount"
