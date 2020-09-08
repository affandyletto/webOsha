# Generated by Django 3.1 on 2020-09-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tentang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bidangUtama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidang', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='daftarasesor',
            name='bidang',
            field=models.ManyToManyField(blank=True, default='', to='tentang.bidangUtama'),
        ),
    ]
