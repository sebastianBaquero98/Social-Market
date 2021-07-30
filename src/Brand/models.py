from django.db import models

def get_logo_image_filepath(self):
    return f'logo_images/{self.pk}/{"logo.png"}'
def get_default_logo_image_filepath():
    return 'default_logo.png'

# Create your models here.
class Brand(models.Model):
    """ Modelo representa a una marca
        Esta marca pertenece al usuario
    """

    # Nombre de la marca
    nombre = models.CharField(verbose_name="nombre de la marca", max_length= 150, blank=False, null=False)

    # Logo de la marca
    logo = models.ImageField(max_length=255, upload_to=get_logo_image_filepath, null=True, blank=True, default=get_default_logo_image_filepath)