# Generated by Django 3.1.7 on 2021-04-02 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0016_auto_20210318_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Product Name')),
                ('price', models.IntegerField(verbose_name='Product price')),
                ('description', models.TextField(max_length=140, verbose_name='brief description of product')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Product image')),
                ('category', models.IntegerField(choices=[(1, 'Crafts'), (2, 'Home and Living'), (3, 'Jewellery'), (4, 'Accessories'), (5, 'Art')], default=1, verbose_name='Choose product category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='FormModel',
        ),
    ]
