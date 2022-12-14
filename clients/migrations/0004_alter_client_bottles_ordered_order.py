# Generated by Django 4.1 on 2022-08-30 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bottles_ordered',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заказа')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения заказа')),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=255)),
                ('finished', models.BooleanField(default=False)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='clients.client')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
