from django.db import models
from django.urls import reverse
from image_cropping import ImageRatioField, ImageCropField


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    model = models.CharField(max_length=125, blank=True)
    description = models.CharField(max_length=500, blank=True)
    image = ImageCropField(upload_to='products/products')
    cropping = ImageRatioField('image', '270x270')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self._generate_slug()
    #
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    # def get_url(self):
    #     return reverse('prods:ProdCatDetail', args=[self.category.slug, self.slug])
    #
    def get_absolute_url(self):
        return reverse('ProdDetail', args=[self.id])

    def __str__(self):
        return self.name
