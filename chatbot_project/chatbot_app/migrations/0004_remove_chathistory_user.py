# Generated by Django 4.2.5 on 2023-09-21 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0003_alter_chatbotresponse_input_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chathistory',
            name='user',
        ),
    ]