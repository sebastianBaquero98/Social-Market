from django.db import models
from MyUser.models import MyUser
from Influencer.models import Influencer
from Brand.models import Brand

# Create your models here.
class ClienteUser(MyUser):
    """ Modelo representa a un usuario de Social Market 
        que desea adquirir un servicio de un influencer

    Args:
        MyUser (User): 
    """

    # Objetivo del cliente. Que es lo que busca sacar de la app
    objetivo = models.TextField(verbose_name="con que fin usas Social Market", blank=True, null=True)

    # Lista de deseo de influencers (Relacion MANY-TO-MANY)
    wishList = models.ManyToManyField(Influencer)

    # Lista de Marcas que tiene el cliente
    marcas = models.ManyToManyField(Brand)