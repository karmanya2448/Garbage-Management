

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_garbagedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.CharField(max_length=25)),
                ('userPhno', models.BigIntegerField()),
                ('userPwrd', models.CharField(max_length=25)),
                ('userAddress', models.TextField()),
                ('userUname', models.CharField(max_length=25)),
                ('userId', models.IntegerField()),
                ('userName', models.CharField(max_length=25)),
                ('userDayDOB', models.IntegerField()),
                ('userMonthDOB', models.IntegerField()),
                ('userYearDOB', models.IntegerField()),
                ('userProfilePicture', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='user_info',
        ),
        migrations.RemoveField(
            model_name='driver_info',
            name='driverEmail',
        ),
        migrations.RemoveField(
            model_name='driver_info',
            name='driverName',
        ),
        migrations.RemoveField(
            model_name='driver_info',
            name='driverPhno',
        ),
        migrations.RemoveField(
            model_name='driver_info',
            name='driverProfilePicture',
        ),
        migrations.RemoveField(
            model_name='driver_info',
            name='driverPwrd',
        ),
        migrations.RemoveField(
            model_name='driver_info',
            name='driverUname',
        ),
        migrations.AddField(
            model_name='garbagedetails',
            name='userDay',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='garbagedetails',
            name='userMonth',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='garbagedetails',
            name='userYear',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
