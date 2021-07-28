from django.db import models

# search tool for stacking querrysets
from django.db.models import Q


class ProductManager(models.Manager):
    
    def get_by_id(self, id):
        item = self.get_queryset().filter(id=id)
        return item.first()

    def get_active_by_id(self, id, title):
        nonSlug = title.replace('-', ' ')
        item = self.get_queryset().filter(id=id, active=True, title=nonSlug)
        
        return item.first()

    def get_all_active(self):
        return self.get_queryset().filter(active=True)


    def search(self, querry):

        condition =  Q(title__icontains=str(querry)) |  Q(caption=str(querry)) | Q(tag__title__iexact=str(querry)) | Q(category__title__icontains=str(querry)) ;

        return self.get_queryset().filter(condition, active=True).distinct()

    
    