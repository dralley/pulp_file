# Generated by Django 2.2.4 on 2019-08-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filecontent',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='filedistribution',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='filepublication',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='fileremote',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterField(
            model_name='filecontent',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='file_filecontent', serialize=False, to='core.Content'),
        ),
        migrations.AlterField(
            model_name='filedistribution',
            name='basedistribution_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='file_filedistribution', serialize=False, to='core.BaseDistribution'),
        ),
        migrations.AlterField(
            model_name='filedistribution',
            name='publication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file_filedistribution', to='core.Publication'),
        ),
        migrations.AlterField(
            model_name='filepublication',
            name='publication_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='file_filepublication', serialize=False, to='core.Publication'),
        ),
        migrations.AlterField(
            model_name='fileremote',
            name='remote_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='file_fileremote', serialize=False, to='core.Remote'),
        ),
    ]
