from django.db import models

# Create your models here.


class UserModel(models.Model):
    Fullname = models.CharField(max_length=200)
    Username = models.CharField(max_length=200, unique=True)
    Email = models.CharField(max_length=200, unique=True)
    Password = models.CharField(max_length=200)
    Unique_Number = models.CharField(max_length=7)
    Image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.Fullname

class UserPosts(models.Model):
    Name = models.CharField(max_length=200)
    PostImage = models.ImageField(upload_to='Post_Image/')
    Category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
        
    
