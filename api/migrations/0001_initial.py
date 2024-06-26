# Generated by Django 5.0.2 on 2024-05-02 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('course_title', models.CharField(max_length=100)),
                ('course_credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('course_timeperweek', models.DecimalField(decimal_places=2, max_digits=3)),
                ('course_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14, unique=True)),
                ('designation', models.CharField(choices=[('L', 'Lecturer'), ('SL', 'Senior Lecturer'), ('P', 'Professor'), ('AP', 'Adjunct Professor'), ('AS', 'Assistant Professor'), ('DH', 'Departmental Head'), ('AD', 'Adjunct')], max_length=2)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('EEE', 'Electrical and Electronic Engineering'), ('CE', 'Civil Engineering'), ('ECE', 'Electronics and Communication Engineering')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('room_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassSlots',
            fields=[
                ('day', models.CharField(choices=[('SUN', 'Sunday'), ('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday')], max_length=3, primary_key=True, serialize=False, unique=True)),
                ('class_slots', models.ManyToManyField(to='api.classslot')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('curriculum_semester', models.CharField(choices=[('1.1', '1st Year 1st Semester'), ('1.2', '1st Year 2nd Semester'), ('2.1', '2nd Year 1st Semester'), ('2.2', '2nd Year 2nd Semester'), ('3.1', '3rd Year 1st Semester'), ('3.2', '3rd Year 2nd Semester'), ('4.1', '4th Year 1st Semester'), ('4.2', '4th Year 2nd Semester')], max_length=3, primary_key=True, serialize=False, unique=True)),
                ('courses', models.ManyToManyField(to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curriculum')),
                ('instructors', models.ManyToManyField(to='api.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_instructors', models.ManyToManyField(to='api.courseinstructor')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curriculum')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
            ],
        ),
    ]
