# Generated by Django 4.2.3 on 2023-07-31 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0006_alter_aluno_data_nascimento_alter_aluno_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoApolice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVendaApolice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(blank=True, default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(blank=True, default='', max_length=9),
        ),
        migrations.CreateModel(
            name='Apolice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('arquivo', models.FileField(default='', upload_to='')),
                ('tipo_apolice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.tipoapolice')),
                ('tipo_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.tipovendaapolice')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='apolices',
            field=models.ManyToManyField(to='escola.apolice'),
        ),
    ]
