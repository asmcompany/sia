import os

def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_upload_path(instance, filepath):
    
    filename, ext = get_name_ext(filepath)

    final = f"id={instance.id}//{filename}{ext}"
    return f"products/{instance.title}/{final}"
