# Compresses the especified folder and downloads it to the local filesystem.
# Any pre-existing zip folders which have the same name as the resulting zipped
# folder will be overwritten. 
def zip_and_download_folder(folder: str) -> str:
  import os
  from google.colab import files
  zip_folder = f'{folder}.zip'
  os.system(f'zip -q -r {zip_folder} {folder}')
  files.download(zip_folder)
  return zip_folder
