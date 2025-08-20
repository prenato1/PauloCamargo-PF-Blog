# accounts/signals.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# Cria o profile automaticamente ao criar um usuário
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Salva o profile sempre que o usuário for salvo
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
