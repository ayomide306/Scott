# Generated by Django 3.2.8 on 2021-11-13 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.reply'),
        ),
    ]
