from django.db import models

# imports from my apps
from VEGAN_API.VEGAN_API_PRODUCT.models import  Product
from .upload import media_product_gallery_upload_path

# a gallery class for adding additional images for a product
class ProductGallery(models.Model):
    
    title   = models.CharField(max_length=50)
    pic     = models.ImageField(upload_to=media_product_gallery_upload_path, null=True, blank=False,verbose_name='عکس')    
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.product.__str__()}"

    class Meta:
        app_label = 'VEGAN_API_PRODUCT'
        default_related_name = 'gallery'