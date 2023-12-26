from django.db import models

# Create your models here.
#Create Comapny Model
class Bookshelf(models.Model):
   ISBN=models.IntegerField(unique=True, primary_key=True)
   title= models.CharField(max_length=100)
   Author=models.CharField(max_length=100)
   genre=models.CharField(max_length=100, choices=(
      ("Fiction", "fiction"),("mythology", "mythology"),("drama","drama"),("others","others")
   ))
   publish_year=models.DateTimeField(auto_now=False)
   is_deleted=models.BooleanField(default=False)

   def __str__(self) -> str:
      return self.title

class Reviews (models.Model):
   userName=models.CharField(max_length=100)
   reviews=models.TextField(blank= True)
   book=models.ForeignKey(Bookshelf, on_delete=models.CASCADE)

   