# Generated by Django 4.1.5 on 2023-01-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='hr_score',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], help_text='1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分', max_length=10, verbose_name='HR复试综合等级'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='username',
            field=models.CharField(help_text='面试者的名字', max_length=135, verbose_name='姓名'),
        ),
    ]
