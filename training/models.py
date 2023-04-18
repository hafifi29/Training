from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class User_Model(models.Model):
    Userkey = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, default="")
    Student_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(null=True)
    collegeYear = models.IntegerField(null=True)

    def __str__(self):
        return str(self.Name)


class Nominee_user(models.Model):
    UserModelKey = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
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
        return str(self.UserModelKey.Name)


class Admin_user(models.Model):
    Userkey = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, default="")



class Vote(models.Model):
    
    voter_id = models.ForeignKey(User_Model, on_delete=models.CASCADE, null=True, blank=True)
    nominee_id = models.ForeignKey(Nominee_user, on_delete=models.CASCADE, null=True,  blank=True)

    def __str__(self):
        return str(self.id)

class Contention(models.Model):
    user_id = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    nominee_id = models.ForeignKey(Nominee_user, on_delete=models.CASCADE)
    reason = models.TextField()
    

# control what apper to students 


# singletonPatern

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get(pk=1)
        except ObjectDoesNotExist:
            return cls()


class Control_content(SingletonModel):
    nomination = models.BooleanField(default=False)
    vote = models.BooleanField(default=False)
    contention = models.BooleanField(default=False)
    result = models.BooleanField(default=False)

    def __str__(self):
        return 'Control Content'

    class Meta:
        verbose_name_plural = "Control Content"


class Dates(SingletonModel):
    nomin_sd = models.CharField(max_length=30)
    nomin_ed = models.CharField(max_length=30)
    
    vote_sd = models.CharField(max_length=30)
    vote_ed = models.CharField(max_length=30)

    con_sd = models.CharField(max_length=30)
    con_ed = models.CharField(max_length=30)
