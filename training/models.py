from django.db import models
from django.contrib.auth.models import User as User_

# Create your models here.


class Nominee_user(models.Model):

    Name = models.CharField(max_length=50, default="")
    phone_no = models.CharField(max_length=12)
    nominee_id = models.ForeignKey(User_, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(null=True)
    community = models.CharField(max_length=20)
    collegeYear = models.IntegerField(max_length=20, null=True)
    rec_letter = models.FileField()
    final_list = models.BooleanField(default=False)
    Numofvotes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.nominee_id)


class Vote(models.Model):
    
    voting_id = models.IntegerField()
    voter_id = models.ForeignKey(User_, on_delete=models.CASCADE)
    nominee_id = models.ForeignKey(Nominee_user, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.voting_id)


class Contention(models.Model):

    contention_id = models.IntegerField()
    user_id = models.ForeignKey(User_, on_delete=models.CASCADE)
    nominee_id = models.ForeignKey(Nominee_user, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return str(self.contention_id)
