# Generated by Django 2.1.7 on 2019-02-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('Embed_code', models.TextField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
