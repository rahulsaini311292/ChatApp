from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, username, password=None):

        user = self.model(email=email, name=name, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, name, username, password=None):
        user = self.create_user(email, name, username)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


# Create your models here.
class Users(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300, unique=True)
    created_on = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'password', 'name')

    objects = UserAccountManager()

    class Meta:
        db_table = "users"
