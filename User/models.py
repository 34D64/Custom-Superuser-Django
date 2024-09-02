from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, codemeli, password=None):
        if not codemeli:
            raise ValueError('Users must have an codemeli address')
        
        user = self.model(
            codemeli=codemeli
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, codemeli, password):
        user = self.create_user(
            codemeli=codemeli,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    codemeli = models.IntegerField(unique=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'codemeli'
    def __str__(self):
       return str(self.codemeli)
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin