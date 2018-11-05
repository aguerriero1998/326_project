# Generated by Django 2.1.1 on 2018-11-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspire', '0008_auto_20181104_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseinstance',
            old_name='time',
            new_name='end',
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='days',
            name='daysoffered',
            field=models.CharField(blank=True, choices=[('m', 'Monday'), ('tu', 'Tuesday'), ('w', 'Wednesday'), ('th', 'Thursday'), ('f', 'Friday')], default='m', help_text='Days offered', max_length=2),
        ),
        migrations.AlterField(
            model_name='days',
            name='daysofweek',
            field=models.ManyToManyField(related_name='daysofweek', to='inspire.CourseInstance'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='coursestaken',
        ),
        migrations.AddField(
            model_name='student',
            name='coursestaken',
            field=models.ManyToManyField(to='inspire.Course'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='shoppingcart',
        ),
        migrations.AddField(
            model_name='student',
            name='shoppingcart',
            field=models.ManyToManyField(related_name='shoppingcart', to='inspire.CourseInstance'),
        ),
    ]
