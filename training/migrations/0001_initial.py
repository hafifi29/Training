# Generated by Django 4.2.1 on 2023-05-11 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Control_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communityMemberElections', models.BooleanField(default=False)),
                ('collegeCommunityTrusteeOreHelperElections', models.BooleanField(default=False)),
                ('collegeStudentUnionPresidentOrViceElections', models.BooleanField(default=False)),
                ('universityElections', models.BooleanField(default=False)),
                ('Voting_1', models.BooleanField(default=False)),
                ('Voting_2', models.BooleanField(default=False)),
                ('Voting_3', models.BooleanField(default=False)),
                ('Voting_4', models.BooleanField(default=False)),
                ('result_1', models.BooleanField(default=False)),
                ('result_2', models.BooleanField(default=False)),
                ('result_3', models.BooleanField(default=False)),
                ('result_4', models.BooleanField(default=False)),
                ('contention', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Control Content',
            },
        ),
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communityMemberElections_sd', models.DateTimeField(max_length=32, null=True)),
                ('communityMemberElections_ed', models.DateTimeField(max_length=33, null=True)),
                ('collegeCommunityTrusteeOreHelperElections_sd', models.DateTimeField(max_length=32, null=True)),
                ('collegeCommunityTrusteeOreHelperElections_ed', models.DateTimeField(max_length=32, null=True)),
                ('collegeStudentUnionPresidentOrViceElections_sd', models.DateTimeField(max_length=32, null=True)),
                ('collegeStudentUnionPresidentOrViceElections_ed', models.DateTimeField(max_length=32, null=True)),
                ('universityElections_sd', models.DateTimeField(max_length=32, null=True)),
                ('universityElections_ed', models.DateTimeField(max_length=32, null=True)),
                ('Voting_1_sd', models.DateTimeField(max_length=32, null=True)),
                ('Voting_1_ed', models.DateTimeField(max_length=32, null=True)),
                ('Voting_2_sd', models.DateTimeField(max_length=32, null=True)),
                ('Voting_2_ed', models.DateTimeField(max_length=32, null=True)),
                ('Voting_3_sd', models.DateTimeField(max_length=32, null=True)),
                ('Voting_3_ed', models.DateTimeField(max_length=32, null=True)),
                ('Voting_4_sd', models.DateTimeField(max_length=32, null=True)),
                ('Voting_4_ed', models.DateTimeField(max_length=32, null=True)),
                ('result_1_sd', models.DateTimeField(max_length=32, null=True)),
                ('result_1_ed', models.DateTimeField(max_length=32, null=True)),
                ('result_2_sd', models.DateTimeField(max_length=32, null=True)),
                ('result_2_ed', models.DateTimeField(max_length=32, null=True)),
                ('result_3_sd', models.DateTimeField(max_length=32, null=True)),
                ('result_3_ed', models.DateTimeField(max_length=32, null=True)),
                ('result_4_sd', models.DateTimeField(max_length=32, null=True)),
                ('result_4_ed', models.DateTimeField(max_length=32, null=True)),
                ('con_sd', models.DateTimeField(max_length=32, null=True)),
                ('con_ed', models.DateTimeField(max_length=32, null=True)),
                ('nominations_period_id', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Student_id', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('college', models.CharField(choices=[('1', 'كلية الحاسبات و الذكاء الاصطناعى'), ('2', 'كلية الهندسة'), ('3', 'كلية الطب'), ('4', 'كلية طب الأسنان'), ('5', 'كلية الطب البيطرى'), ('6', 'كلية العلوم'), ('7', 'كلية الصيدلة'), ('8', 'كلية التمريض'), ('9', 'كلية التكنولوجيا و التعليم'), ('10', 'كلية الدراسات العليا للعلوم المتقدمة'), ('11', 'كلية علوم الملاحة و تكنولوجيا الفضاء'), ('12', 'كلية علوم ذوى الاحتياجات الخاصة'), ('13', 'كلية علوم الأرض'), ('14', 'كلية الفنون التطبيقية'), ('15', 'كلية تكنولوجيا العلوم الصحية التطبيقية'), ('16', 'كلية الزراعة'), ('17', 'كلية العلاج الطبيعى'), ('18', 'كلية الإعلام'), ('19', 'كلية التجارة'), ('20', 'كلية الآداب'), ('21', 'كلية التربية'), ('22', 'كلية الحقوق'), ('23', 'كلية التربية الرياضية'), ('24', 'كلية السياسة و الاقتصاد'), ('25', 'كلية التربية للطفولة المبكرة'), ('26', 'كلية الألسن'), ('27', 'كلية الخدمة الاجتماعية التنموية'), ('28', 'كلية السياحة و الفنادق')], max_length=20)),
                ('collegeYear', models.IntegerField(null=True)),
                ('Voting_status_1', models.BooleanField(default=False)),
                ('Voting_status_2', models.BooleanField(default=False)),
                ('Voting_status_3', models.BooleanField(default=False)),
                ('Voting_status_4', models.BooleanField(default=False)),
                ('Userkey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominations_period_id', models.IntegerField(default=0)),
                ('community', models.CharField(choices=[('1', 'اللجنة العلمية'), ('2', 'اللجنة الرياضية'), ('3', 'اللجنة الاجتماعية'), ('4', 'أسرة الجوالة و الخدمات'), ('5', 'اللجنة الثقافية'), ('6', 'اللجنة الفنية'), ('7', 'لجنة الاسر و الرحلات')], max_length=21)),
                ('vote_type', models.CharField(choices=[('1', 'collegevote'), ('2', 'universityvote')], max_length=20)),
                ('nominee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_to_foreign_key_2', to='training.user_model')),
                ('voter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_to_foreign_key_1', to='training.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Nominee_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('community', models.CharField(choices=[('1', 'اللجنة العلمية'), ('2', 'اللجنة الرياضية'), ('3', 'اللجنة الاجتماعية'), ('4', 'أسرة الجوالة و الخدمات'), ('5', 'اللجنة الثقافية'), ('6', 'اللجنة الفنية'), ('7', 'لجنة الاسر و الرحلات')], default='1', max_length=32)),
                ('rec_letter', models.FileField(upload_to='')),
                ('final_list', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('1', 'لم يحدد'), ('2', 'عضو'), ('3', 'أمين لجنة على مستوى الكلية'), ('4', 'مساعد أمين لجنة على مستوى الكلية'), ('5', 'نائب رئيس اتحاد طلاب الكلية'), ('6', 'رئيس اتحاد طلاب الكلية'), ('7', 'أمين لجنة على مستوى الجامعة'), ('8', 'مساعد أمين لجنة على مستوى الجامعة'), ('9', 'نائب رئيس اتحاد طلاب الجامعة'), ('10', 'رئيس اتحاد طلاب الجامعة')], default='1', max_length=26)),
                ('communityMemberElections', models.BooleanField(default=False)),
                ('collegeCommunityTrusteeOreHelperElections', models.BooleanField(default=False)),
                ('collegeStudentUnionPresidentOrViceElections', models.BooleanField(default=False)),
                ('universityElections', models.BooleanField(default=False)),
                ('communityMemberElectionsNumOfVotes', models.IntegerField(default=0)),
                ('collegeCommunityTrusteeOreHelperElectionsNumOfVotes', models.IntegerField(default=0)),
                ('collegeStudentUnionPresidentOrViceElectionsNumOfVotes', models.IntegerField(default=0)),
                ('universityElectionsNumOfVotes', models.IntegerField(default=0)),
                ('UserModelKey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='training.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='electoral_prog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personnal_pic', models.ImageField(blank=True, upload_to='nominees_pictures')),
                ('acheivement_brief', models.TextField()),
                ('program_brief', models.TextField()),
                ('electoral_symbol', models.ImageField(blank=True, upload_to='electoral_symbol')),
                ('electoral_symbol_name', models.CharField(max_length=50)),
                ('nominee_key', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='training.nominee_user')),
            ],
        ),
        migrations.CreateModel(
            name='Current_Nom_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.CharField(choices=[('1', 'اللجنة العلمية'), ('2', 'اللجنة الرياضية'), ('3', 'اللجنة الاجتماعية'), ('4', 'أسرة الجوالة و الخدمات'), ('5', 'اللجنة الثقافية'), ('6', 'اللجنة الفنية'), ('7', 'لجنة الاسر و الرحلات')], default='1', max_length=32)),
                ('numOfVotes', models.IntegerField(default=0)),
                ('role', models.CharField(choices=[('1', 'لم يحدد'), ('2', 'عضو'), ('3', 'أمين لجنة على مستوى الكلية'), ('4', 'مساعد أمين لجنة على مستوى الكلية'), ('5', 'نائب رئيس اتحاد طلاب الكلية'), ('6', 'رئيس اتحاد طلاب الكلية'), ('7', 'أمين لجنة على مستوى الجامعة'), ('8', 'مساعد أمين لجنة على مستوى الجامعة'), ('9', 'نائب رئيس اتحاد طلاب الجامعة'), ('10', 'رئيس اتحاد طلاب الجامعة')], default='1', max_length=33)),
                ('Nominee_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.nominee_user')),
            ],
        ),
        migrations.CreateModel(
            name='Contention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('nominee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.nominee_user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('college', models.CharField(choices=[('1', 'كلية الحاسبات و الذكاء الاصطناعى'), ('2', 'كلية الهندسة'), ('3', 'كلية الطب'), ('4', 'كلية طب الأسنان'), ('5', 'كلية الطب البيطرى'), ('6', 'كلية العلوم'), ('7', 'كلية الصيدلة'), ('8', 'كلية التمريض'), ('9', 'كلية التكنولوجيا و التعليم'), ('10', 'كلية الدراسات العليا للعلوم المتقدمة'), ('11', 'كلية علوم الملاحة و تكنولوجيا الفضاء'), ('12', 'كلية علوم ذوى الاحتياجات الخاصة'), ('13', 'كلية علوم الأرض'), ('14', 'كلية الفنون التطبيقية'), ('15', 'كلية تكنولوجيا العلوم الصحية التطبيقية'), ('16', 'كلية الزراعة'), ('17', 'كلية العلاج الطبيعى'), ('18', 'كلية الإعلام'), ('19', 'كلية التجارة'), ('20', 'كلية الآداب'), ('21', 'كلية التربية'), ('22', 'كلية الحقوق'), ('23', 'كلية التربية الرياضية'), ('24', 'كلية السياسة و الاقتصاد'), ('25', 'كلية التربية للطفولة المبكرة'), ('26', 'كلية الألسن'), ('27', 'كلية الخدمة الاجتماعية التنموية'), ('28', 'كلية السياحة و الفنادق')], max_length=20)),
                ('Userkey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
