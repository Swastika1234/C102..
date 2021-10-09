import cv2
import dropbox
import time
import random
startTime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCapture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCapture.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    print("Snapshot has been taken")
    videoCapture.release()
    cv2.destroyAllWindows()
def uploadFile(imageName):
    access_token="sl.A6CH8bq89O4j1eYgeHtHqFirTPDwgl5eHRNpU8zt7gEwlT_mA_W8UvNUeG5BRKvue_7D1vCHBC1QU1kwzXVc-EXAKuYYhcyjm5pNUieYbgb5mUwp_UAePcXNTDuhxJKHBN-qqi0"
    file=imageName
    fileFrom=file
    file2="/testFolder/"+(imageName)
    dbx=dropbox.Dropbox(access_token)
    with open (fileFrom,'rb') as f:
        dbx.fileUpload(f.read(),file2,mode=dropbox.files.WriteMode.overwrite)
        print("File is uploaded")
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=takeSnapshot()
            uploadFile(name)
main()
            

