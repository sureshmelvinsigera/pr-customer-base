# Generated by Django 2.1.5 on 2019-02-07 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('historical_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='documents',
        ),
        migrations.AddField(
            model_name='document',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='deta_sheet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DataSheet'),
        ),
        migrations.AddField(
            model_name='customer',
            name='professions',
            field=models.ManyToManyField(to='core.Profession'),
        ),
    ]
