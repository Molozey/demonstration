# Generated by Django 3.2.9 on 2021-12-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forta', '0003_rename_company_company_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=200)),
                ('trend', models.CharField(max_length=200)),
                ('daily', models.CharField(max_length=200)),
            ],
        ),
    ]