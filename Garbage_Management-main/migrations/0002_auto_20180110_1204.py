

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='profilePicture',
        ),
        migrations.AddField(
            model_name='user_info',
            name='userProfilePicture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
