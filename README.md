# Portfolio Resume Update helper

## Problem:
Whenever I updated my resume for the better, I would have to follow the following steps to update that resume on project portfolio website:
1. Delete the Old Resume in my Google Drive
2. Upload the New Resume in my Google Drive
3. Change the share access of the new resume to public
4. Fetch the ID of the new resume from the url
5. Update the download link in my portfolio button for the new resume

This was a long process.


## Solution:
I created Google Drive API Project in Google Cloud, and developed a python script using pydrive which will follow all the process and generate the final downloading URL, which I just have to paste in my portfolio button link.
I have also added a log file, which will keep track of the latest resume on my google account. This way, the script will not go forward to perform the operations required if my Google Drive already has the most recent version of my resume.

## Tools Used:
1. Google Cloud
2. Google Drive API Project
3. OAuth credential
4. PyDrive

