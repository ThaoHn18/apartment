# Generated by Django 3.2.13 on 2022-06-06 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('manage_id', models.CharField(max_length=200)),
                ('apartment_add', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('used', models.BooleanField(default=False)),
                ('del_flg', models.BooleanField(default=False)),
                ('exclusive_fg', models.BooleanField(default=False)),
                ('created_company_cd', models.IntegerField()),
                ('updated_company_cd', models.IntegerField()),
                ('created_user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created_user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'apartment',
                'ordering': ['created_at'],
            },
        ),
    ]