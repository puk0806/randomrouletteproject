# Generated by Django 2.2 on 2019-08-20 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goodmenu', '0013_auto_20190810_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodcomment',
            name='goodmenucomment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goodcomments', to='goodmenu.Goodmenu'),
        ),
    ]
