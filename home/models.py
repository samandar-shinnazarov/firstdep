from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=5000,verbose_name='Post nomi',
                          help_text= 'Post uchun sarlavha kiriting')
    image=models.ImageField(upload_to='post-images',verbose_name='Post rasmi',
                            help_text='Post uchun rasm kiriting')
    def __str__(self):
        return self.title