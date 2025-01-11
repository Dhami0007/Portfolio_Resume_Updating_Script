from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return gauth

drive = GoogleDrive(authenticate())

# Deleting the old Resume from my Drive
file_name = "Resume_Jaspreet_Singh_Dhami.pdf"  # Change this to your file name
file_list = drive.ListFile({'q': f"title = '{file_name}' and trashed=false"}).GetList()

if len(file_list) != 0:
# if the file exists already, delete the file
    old_file_id = file_list[0]['id']
    old_file = drive.CreateFile({'id': old_file_id})
    old_file.Delete()

# Upload the new Resume to my Drive
resume_path = f"../Final_Job_Search/{file_name}"

# Creating instance
upload_resume = drive.CreateFile({'title': f'{file_name}'})  # Set the desired title for the uploaded file

# Set the content of the file from given path
upload_resume.SetContentFile(resume_path)

# Upload the file
upload_resume.Upload()

print(f"File {file_name} uploaded successfully!")