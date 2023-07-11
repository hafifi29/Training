from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import os
from django.conf import settings
from django.dispatch import receiver

# Create your models here.

class User_Model(models.Model):
    Userkey = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, default="")
    Student_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(null=True)
    college = models.CharField(max_length=20, choices=[('1', 'كلية الحاسبات و الذكاء الاصطناعى'),
                                           ('2', 'كلية الهندسة'),
                                            ('3', 'كلية الطب'),
                                            ('4', 'كلية طب الأسنان'),
                                            ('5', 'كلية الطب البيطرى'),
                                           ('6', 'كلية العلوم'),
                                           ('7', 'كلية الصيدلة'),
                                           ('8', 'كلية التمريض'),
                                           ('9', 'كلية التكنولوجيا و التعليم'),
                                           ('10', 'كلية الدراسات العليا للعلوم المتقدمة'),
                                           ('11', 'كلية علوم الملاحة و تكنولوجيا الفضاء'),
                                           ('12', 'كلية علوم ذوى الاحتياجات الخاصة'),
                                           ('13', 'كلية علوم الأرض'),
                                           ('14', 'كلية الفنون التطبيقية'),
                                           ('15', 'كلية تكنولوجيا العلوم الصحية التطبيقية'),
                                           ('16', 'كلية الزراعة'),
                                           ('17', 'كلية العلاج الطبيعى'),
                                           ('18', 'كلية الإعلام'),
                                           ('19', 'كلية التجارة'),
                                           ('20', 'كلية الآداب'),
                                           ('21', 'كلية التربية'),
                                            ('22', 'كلية الحقوق'),
                                           ('23', 'كلية التربية الرياضية'),
                                           ('24', 'كلية السياسة و الاقتصاد'),
                                           ('25', 'كلية التربية للطفولة المبكرة'),
                                           ('26', 'كلية الألسن'),
                                           ('27', 'كلية الخدمة الاجتماعية التنموية'),
                                           ('28', 'كلية السياحة و الفنادق'),             
                                  ])
    collegeYear = models.IntegerField(null=True)
    Voting_status_1 = models.BooleanField(default=False)
    Voting_status_2 = models.BooleanField(default=False)
    Voting_status_3 = models.BooleanField(default=False)
    Voting_status_4 = models.BooleanField(default=False)



    def __str__(self):
        return str(self.Name)  



class Nominee_user(models.Model):    
    def get_upload_path(instance, filename):
        base_filename, extension = os.path.splitext(filename)
        new_filename = str(instance.UserModelKey.college) + "_" + str(instance.UserModelKey.Student_id) + extension
        return 'rec_letters/%s' % new_filename

    UserModelKey = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    email = models.EmailField(max_length=50)
    community = models.CharField(max_length= 32, choices=[('1', 'اللجنة العلمية'),
                                           ('2', 'اللجنة الرياضية'),
                                           ('3', 'اللجنة الاجتماعية'),
                                           ('4', 'أسرة الجوالة و الخدمات'),
                                           ('5', 'اللجنة الثقافية'),
                                           ('6', 'اللجنة الفنية'),
                                           ('7', 'لجنة الاسر و الرحلات')
                                           
                                  ], default='1')
    rec_letter = models.FileField(upload_to =get_upload_path)
    final_list = models.BooleanField(default=False)
    role = models.CharField(max_length=26, choices=[('1', 'لم يحدد'),
                                           ('2', 'عضو'),
                                           ('3', 'أمين لجنة على مستوى الكلية'),
                                           ('4', 'مساعد أمين لجنة على مستوى الكلية'),
                                           ('5', 'نائب رئيس اتحاد طلاب الكلية'),
                                           ('6', 'رئيس اتحاد طلاب الكلية'),
                                           ('7', 'أمين لجنة على مستوى الجامعة'),
                                           ('8', 'مساعد أمين لجنة على مستوى الجامعة'),
                                           ('9', 'نائب رئيس اتحاد طلاب الجامعة'),
                                           ('10', 'رئيس اتحاد طلاب الجامعة'),                                           
                                  ], default = "1")
    
    communityMemberElections = models.BooleanField(default=False)
    collegeCommunityTrusteeOreHelperElections = models.BooleanField(default=False)
    collegeStudentUnionPresidentOrViceElections = models.BooleanField(default=False)
    universityElections = models.BooleanField(default=False)

    communityMemberElectionsNumOfVotes = models.IntegerField(default=0)
    collegeCommunityTrusteeOreHelperElectionsNumOfVotes = models.IntegerField(default=0)
    collegeStudentUnionPresidentOrViceElectionsNumOfVotes = models.IntegerField(default=0)
    universityElectionsNumOfVotes =  models.IntegerField(default=0)

    def __str__(self):
        return str(self.UserModelKey.Name)
    
    def delete(self, *args, **kwargs):
        if self.rec_letter:
            self.rec_letter.delete(False)
        super().delete(*args, **kwargs)

@receiver(models.signals.pre_delete, sender=Nominee_user)
def delete_file(sender, instance, **kwargs):
    instance.rec_letter.delete(False)

class electoral_prog(models.Model):
    nominee_key = models.OneToOneField(Nominee_user,null=True,on_delete=models.SET_NULL)
    personnal_pic = models.ImageField(blank=True,upload_to='nominees_pictures')
    acheivement_brief = models.TextField()
    program_brief = models.TextField()
    electoral_symbol = models.ImageField(blank=True,upload_to='electoral_symbol')
    electoral_symbol_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nominee_key.UserModelKey.Name} - Electoral Program"

    def delete(self, *args, **kwargs):
        if self.personnal_pic:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(self.personnal_pic)))
        if self.electoral_symbol:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(self.electoral_symbol)))
        super().delete(*args, **kwargs)


class Admin_user(models.Model):
    Userkey = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, default="")
    college = models.CharField(max_length=20, choices=[('1', 'كلية الحاسبات و الذكاء الاصطناعى'),
                                           ('2', 'كلية الهندسة'),
                                            ('3', 'كلية الطب'),
                                            ('4', 'كلية طب الأسنان'),
                                            ('5', 'كلية الطب البيطرى'),
                                           ('6', 'كلية العلوم'),
                                           ('7', 'كلية الصيدلة'),
                                           ('8', 'كلية التمريض'),
                                           ('9', 'كلية التكنولوجيا و التعليم'),
                                           ('10', 'كلية الدراسات العليا للعلوم المتقدمة'),
                                           ('11', 'كلية علوم الملاحة و تكنولوجيا الفضاء'),
                                           ('12', 'كلية علوم ذوى الاحتياجات الخاصة'),
                                           ('13', 'كلية علوم الأرض'),
                                           ('14', 'كلية الفنون التطبيقية'),
                                           ('15', 'كلية تكنولوجيا العلوم الصحية التطبيقية'),
                                           ('16', 'كلية الزراعة'),
                                           ('17', 'كلية العلاج الطبيعى'),
                                           ('18', 'كلية الإعلام'),
                                           ('19', 'كلية التجارة'),
                                           ('20', 'كلية الآداب'),
                                           ('21', 'كلية التربية'),
                                            ('22', 'كلية الحقوق'),
                                           ('23', 'كلية التربية الرياضية'),
                                           ('24', 'كلية السياسة و الاقتصاد'),
                                           ('25', 'كلية التربية للطفولة المبكرة'),
                                           ('26', 'كلية الألسن'),
                                           ('27', 'كلية الخدمة الاجتماعية التنموية'),
                                           ('28', 'كلية السياحة و الفنادق'),             
                                  ])


class Vote(models.Model):
    nominations_period_id = models.IntegerField(default=0)
    voter_id = models.ForeignKey(User_Model, on_delete=models.CASCADE, null=True, blank=True, related_name='related_to_foreign_key_1')
    nominee_id = models.ForeignKey(User_Model, on_delete=models.CASCADE, null=True,  blank=True, related_name='related_to_foreign_key_2')
    community = models.CharField(max_length=21, choices=[('1', 'اللجنة العلمية'),
                                           ('2', 'اللجنة الرياضية'),
                                           ('3', 'اللجنة الاجتماعية'),
                                           ('4', 'أسرة الجوالة و الخدمات'),
                                           ('5', 'اللجنة الثقافية'),
                                           ('6', 'اللجنة الفنية'),
                                           ('7', 'لجنة الاسر و الرحلات')
                                           
                                  ])
    vote_type = models.CharField(max_length=20, choices=[('1', 'collegevote'),
                                           ('2', 'universityvote'),
                                  ])
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
    communityMemberElections = models.BooleanField(default=False)
    collegeCommunityTrusteeOreHelperElections = models.BooleanField(default=False)
    collegeStudentUnionPresidentOrViceElections = models.BooleanField(default=False)
    universityElections = models.BooleanField(default=False)

    Voting_1 = models.BooleanField(default=False)
    Voting_2 = models.BooleanField(default=False)
    Voting_3 = models.BooleanField(default=False)
    Voting_4 = models.BooleanField(default=False)

    result_1 = models.BooleanField(default=False)
    result_2 = models.BooleanField(default=False)
    result_3 = models.BooleanField(default=False)
    result_4 = models.BooleanField(default=False)

    contention = models.BooleanField(default=False)

    def __str__(self):
        return 'Control Content'

    class Meta:
        verbose_name_plural = "Control Content"


class Dates(SingletonModel):
    communityMemberElections_sd = models.DateTimeField(max_length=32, null=True)
    communityMemberElections_ed = models.DateTimeField(max_length=33, null=True)

    collegeCommunityTrusteeOreHelperElections_sd = models.DateTimeField(max_length= 32, null=True)
    collegeCommunityTrusteeOreHelperElections_ed = models.DateTimeField(max_length= 32, null=True)

    collegeStudentUnionPresidentOrViceElections_sd = models.DateTimeField(max_length= 32, null=True)
    collegeStudentUnionPresidentOrViceElections_ed = models.DateTimeField(max_length= 32, null=True)

    universityElections_sd = models.DateTimeField(max_length= 32, null=True)
    universityElections_ed = models.DateTimeField(max_length= 32, null=True)

    Voting_1_sd = models.DateTimeField(max_length= 32, null=True)
    Voting_1_ed = models.DateTimeField(max_length= 32, null=True)

    Voting_2_sd = models.DateTimeField(max_length= 32, null=True)
    Voting_2_ed = models.DateTimeField(max_length= 32, null=True)

    Voting_3_sd = models.DateTimeField(max_length= 32, null=True)
    Voting_3_ed = models.DateTimeField(max_length= 32, null=True)

    Voting_4_sd = models.DateTimeField(max_length= 32, null=True)
    Voting_4_ed = models.DateTimeField(max_length= 32, null=True)

    result_1_sd = models.DateTimeField(max_length= 32, null=True)
    result_1_ed = models.DateTimeField(max_length= 32, null=True)

    result_2_sd = models.DateTimeField(max_length= 32, null=True)
    result_2_ed = models.DateTimeField(max_length= 32, null=True)

    result_3_sd = models.DateTimeField(max_length= 32, null=True)
    result_3_ed = models.DateTimeField(max_length= 32, null=True)

    result_4_sd = models.DateTimeField(max_length= 32, null=True)
    result_4_ed = models.DateTimeField(max_length= 32, null=True)

    con_sd = models.DateTimeField(max_length= 32, null=True)
    con_ed = models.DateTimeField(max_length= 32, null=True)

    nominations_period_id = models.IntegerField(default=0)

