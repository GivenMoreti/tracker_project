# Generated by Django 4.1.4 on 2022-12-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='describe_issues',
            field=models.CharField(default=None, max_length=3000),
        ),
        migrations.AddField(
            model_name='tracker',
            name='issue',
            field=models.CharField(choices=[('engine', 'engines'), ('lights', 'lights'), ('door', 'door'), ('fluid', 'fluid')], default=None, max_length=30),
        ),
    ]
