from django.db import models

class user(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    email = models.EmailField()
    is_trener = models.BooleanField()
  
    class Meta:
        ordering = ('name',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
    def __str__(self):
        return self.name