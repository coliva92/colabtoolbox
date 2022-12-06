from typing import Optional
from pydrive.drive import GoogleDrive





# Establishes a connection to Google Drive using PyDrive.
# Returns an instance of `pydrive.drive.GoogleDrive` for further interaction 
# with the Google Drive API.
#
# See:
# - https://pythonhosted.org/PyDrive/index.html
# - https://developers.google.com/drive/api/v3/reference
def sign_in_to_google_drive() -> Optional[GoogleDrive]:
  from pydrive.auth import GoogleAuth
  from google.colab import auth
  from oauth2client.client import GoogleCredentials
  auth.authenticate_user()
  gauth = GoogleAuth()
  gauth.credentials = GoogleCredentials.get_application_default()
  return GoogleDrive(gauth)



# Saves the especified file to an already signed-in Google Drive.
# Returns the ID assigned to the uploaded file. This ID can then be used to
# query the Google Drive API. 
#
# See: 
# - https://pythonhosted.org/PyDrive/filemanagement.html#upload-and-update-file-content
# - https://developers.google.com/drive/api/v3/reference#Files
# - https://developers.google.com/drive/api/v3/reference/files#resource
def upload_to_google_drive(drive: GoogleDrive, 
                           filename: str,
                           parentId: Optional[str] = None) -> str:
  metadata = { 'title': filename }
  if parentId is not None:
    metadata['parents'] = [{ 
      'id': parentId,
      'kind': 'drive#fileLink'
    }]
  file = drive.CreateFile(metadata)
  file.SetContentFile(filename)
  file.Upload()
  return file.get('id')



# Downloads from Google Drive a copy of the file with the especified ID and 
# stores it in the current virtual filesystem. It does not download the file to
# the user's local filesystem. The stored file is renamed to the especified 
# filename.
#
# See: https://pythonhosted.org/PyDrive/filemanagement.html#download-file-content
def download_from_google_drive(drive: GoogleDrive,
                               fileId: str,
                               filename: str):
  file = drive.CreateFile({ 'id': fileId })
  file.GetContentFile(filename)



# Updates the contents of the file with the especified ID with the contents
# of the local file with the especified filename.
def update_in_google_drive(drive: GoogleDrive, 
                           fileId: str,
                           filename: str):
  file = drive.CreateFile({ 'id': fileId })
  file.SetContentFile(filename)
  file.Upload()



# Creates a new folder in Google Drive with the especified name.
# Returns the assigned ID of the created folder. 
def create_folder_in_google_drive(drive: GoogleDrive, 
                                  name: str, 
                                  parentId: Optional[str] = None) -> str:
  metadata = {
    'title': name,
    'mimeType': 'application/vnd.google-apps.folder'
  }
  if parentId is not None:
    metadata['parents'] = [{ 
      'id': parentId,
      'kind': 'drive#fileLink'
    }]
  folder = drive.CreateFile(metadata)
  folder.Upload()
  return folder.get('id')
