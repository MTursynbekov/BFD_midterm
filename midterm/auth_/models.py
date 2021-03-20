from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

USER_ROLE_SUPER_ADMIN = 1
USER_ROLE_GUEST = 2
USER_ROLES = (
    (USER_ROLE_SUPER_ADMIN, 'super admin'),
    (USER_ROLE_GUEST, 'guest'),
)


class UserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True...")
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Почта")
    first_name = models.CharField(max_length=50, verbose_name="Имя", blank=True)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", blank=True)
    is_staff = models.BooleanField(default=False, verbose_name="Является сотрудником?")
    is_active = models.BooleanField(default=True, verbose_name="Активный?")
    is_superuser = models.BooleanField(default=False, verbose_name="Является суперюзером?")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Дата присоединения")
    role = models.SmallIntegerField(choices=USER_ROLES,
                                    default=USER_ROLE_GUEST)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['-date_joined']
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name


class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(auto_now_add=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
