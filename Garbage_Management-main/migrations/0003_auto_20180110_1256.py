

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180110_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='userProfilePicture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
