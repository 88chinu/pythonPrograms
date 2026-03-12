# file organizer automation

import os
import shutil

def folderPath(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    shutil.move(src, dst)

def main():
    path = input("Enter the file path : ")
    if not os.path.exists(path):
        print("\nFile Not Found")
        return
    for f in os.listdir(path):
        fp = os.path.join(path, f)

        if os.path.isfile(fp):
            extension  = os.path.splitext(fp)[1].lower()
            if extension in[".jpg", ".jpeg", ".png"]:
                d = os.path.join(path,"images")
                folderPath(fp, d)

            elif extension in [".pdf", ".txt", ".docx"]:
                d = os.path.join(path,"documents")
                folderPath(fp, d)

            elif extension in [".csv", ".xlsx"]:
                d = os.path.join(path,"data files")
                folderPath(fp, d)

            elif extension in [".py", ".c", ".java"]:
                d = os.path.join(path,"programming code")
                folderPath(fp, d)

            else:
                d = os.path.join(path,"others")
                folderPath(fp, d)
    print("\nFolder organize Successfully!")

main()
