# Generated by Django 3.0.5 on 2020-04-02 03:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bost_or_roast', models.BooleanField()),
                ('screen_name', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=280)),
                ('popularity', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
