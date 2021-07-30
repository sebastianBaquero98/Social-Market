from django.db import models
from Influencer.models import Influencer
from Brand.models import Brand
from Tag.models import Tag

# Create your models here.
class Perfil(models.Model):
    """ Modelo representa un perfil de un Creator o de un ClientUser
    """

    redesSociales = [('IG', 'Instagram'), ('TK', 'TikTok'), ('YT','YouTube')]

    # Red Social del perfil del creator o clienteuser
    redeSocial = models.CharField(choices=redesSociales,blank=False,null=False,max_length= 150)

    # Numero de seguidores en el perfil
    numSeguidores = models.IntegerField(default=0, null=False, blank=False)

    # Numero de publicaciones en el perfil 
    numPost= models.IntegerField(default=0, null=False, blank=False)

    # Llave foranea a influencer (Relacion MANY-TO-ONE)
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)

    # Llave foranea a marca (Relacion MANY-TO-ONE)
    marca = models.ForeignKey(Brand, on_delete=models.CASCADE)

    # Lista de tags que tiene el perfil
    tags = models.ManyToManyField(Tag)