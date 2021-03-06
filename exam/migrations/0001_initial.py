# Generated by Django 2.1.11 on 2020-02-13 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=50)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('section', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=500)),
                ('erp', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('grade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Studentmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tname', models.CharField(choices=[('--', '--'), ('WT', 'WEEKLY-TEST'), ('ST', 'SPECIAL-TEST')], max_length=4)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testid',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('testid', models.CharField(max_length=10)),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='studentmark',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Testid'),
        ),
        migrations.AddField(
            model_name='grade',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Section'),
        ),
        migrations.AddField(
            model_name='grade',
            name='subject_id',
            field=models.ManyToManyField(to='exam.Subject'),
        ),
    ]
