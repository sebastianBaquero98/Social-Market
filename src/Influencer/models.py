from django.db import models
from MyUser.models import MyUser

def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profilePic.png"}'
def get_default_profile_image_filepath():
    return 'default-profile.jpg'

# Create your models here.
class Influencer(MyUser):
    """ Modelo representa un Influencer

    Args:
        MyUser (User): El influencer extiende de MyUser
    """
    # Correo de contacto para pauta
    contactoCorreo = models.EmailField(verbose_name="correo de contacto",max_length= 150, blank=False, null=False)

    # Handel instagram de contacto con manager o personal para pauta
    contactoInstagram = models.CharField(verbose_name="contacto en instagram", max_length= 150,blank=True, null=True)

    # URL de sitio web de manager o personal para pauta
    contactoSitioWeb = models.TextField(verbose_name="sitio web de contacto", max_length= 150, blank=True, null=True)

    # Foto de perfil de Social Market
    profilePic = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image_filepath)

    # Likes totales de todas las redes sociales
    likeTotales = models.IntegerField(default=0, null=False, blank=False)

    # Bio: Es una pequeña descripción sobre el influencer, un abre bocas
    bio = models.TextField(verbose_name="pequeña descripción sobre ti", null=False, blank=False)

    # Esta escondiendo información de contacto
    hidecontactInfo = models.BooleanField(default=True)

    