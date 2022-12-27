import os
import shutil

path = "/Users/christianaltamura/Downloads"
files = os.listdir(path)
folder = path + "/" + "_OTHER"

if os.path.exists(folder):
    pass
else:
    os.makedirs(folder)

for file in files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]

    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext)

for file in files:
    docs = ['exe','rar','mp3','jpeg','accdb','xlsx','pptx','png','app','docx','jpg','zip','dmg','pdf']
    if file not in docs:
        shutil.move(path + "/" + file, folder)