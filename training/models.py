from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Model(models.Model):
    Userkey = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, default="")
    Student_id = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(null=True)
    collegeYear = models.IntegerField(max_length=20, null=True)


class Nominee_user(models.Model):
    nominee_id = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    phone_no = models.IntegerField(max_length=12)
    email = models.EmailField(max_length=50)
    community = models.CharField(max_length=20, choices=[('1', 'اللجنة العلمية'),
                                           ('2', 'اللجنة الرياضية'),
                                           ('3', 'اللجنة الاجتماعية'),
                                           ('4', 'أسرة الجوالة و الخدمات'),
                                           ('5', 'اللجنة الثقافية'),
                                           ('6', 'اللجنة الفنية'),
                                           ('7', 'لجنة الاسر و الرحلات')
                                           
                                  ])
    rec_letter = models.FileField()
    final_list = models.BooleanField(default=False)
    Numofvotes = models.IntegerField(default=0)


    def __str__(self):
        return str(self.nominee_id)


class Vote(models.Model):
    
    voting_id = models.IntegerField()
    voter_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nominee_id = models.ForeignKey(Nominee_user, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.voting_id)


class Contention(models.Model):

    contention_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nominee_id = models.ForeignKey(Nominee_user, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return str(self.contention_id)
