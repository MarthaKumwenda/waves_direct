# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import migrations, models
from django.template.defaultfilters import slugify


# Create your models here.

class Profile(models.Model):
    SALON_OWNER = 1
    BARBERSHOP_OWNER = 2
    FREELANCE = 3
    ROLE_CHOICES = (
        (SALON_OWNER, 'Salon_Owner'),
        (BARBERSHOP_OWNER, 'Barbershop_Owner'),
        (FREELANCE, 'Freelance'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploadphoto = models.FileField(upload_to="profile_photos", default=None, null=True)
    company_name = models.CharField(max_length = 30, default=None, null=True)
    phone = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    Services_offered = models.TextField(default=None, null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

class Gallery(models.Model):
    company_name = models.ForeignKey(User)
    title = models.CharField(max_length=12)

    def profile_photos(self):
        title = self.gallery.title
        slug = slugify(title)
        return "post_images/%s-%s" % (slug, self.image)

class Images(models.Model):
    gallery = models.ForeignKey(Gallery, default=None)
    image = models.FileField(upload_to="profile_photos",
                              default=None, null=True, )


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Profile(user=user)
        profile.save()
        post_save.connect(create_profile, sender=User)



class Popup(models.Model):
    client_name = models.CharField(max_length=60, default=None, null=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100,blank=True)
    time_of_appointment = models.TimeField(default=None, null=True)
    due_date = models.DateField(default=None, null=True)
    request = models.CharField(max_length = 2000,default=None, null=True)



class Comment(models.Model):
    profile = models.ForeignKey('wavesapp.profile', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
def approve(self):
    self.approved_comment = True
    self.save()
def __str__(self):
    return self.text

def approved_comments(self):
    return self.comments.filter(approved_comment=True)


class Migration(migrations.Migration):

    dependencies = [("migrations", "0001_initial")]

    operations = [
        migrations.DeleteModel("Tribble"),
        migrations.AddField("Author", "rating", models.IntegerField(default=0)),
    ]
