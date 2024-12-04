# Generated by Django 5.1.2 on 2024-12-04 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_parent_section_coursesection_section_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentExamQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_serial_no', models.IntegerField()),
                ('question_text', models.TextField()),
                ('question_type', models.CharField(max_length=50)),
                ('options', models.JSONField()),
                ('answers', models.JSONField()),
                ('is_correct', models.BooleanField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
    ]
