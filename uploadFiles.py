from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx= dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='VjhioScEVRgAAAAAAAAAAf2kL-cgugCMD9sUbqyADv1np6gp2RHREvMjs6fXOs85'
    transferData=TransferData(access_token)
    file_from=input("Enter the file path to transport")
    file_to=input("Enter the full path to upload on dropbox")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()