# Generated by Django 4.1.7 on 2023-05-15 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_lessonplangpt_alter_examgptmodel_topic_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="LessonPlanGPT",
            new_name="LessonPlanGPTModel",
        ),
    ]
