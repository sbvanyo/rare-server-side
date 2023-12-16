# Generated by Django 4.1.3 on 2023-12-14 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('image_url', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('approved', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=100)),
                ('profile_image_url', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('created_on', models.DateField()),
                ('active', models.BinaryField()),
                ('is_staff', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.tag')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='rare_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.user'),
        ),
    ]