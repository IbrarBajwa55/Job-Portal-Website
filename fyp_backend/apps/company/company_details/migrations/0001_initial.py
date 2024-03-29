# Generated by Django 4.2.7 on 2024-02-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('com_logo', models.ImageField(blank=True, null=True, upload_to='uploaded_logo')),
                ('contact_info', models.CharField(max_length=255)),
            ],
        ),
    ]
