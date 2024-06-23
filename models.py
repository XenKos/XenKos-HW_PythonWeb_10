from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255, null=True, blank=True)
    born_location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    tags = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.author.fullname}: {self.quote}'
    
    