'''
Created on Oct 7, 2023

@author: Wesley
'''
import os
from PIL import Image



def obfuscation(files):
    for file_path in files:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".tiff", ".bmp")):
            def black_image(file_path):
                image = Image.open(file_path)
                width, height = image.size
                for x in range(width):
                    for y in range(height):
                        image.putpixel((x, y), (0, 0, 0))
                image.save(file_path)
            black_image(file_path)
            os.remove(file_path)
            print(f"File {file_path} deleted successfully")
            
        elif file_path.lower().endswith((".mp4", ".mov", ".wmv", ".webm")):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully")
            
        elif file_path.lower().endswith((".wav", ".mp3")):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully")
            
        elif file_path.lower().endswith((".txt", ".docx", ".doc", ".pdf")):
            new_text = "Hello World!"
            with open(file_path, "w") as file:
                file.write(new_text * 10000)
            os.remove(file_path)
            print(f"File {file_path} deleted successfully")
                     
        else:
            print(f"{file_path} not supported")