# Generated by Django 3.1.5 on 2021-01-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('pw', models.CharField(max_length=30)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
