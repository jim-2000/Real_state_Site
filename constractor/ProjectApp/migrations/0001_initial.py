# Generated by Django 3.1.5 on 2021-01-12 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConstractionCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keyword', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='catagory/')),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConstractionProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keyword', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('new_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount', models.IntegerField(default=0)),
                ('min_amount', models.IntegerField(default=3)),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.constractioncatagory')),
            ],
        ),
    ]
