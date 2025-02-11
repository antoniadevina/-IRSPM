# Generated by Django 3.1.7 on 2021-03-06 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AGRApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=50, unique=True)),
                ('main_musclegroup', models.CharField(blank=True, max_length=30, null=True)),
                ('detailed_musclegroup', models.CharField(blank=True, max_length=30, null=True)),
                ('other_musclegroups', models.CharField(blank=True, max_length=100, null=True)),
                ('exercise_type', models.CharField(blank=True, max_length=30, null=True)),
                ('mechanics', models.CharField(blank=True, max_length=30, null=True)),
                ('equipment', models.CharField(blank=True, max_length=100, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=20, null=True)),
                ('instruction_text', models.TextField(blank=True, null=True)),
                ('pic_no', models.TextField(blank=True, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'EXERCISE',
            },
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_id', models.IntegerField()),
                ('date', models.DateField()),
                ('userdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGRApi.userdata')),
            ],
            options={
                'db_table': 'ROUTINE',
            },
        ),
        migrations.CreateModel(
            name='UserExerciseRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_score', models.FloatField(default=5)),
                ('exercise_count', models.IntegerField(default=1)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGRApi.exercise')),
                ('userdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGRApi.userdata')),
            ],
            options={
                'db_table': 'USER_EXERCISE',
            },
        ),
        migrations.CreateModel(
            name='RoutineExercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGRApi.exercise')),
                ('set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AGRApi.routine')),
            ],
            options={
                'db_table': 'ROUTINE_EXERICSE',
            },
        ),
    ]
