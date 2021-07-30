from django.db import models

# Create your models here.
class Tag(models.Model):
    """ Modelo representa un tag
        Un tag es como un hashtag de un perfi, una caracteristica, un atributo
    """
    tags = [('Arte','Arte'), ('Belleza','Belleza'), ('Negocios','Negocios'), ('Cinema y Actuación','Cinema y Actuación'), ('Cultura','Cultura'), ('DIY','DIY'), ('Baile','Baile'), ('Entretenimiento','Entretenimiento'), ('Familia','Familia'), ('Moda','Moda'), ('Fitness y Bienestar','Fitness y Bienestar'), ('Comida','Comida'), ('Decoración del Hogar','Decoración del Hogar'), ('Humor','Humor'), ('Estilo de vida','Estilo de vida'), ('Nutrición','Nutrición'), ('Medicina','Medicina'), ('Automoviles','Automoviles'), ('Motocicleta','Motocicleta'), ('Deporte','Deporte'), ('Musica','Musica'), ('Covers Musicales','Covers Musicales'), ('Naturaleza','Naturaleza'), ('Mascotas y Animales','Mascotas y Animales'), ('Espiritualidad','Espiritualidad'), ('Tecnologia','Tecnología'), ('Ciencia','Ciencia'), ('Educación','Educación'), ('Viajes','Viajes')] 
    contenido = models.CharField(choices=tags,blank=True,null=True,max_length= 150)