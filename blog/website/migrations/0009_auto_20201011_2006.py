# Generated by Django 3.1.1 on 2020-10-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]