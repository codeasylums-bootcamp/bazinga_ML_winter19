from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

path_to_file=input("Enter file path")
with open("path_to_file","r") as file:
    file_drive = drive.CreateFile({'title':os.path.basename(file.name) })  
    file_drive.SetContentString(file.read()) 
    file_drive.Upload()


