# Generated by Django 2.2 on 2019-07-30 10:25

from django.db import migrations
import goodmenu.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goodmenu', '0005_auto_20190730_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodstar',
            name='img',
            field=goodmenu.fields.ThumbnailImageField(null=True, upload_to='goodstar'),
        ),
    ]