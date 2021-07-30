from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Se usa para crear un usuario 
# Se usa para crear un superUsario
class MyUserManager(BaseUserManager):
    """ Se usa para crear a un usuario y a un superusuario
    """

    def create_user(self, correo, pais, nombre, password=None):
        """ Crea a un usuario

        Args:
            correo (String): Es el correo del usuario
            pais (String): Es el país de origen del usuario
            nombre (String): Es el nombre del usuario
            password (String, optional): Es la contraseña del usuario. Defaults to None.

        Raises:
            ValueError: Si el usuario se crea sin tener correo, pais ni nombre.

        Returns:
            User: El usuario creado
        """

        if not correo:
            raise ValueError("Los usuarios tienen que tener un correo")
        if not pais:
            raise ValueError("Los usuarios tienen que un país")
        if not nombre:
            raise ValueError("Los usuarios tienen que un nombre")

        usuario = self.model(
            nombre=nombre,
            correo=correo,
            pais=pais,
        )
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario
    
    def create_superuser(self, correo, pais, nombre, password):
        """ Crea a un superusuario

        Args:
            correo (String): Es el correo del usuario
            pais (String): Es el país de origen del usuario
            nombre (String): Es el nombre del usuario
            password (String): Es la contraseña del usuario del

        Returns:
            User: El usuario creado
        """
        usuario = self.create_user(correo=correo, pais=pais, nombre=nombre, password=password)
        usuario.is_superuser = True
        usuario.is_admin= True
        usuario.is_staff = True
        usuario.save(using=self._db)

        return usuario



# Create your models here.
class MyUser(AbstractBaseUser):
    """ El modelo representa a un usuario de la aplicación.
        Este modelo será abstracto, por lo tanto el usuario
        podrá ser un influencer o un cliente.
    """
    # Lista de paises
    paises = [('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua &amp; Barbuda', 'Antigua &amp; Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia &amp; Herzegovina', 'Bosnia &amp; Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('British Virgin Islands', 'British Virgin Islands'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Cote D Ivoire', 'Cote D Ivoire'), ('Croatia', 'Croatia'), ('Cruise Ship', 'Cruise Ship'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands', 'Falkland Islands'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Polynesia', 'French Polynesia'), ('French West Indies', 'French West Indies'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guernsey', 'Guernsey'), ('Guinea', 'Guinea'), ('Guinea Bissau', 'Guinea Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Isle of Man', 'Isle of Man'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jersey', 'Jersey'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kuwait', 'Kuwait'), ('Kyrgyz Republic', 'Kyrgyz Republic'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau', 'Macau'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('Netherlands Antilles', 'Netherlands Antilles'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palestine', 'Palestine'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saint Pierre &amp; Miquelon', 'Saint Pierre &amp; Miquelon'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Satellite', 'Satellite'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('St Kitts &amp; Nevis', 'St Kitts &amp; Nevis'), ('St Lucia', 'St Lucia'), ('St Vincent', 'St Vincent'), ('St. Lucia', 'St. Lucia'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ("Timor L'Este", "Timor L'Este"), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad &amp; Tobago', 'Trinidad &amp; Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks &amp; Caicos', 'Turks &amp; Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')]

    # Nombre completo del usuario
    nombre = models.CharField(verbose_name="nombre Completo", max_length= 150, blank=False, null=False)

    # País de origen del usuario
    pais = models.CharField(verbose_name="país de Nacimiento",max_length= 150, choices=paises, blank=False, null=False)

    # Correo del usuario
    correo = models.EmailField(verbose_name="Correo", max_length= 150, blank=False, null=False)

    # Es Admin
    is_admin = models.BooleanField(default=False)

    # Esta Activo
    is_active = models.BooleanField(default=True)

    # Es Staff
    is_staff = models.BooleanField(default=False)

    # Es Superuser
    is_superuser = models.BooleanField(default=False)

    # Esta escondido el correo
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'correo'

    REQUIRED_FIELDS = ['nombre', 'pais']

    objects = MyUserManager()

    # Hace que el modelo sea abstracto para que otros modelos puedan heredar de el 
    class Meta:
        abstract = True

    def __str__(self):
        return f'El usuario con nombre {self.nombre}, correo {self.correo}, del país {self.pais}'
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True