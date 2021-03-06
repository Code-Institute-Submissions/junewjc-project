# Generated by Django 2.2.4 on 2020-04-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sku', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.CharField(choices=[('PC', 'Phone Cables'), ('PB', 'Power Banks'), ('EP', 'Earphone')], max_length=2)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
