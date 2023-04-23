from django.db import models
#import user
from django.contrib.auth.models import AbstractUser
#import models from db


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    code=models.CharField(max_length=16,blank=True);
    auth=models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='my_groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='my_user_permissions',
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
