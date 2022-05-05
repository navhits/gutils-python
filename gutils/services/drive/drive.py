import io, shutil
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from .query import Query
from ..api_client import GoogleApiClient
from ..enums import *

class Drive(GoogleApiClient):
    
    resource_name = "drive"
    version = "v3"
    
    def initialize(self):
        if self.login_type == LoginType.OAUTH2:
            self.oauth2_login()
        elif self.login_type == LoginType.SERVICE_ACCOUNT:
            self.service_account_auth()
        self.set_service(self.resource_name, self.version)
    
    def list_drives(self) -> list:
        """
        Returns a list of all drive resources.
        """
        drives = list()
        page_token = None
        while True:
            response = self.service.drives().list(fields='nextPageToken, drives(id, name)',
                                                    pageSize=100, pageToken=page_token).execute()
            
            for drive in response.get('drives', []):
                drives.append(drive)
            page_token = response.get('nextPageToken', None)
            
            if page_token is None:
                break
        return drives
    
    def upload(self, title: str = None, filename: str = None, input_mime_type: str = None,
              upload_mime_type: str = None, parent_folder_id: str = None, meta_body: dict = None) -> dict:
        """
        Creates a new file with the given title in Google Drive.
        Requires service to be 'drive'
        Requires one of the folowing scopes,
        - https://www.googleapis.com/auth/drive
        - https://www.googleapis.com/auth/drive.file
        """
        if not meta_body:
            meta_body = {
                'name': title if title else filename,
                'mimeType': upload_mime_type if upload_mime_type else MimeType.APPLICATION_BINARY.value,
                'parents' : [parent_folder_id] if parent_folder_id else None
            }
            
        temp = {k: v for k, v in meta_body.items() if v is not None}
        meta_body.clear()
        meta_body.update(temp)

        media_body = MediaFileUpload(filename,
                                mimetype=input_mime_type if input_mime_type else MimeType.APPLICATION_BINARY.value)
        
        return self.service.files().create(body=meta_body, media_body=media_body).execute()

    def create_folder(self, folder_name: str, parent_folder_id: str = None, 
                            ignore_duplicates: bool = False) -> dict:
        """
        Creates a new folder in Google Drive. Optionally supports to ignore duplicate folders.
        """
        if ignore_duplicates is False:
            files = self.list_folders(folder_name)
            if files:
                # FIXME: Handle multiple duplicates here. It is highly possible that 2 folders might exist with the same name.
                return files[0]

        meta_body = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_folder_id] if parent_folder_id else None
        }

        temp = {k: v for k, v in meta_body.items() if v is not None}
        meta_body.clear()
        meta_body.update(temp)

        return self.upload()

    def get_file(self, file_id: str) -> dict:
        """
        Returns a files's metadata.
        """
        return self.service.files().get(fileId=file_id).execute()

    def list_items(self, query: Query = None, drive_id: str = None) -> list:
        """
        Returns a list of items from Google Drive based on the given query.
        """
        items = list()
        page_token = None
        corpora = None
        query = None
        
        if query:
            query = f"{query}"

        if drive_id:
            corpora = 'drive'

        while True:
            response = self.service.files().list(q=query, corpora=corpora, drive_id=drive_id, spaces='drive', 
                                                    fields='nextPageToken, files(id, name, parents)',
                                                    pageSize=1000, pageToken=page_token).execute()
            
            for file_ in response.get('files', []):
                items.append(file_)
            
            page_token = response.get('nextPageToken', None)
            
            if page_token is None:
                break
        return items

    def list_folders(self, query: Query = None, drive_id: str = None) -> list:
        """
        Returns a list of folder resources in Google Drive.
        """
        
        default_query = Query().FIELD(QueryFields.MIME_TYPE).EQUALS(MimeType.FOLDER.value)
        if query:
            query = f"{default_query} {Operator.AND} {query}"    
        else:
            query = default_query

        return self.list_items(query, drive_id)
    
    def list_files(self, query: Query = None, drive_id: str = None) -> list:
        """
        Returns a list of file resources in Google Drive.
        """
        
        default_query = Query().FIELD(QueryFields.MIME_TYPE).NOT_EQUALS.VALUE(MimeType.FOLDER.value).AND.FIELD(QueryFields.MIME_TYPE).NOT_EQUALS.VALUE(MimeType.APPLICATION_GDRIVE_SHORTCUT.value)
        if query:
            query = f"{default_query} {Operator.AND} {query}"    
        else:
            query = default_query

        return self.list_items(query, drive_id)
        
    
    def download(self, file_id: str, download_mime_type: MimeType, output_file: str = None) -> str:
        """
        Downloads a file from Google Drive.
        """
        
        if not output_file:
            output_file = self.get(file_id).get("name")

        request = self.service.files().export_media(fileId=file_id,
                                             mimeType=f'{download_mime_type}')
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        fh.seek(0)
        with open(output_file, 'wb') as f:
            shutil.copyfileobj(fh, f)

    def move_to_folder(self, file_id: str, folder_id: str):
        """
        Moves a file to a given folder in Google Drive.
        Note: All previous occurances of the same file in various parent folders will be removed.
        """
        file_ = self.service.files().get(fileId=file_id).execute()
        previous_parents = ",".join(file_.get('parents'))
        self.service.files().update(fileId=file_id,
                                    addParents=folder_id,
                                    removeParents=previous_parents).execute()

    def copy_to_folder(self, file_id: str, folder_id: str):
        """
        Copies a file to a given folder in Google Drive.
        """
        self.service.files().update(fileId=file_id,
                                    addParents=folder_id).execute()
