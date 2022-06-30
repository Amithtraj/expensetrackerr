# Generated by Django 3.2.13 on 2022-06-29 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('tracker', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='type',
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.category'),
        ),
        migrations.AddField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='users.user'),
            preserve_default=False,
        ),
    ]