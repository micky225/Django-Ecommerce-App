# Generated by Django 4.2.6 on 2023-11-06 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('was_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
