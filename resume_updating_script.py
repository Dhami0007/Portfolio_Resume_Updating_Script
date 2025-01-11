from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from datetime import datetime

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

def check_last_update(file_path):
    log_file_name = "resume_upload_logs.txt"
    log_file = open(log_file_name, "r+")
    content = log_file.readlines()
    update_date = os.path.getmtime(file_path)
    update_date = datetime.fromtimestamp(update_date).strftime('%Y-%m-%d %H:%M:%S')

    if len(content) == 0:
        log_file.write(f"{update_date};")
        log_file.close()
        return True
    
    else:
        last_update = content[-1]
        if last_update != update_date:
            print("File has been updated since last update")
            log_file.write(f"{update_date}  link: ")
            log_file.close()
            return True
        else:
            log_file.close()
            return False

def add_link_to_log(link):
    file = open("resume_upload_logs.txt", "a")
    file.write(f"{link}\n")
    file.close()

def main():
    drive = authenticate()
    file_name = "Resume_Jaspreet_Singh_Dhami.pdf"  # Change this to your file name
    resume_path = f"../Final_Job_Search/{file_name}"

    # Checking if the file has been updated since last update
    updated = check_last_update(resume_path)

    if updated:
        # Deleting the old Resume from my Drive
        deleting_file(file_name,drive)

        # new_resume_path
        resume = uploading_file(resume_path, file_name, drive)

        url = f"https://drive.google.com/uc?export=download&id={resume['id']}"

        print(f"paste this link in the button:\n{url}")
        add_link_to_log(url)
    
    else:
        print("File has not been updated since last update")

main()