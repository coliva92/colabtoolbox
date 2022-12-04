# Prompts the user to upload a file from her local filesystem.
# Returns a dictionary with a single entry which key's the filename and value's 
# the file contents.
# 
# Two small buttons will be displayed on screen: a "Choose Files" button and 
# a "Cancel" button. 
# Clicking the "Choose Files" button opens a window instance of the local 
# file explorer. 
# Cell execution is paused until either the file is uploaded or 
# the "Cancel upload" button is clicked.
def upload_and_open_file() -> dict:
  from google.colab import files
  return files.upload()



# Compresses the especified folder and downloads it to the local filesystem.
# Any pre-existing zip folders which have the same name as the resulting zipped
# folder will be overwritten. 
def zip_and_download_folder(folder: str):
  import os
  from google.colab import files
  zip_filename = f'{folder}.zip'
  %shell zip -q -r $zip_filename $folder
  files.download(zip_filename)
