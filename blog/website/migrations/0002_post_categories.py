# Generated by Django 3.1.1 on 2020-10-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('tec', 'Tecnologia'), ('cur', 'Curiosidades'), ('ger', 'Geral')], default='ger', max_length=3),
        ),
    ]
