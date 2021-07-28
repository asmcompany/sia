import os
from random import randint

def media_product_gallery_upload_path(instance, filepath):
    
    def get_name_ext(filepath):
        fullName      = os.path.basename(filepath)
        filename, ext = os.path.splitext(fullName)
        return filename, ext

    filename, ext = get_name_ext(filepath)
    random_name_generated = randint(100000000, 100000000000)
    final = f"{random_name_generated}{ext}"
    return f"products/gallery/{instance.title}/{final}"
