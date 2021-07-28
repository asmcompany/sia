import os
from random import randint
def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_upload_path(instance, filepath):
    
    filename, ext = get_name_ext(filepath)

    return f"blog/{instance.title}/{randint(100000000, 9999999999999)}{ext}"
