from django.db import models
from django.contrib.auth.models import User as User_

# Create your models here.
class User(models.Model):

    user_id = models.CharField(max_length=7, primary_key= True)
    SSN = models.CharField(max_length=14)
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    year = models.CharField(max_length=10)
    administrator = models.BooleanField()

    def __str__(self):
        return str (self.user_id)
    
class Nominee(models.Model):

    nominee_id = models.ForeignKey(User, on_delete= models.CASCADE)  
    phone_no = models.CharField(max_length=12)
    community = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    rec_letter = models.BinaryField()
    email = models.CharField(max_length=50)
    final_list = models.BooleanField()


    def __str__(self):
        return str (self.nominee_id)
    

class Voting(models.Model):

    voting_id = models.IntegerField()
    voter_id = models.ForeignKey(User, on_delete= models.CASCADE)
    nominee_id = models.ForeignKey(Nominee, on_delete= models.CASCADE)


    def __str__(self):
        return str (self.voting_id)
    

class Contention(models.Model):

    contention_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    nominee_id = models.ForeignKey(Nominee, on_delete= models.CASCADE)
    reason = models.TextField()


    def __str__(self):
        return str (self.contention_id)
    

class Nominee_user(models.Model):

    nominee_id = models.OneToOneField(User_,on_delete=models.CASCADE) 
    phone_no = models.CharField(max_length=12)
    community = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    rec_letter = models.BinaryField()
    email = models.CharField(max_length=50)
    final_list = models.BooleanField()
    
    def __str__(self):
        return str (self.nominee_id)