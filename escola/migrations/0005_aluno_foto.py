# Generated by Django 4.2.3 on 2023-07-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_delete_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
