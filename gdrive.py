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
                         folderId: Optional[str] = None) -> str:
  config = { 'title': filename }
  if folderId is not None:
    config['parents'] = [{ 
      'id': folderId,
      'kind': 'drive#fileLink'
    }]
  uploaded = drive.CreateFile(config)
  uploaded.SetContentFile(filename)
  uploaded.Upload()
  return uploaded.get('id')



# Queries the Google Drive API in search of a file with the specified name.
# Returns the ID of the first search result or `None` if the query returned 
# no results.
#
# See:
# - https://pythonhosted.org/PyDrive/filelist.html#get-all-files-which-matches-the-query
# - https://developers.google.com/drive/api/v3/reference/files/list
# - https://developers.google.com/drive/api/guides/ref-search-terms
# - https://developers.google.com/drive/api/v3/reference/files#resource
def find_id_from_google_drive(drive: GoogleDrive, 
                              name: str) -> Optional[str]:
  query = { 'q': f"title='{name}' and trashed=false" }
  file_list = drive.ListFile(query).GetList()
  return file_list[0]['id'] if len(file_list) > 0 else None 



# Returns a string that describes the contents of the file with the especified ID,
# obtained from Google Drive.
#
# See: https://pythonhosted.org/PyDrive/filemanagement.html#download-file-content
def get_contents_from_google_drive(drive: GoogleDrive,
                                   fileId: str) -> str:
  file = drive.CreateFile({ 'id': fileId })
  return file.GetContentString()



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
def update_to_google_drive(drive: GoogleDrive, 
                           fileId: str,
                           filename: str):
  file = drive.CreateFile({ 'id': fileId })
  file.SetContentFile(filename)
  file.Upload()
  
