from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive_obj = GoogleDrive(gauth)
    return drive_obj

def deleting_file(file_name, drive):
    file_list = drive.ListFile({'q': f"title = '{file_name}' and trashed=false"}).GetList()

    if len(file_list) != 0:
    # if the file exists already, delete the file
        old_file_id = file_list[0]['id']
        old_file = drive.CreateFile({'id': old_file_id})
        old_file.Delete()

def uploading_file(resume_path, file_name, drive):
    # Creating instance
    upload_resume = drive.CreateFile({'title': f'{file_name}'})  # Set the desired title for the uploaded file

    # Set the content of the file from given path
    upload_resume.SetContentFile(resume_path)

    # Upload the file
    upload_resume.Upload()

    # updating the file permissions
    upload_resume.InsertPermission({
        'type': 'anyone',  # "anyone" means anyone with the link
        'value': 'anyoneWithLink',  # Share with anyone who has the link
        'role': 'reader'  # Set the role to "reader" (can view)
    })

    return upload_resume


def main():
    drive = authenticate()

    # Deleting the old Resume from my Drive
    file_name = "Resume_Jaspreet_Singh_Dhami.pdf"  # Change this to your file name
    deleting_file(file_name,drive)

    # new_resume_path
    resume_path = f"../Final_Job_Search/{file_name}"
    resume = uploading_file(resume_path, file_name, drive)

    url = f"https://drive.google.com/uc?export=download&id={resume['id']}"

    print(f"paste this link in the button:\n{url}")

main()