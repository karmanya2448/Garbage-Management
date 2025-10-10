

from django.db import migrations, models # type: ignore


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_remove_schedule_driver_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='driver_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
