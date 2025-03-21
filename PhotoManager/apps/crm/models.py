from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    uploaded_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)  # Змінили на uploaded_by
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title