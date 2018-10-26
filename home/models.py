from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "auth_user"
        verbose_name_plural = '用户'
    pass

# 广告位

# 产品

#