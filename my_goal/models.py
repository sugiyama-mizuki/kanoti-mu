from tabnanny import verbose
from django.db import models
from accounts.models import CustomUser

# Create your models here.

class My_Goal(models.Model):
    '''目標モデル'''

    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
    title=models.CharField(verbose_name='目標',max_length=40)
    content=models.TextField(verbose_name='振り返り',blank=True,null=True)
    created_at=models.DateField(verbose_name='作成日時',auto_now_add=True)
    updated_at=models.DateField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural='Goal'

        def __str__(self):
            return self.title