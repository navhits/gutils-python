from .drive import Drive

def create_nested_drive_folders(self, drive: Drive, folder_paths: str) -> list:
    """
    Creates a new folder paths in Google Drive.
    """

    folders = list()
    folder_paths = folder_paths.split('/')
    next_parent = None
    for folder_path in folder_paths:
        f = drive.create_folder(folder_path, parent_folder_id=next_parent)
        next_parent = f.get('id')
        folders.append(f)
    return folders


def get_drive_folder_id(self, drive: Drive, folder_name: str) -> str:
    """
    Gets the folder id from the folder path.
    """
    
    pass