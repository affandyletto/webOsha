# Generated by Django 3.1 on 2020-09-02 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengalamanKontakForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='judulGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='dokumentasi',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.RemoveField(
            model_name='dokumentasi',
            name='judul',
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='dokumentasi',
            name='judul',
            field=models.ManyToManyField(blank=True, default='', to='pengalamanKontakForm.judulGallery'),
        ),
    ]
