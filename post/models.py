from django.db import models
# from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name="Başlık")    
    content = models.TextField(verbose_name="İçerik")
    # yazar = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # created_date = models.DateTimeField(default=timezone.now)
    publishing_date = models.DateTimeField(verbose_name="Yayımlanma Tarihi")

    """
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    """
    
    # Post listesi başlık adlarıyla listelenir.
    def __str__(self):
        return self.title
        
