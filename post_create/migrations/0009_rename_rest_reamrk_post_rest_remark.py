# Generated by Django 4.2.5 on 2023-10-25 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post_create", "0008_alter_comment_author_alter_post_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="rest_reamrk",
            new_name="rest_remark",
        ),
    ]
