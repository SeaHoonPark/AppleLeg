# Generated by Django 2.2.4 on 2019-08-29 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Wrongnote',
            fields=[
                ('wrong_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, max_length=1000, null=True, upload_to='image-folder')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('Management_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder.Management')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'ordering': ('wrong_id',),
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('choice_1', models.CharField(max_length=50)),
                ('choice_2', models.CharField(max_length=50)),
                ('choice_3', models.CharField(max_length=50)),
                ('choice_4', models.CharField(max_length=50)),
                ('answer', models.IntegerField()),
                ('explain', models.TextField()),
                ('Management_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder.Management')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'ordering': ('quiz_id',),
            },
        ),
    ]
