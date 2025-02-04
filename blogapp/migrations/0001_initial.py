# Generated by Django 5.1 on 2024-08-22 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('synopsis', models.TextField()),
                ('image', models.ImageField(default=1, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Current',
            fields=[
                ('cur_id', models.AutoField(primary_key=True, serialize=False)),
                ('curr_read', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('fav_id', models.AutoField(primary_key=True, serialize=False)),
                ('favourite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('rec_id', models.AutoField(primary_key=True, serialize=False)),
                ('recommend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Random',
            fields=[
                ('rand_id', models.AutoField(primary_key=True, serialize=False)),
                ('random', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Memoir',
            fields=[
                ('mem_id', models.AutoField(primary_key=True, serialize=False)),
                ('memoir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Litfic',
            fields=[
                ('litfic_id', models.AutoField(primary_key=True, serialize=False)),
                ('litfiction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Horror',
            fields=[
                ('horr_id', models.AutoField(primary_key=True, serialize=False)),
                ('horror', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('rev_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Romance',
            fields=[
                ('rom_id', models.AutoField(primary_key=True, serialize=False)),
                ('romance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Tbr',
            fields=[
                ('tbr_id', models.AutoField(primary_key=True, serialize=False)),
                ('toread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Thriller',
            fields=[
                ('thrill_id', models.AutoField(primary_key=True, serialize=False)),
                ('thriller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Wrapup',
            fields=[
                ('mon_id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='September',
            fields=[
                ('sept_id', models.AutoField(primary_key=True, serialize=False)),
                ('september', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='October',
            fields=[
                ('octo_id', models.AutoField(primary_key=True, serialize=False)),
                ('october', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='November',
            fields=[
                ('nov_id', models.AutoField(primary_key=True, serialize=False)),
                ('november', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='May',
            fields=[
                ('may_id', models.AutoField(primary_key=True, serialize=False)),
                ('may_rev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='March',
            fields=[
                ('mar_id', models.AutoField(primary_key=True, serialize=False)),
                ('march', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='June',
            fields=[
                ('jun_id', models.AutoField(primary_key=True, serialize=False)),
                ('june', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='July',
            fields=[
                ('jul_id', models.AutoField(primary_key=True, serialize=False)),
                ('july', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='January',
            fields=[
                ('jan_id', models.AutoField(primary_key=True, serialize=False)),
                ('january', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='February',
            fields=[
                ('feb_id', models.AutoField(primary_key=True, serialize=False)),
                ('february', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='December',
            fields=[
                ('dec_id', models.AutoField(primary_key=True, serialize=False)),
                ('december', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='August',
            fields=[
                ('aug_id', models.AutoField(primary_key=True, serialize=False)),
                ('august', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
        migrations.CreateModel(
            name='April',
            fields=[
                ('apr_id', models.AutoField(primary_key=True, serialize=False)),
                ('april', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.wrapup')),
            ],
        ),
    ]
