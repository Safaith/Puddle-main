# Generated by Django 4.1.7 on 2023-08-24 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0004_alter_conversationmessage_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationmessage',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='conversationmessage',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='ConversationMessage',
        ),
    ]
