# Generated by Django 4.0.4 on 2022-07-29 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('placed', models.BooleanField(default=False)),
                ('total_price', models.IntegerField(default=0)),
                ('total_qty', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('qty', models.IntegerField(default=0)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='order_app.order')),
            ],
        ),
    ]
