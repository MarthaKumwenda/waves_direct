from todo.models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user, bio='my bio', website='http://khophi.co')
        user_profile.save()
post_save.connect(create_profile, sender=User)
