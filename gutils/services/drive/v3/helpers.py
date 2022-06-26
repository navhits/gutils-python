"""
Some helper functions for Google Drive that isn't part of the API functionality.
"""
from typing import Union

from gutils.services.drive.v3.drive import Drive


def create_nested_drive_folders(drive: Drive, folder_paths: str) -> list:
    """
    Creates a new folder paths in Google Drive.
    """

    folders = list()
    folder_paths = folder_paths.split('/')
    next_parent = None
    for folder_path in folder_paths:
        folder = drive.create_folder(folder_path, parent_folder_id=next_parent)
        next_parent = folder.get('id')
        folders.append(folder)
    return folders

#TODO: This method needs to be tested
def get_drive_folder_id(drive: Drive, folder_name: str) -> Union[str, None]:
    """
    Returns the id of the folder with the given name.
    """
    folders = drive.list_folders()
    if folders:
        for folder in folders:
            if folder_name == folder.get('name'):
                return folder.get('id')
    return None
