from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length =50)

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads/')
    description = models.TextField()
    image_location = models.ForeignKey('Location')
    image_category = models.ForeignKey('Category')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,image_id):
        image = cls.objects.filter(image_id= id).all()
        return image

    # @classmethod
    # def search_by_category(cls,search_term):
    #     image = cls.objects.filter(title__icontains=search_term)
    #     return image

    @classmethod
    def search_by_category(cls,category):
        images = cls.objects.filter(image_category__category_name__icontains=category).all()
        return images


    @classmethod
    def get_image_by_location(cls,location):
        images = cls.objects.filter(image_location__location_name__icontains=location).all()
        return images

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
