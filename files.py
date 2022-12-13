# Compresses the especified folder and downloads it to the local filesystem.
# Any pre-existing zip folders which have the same name as the resulting zipped
# folder will be overwritten. 
def zip_and_download_folder(folder: str) -> str:
  import os
  from google.colab import files
  zip_filename = f'{folder}.zip'
  os.system(f'zip -q -r {zip_filename} {folder}')
  files.download(zip_filename)
  return zip_filename
