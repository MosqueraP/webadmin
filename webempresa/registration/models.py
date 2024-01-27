from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

'''
RELACION ENTRE MODELOS EN DJANGO:
1. OneToOneField (1:1)  -> un usuarios puede tener un solo peril y un persil puede estar en un solo ususario

2. ForeignKeyField (1:N) 1 autor - N entradas -> un ator puede realizar muchas entradas

3. ManyToManyField (N:M) 1 entradas <-> N entradas -> M muchas categorias -> muchas categorias

'''
# ubicacion del avatar y eliminar el viejo al actualizar 
def custon_upload_to(instance, filename): # personalizado_upload_to
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename #guarda en direccorio profiles con su nuevo nombre

class Profile(models.Model):
    '''Relacion de un peril por cada ususario
    ni distintos ususarios para un mismo permil
    relacion uno a ano '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to=custon_upload_to, blank=True, null=True)
    bio = models.TextField(blank=True, null=True, verbose_name= 'Bibiografia')
    link = models.URLField(blank=True, null=True)
    

    class Meta:
        verbose_name = ("perfil")
        verbose_name_plural = ("perfil")
        ordering = ['user__username']

    def __str__(self):
        return self.user

    # Señal para el ususario al registrarse y evitar lios mas a adelnate
    @receiver(post_save, sender=User) # ejecutar esta señal despues que el usuario se guarde
    def ensure_profile_exists(sender, instance, **kwargs):
        if kwargs.get('created', False):
            #
            Profile.objects.get_or_create(user=instance)
            # print('Se acaba de crear un ususario y su perfil enlazado')