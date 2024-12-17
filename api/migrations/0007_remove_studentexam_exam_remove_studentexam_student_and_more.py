# Generated by Django 5.1.2 on 2024-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_answeroption_question_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentexam',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='studentexam',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentexamanswer',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='studentexamanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='studentexamanswer',
            name='student',
        ),
        migrations.AddField(
            model_name='studentexam',
            name='exam_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='studentexam',
            name='student_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='studentexamanswer',
            name='exam_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='studentexamanswer',
            name='question_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='studentexamanswer',
            name='student_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterModelTable(
            name='studentexam',
            table='api_studentexam',
        ),
        migrations.AlterModelTable(
            name='studentexamanswer',
            table='api_studentexamanswer',
        ),
    ]