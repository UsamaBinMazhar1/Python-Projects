from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

fileList = drive.ListFile({'q': "'18pFZ2tcNqPxl7HILWUohQyxlb0VekLDE' in parents and trashed=false"}).GetList()
for file in fileList:
	print('Title: %s, ID: %s' % (file['title'], file['id']))
	# Get the folder ID that you want
	if (file['title'] == "marketing.db"):
		fileID = file['id']
		file2 = drive.CreateFile({'id': fileID})
		file2.Delete()

upload_file_list = ["marketing.db"]
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '18pFZ2tcNqPxl7HILWUohQyxlb0VekLDE'}]})
	gfile.SetContentFile(upload_file)
	gfile.Upload()

