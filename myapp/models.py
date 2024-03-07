from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # 追加のフィールドを定義する
    image = models.ImageField(upload_to='media_local/', null=True, blank=True)
    # 他に必要なフィールドがあれば追加する  

    # 既存のフィールドと関連名を変更する場合、related_nameを指定する
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

