from django.db import models

class User(models.Model):
    code = models.CharField(max_length=200, verbose_name='Идентификационный номер')
    name = models.CharField(max_length=200, verbose_name='ФИО')
    birthdate = models.CharField(max_length=200, verbose_name='Дата')

    def __str__(self):
        return f"{self.name} ({self.birthdate}): {self.code} "

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"