# Generated by Django 4.2.4 on 2023-08-31 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_alter_post_tzone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='tzone',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Completada', 'Completada')], default='Pendiente', max_length=20, verbose_name='Estado'),
        ),
    ]
