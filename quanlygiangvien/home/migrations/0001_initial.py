# Generated by Django 5.0.1 on 2024-05-26 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('departmentID', models.CharField(editable=False, max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructorID', models.CharField(editable=False, max_length=7, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/instructorAvatars/')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('education_level', models.CharField(choices=[('Cử nhân', 'Cử nhân'), ('Thạc sĩ', 'Thạc sĩ'), ('Tiến sĩ', 'Tiến sĩ')], max_length=100)),
                ('job_position', models.CharField(choices=[('Trợ giảng', 'Trợ giảng'), ('Giảng viên', 'Giảng viên'), ('Phó giáo sư', 'Phó giáo sư'), ('Giáo sư', 'Giáo sư')], max_length=100)),
                ('status', models.CharField(choices=[('Đang dạy', 'Đang dạy'), ('Nghỉ hưu', 'Nghỉ hưu'), ('Nghỉ việc', 'Nghỉ việc'), ('Hợp đồng', 'Hợp đồng'), ('Nghỉ phép', 'Nghỉ phép')], max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('articleID', models.CharField(editable=False, max_length=7, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/articleImg/')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('content', models.TextField()),
                ('publish_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.instructor')),
            ],
        ),
    ]