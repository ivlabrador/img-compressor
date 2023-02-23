from pickletools import optimize
from PIL import Image
from sys import path
import os

class Conventer:
    dir_path = str
    download_path = str #"/Users/PC/Downloads/"
    def __init__(self, dir_path, download_path):
        self.dir_path = dir_path
        self.download_path = download_path


    def convert(self):
        if os.path.exists(self.dir_path):
            directory = os.listdir(self.dir_path)
            for filename in directory:
                name, extension = os.path.splitext(self.dir_path + filename)
                print(self.download_path)
                if extension in [".jpg", ".png", ".jpeg", ".JPG"]:
                    picture = Image.open(self.dir_path+"/"+filename)
                    picture.save(self.download_path + "compressed"+filename, optimize=True, quality=60)




    for p in path:
        print(p)
    """
    for filname in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filname)
        if extension in [".jpg", ".jpeg", ".png", ".JPG"]:
            picture = Image.open(downloadsFolder + filname)
            picture.save(downloadsFolder + "compressed"+filname, optimize=True, quality=60)
    """