# Generated by Django 2.2.7 on 2019-11-24 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4096)),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=512)),
                ('state', models.CharField(max_length=2)),
                ('county', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4096)),
                ('term_start', models.DateField()),
                ('term_end', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalActionCommittee',
            fields=[
                ('committee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4096)),
                ('type_of_body', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('state', models.CharField(max_length=2)),
                ('county', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Political bodies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=512)),
                ('last_name', models.CharField(max_length=512)),
                ('nickname', models.CharField(blank=True, max_length=512, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('candidate_id', models.IntegerField(blank=True, null=True)),
                ('political_action_committees', models.ManyToManyField(blank=True, related_name='people', to='electoraid.PoliticalActionCommittee')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='OfficeTenure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('office', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electoraid.Office')),
                ('office_holder', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenures', to='electoraid.Person')),
            ],
        ),
        migrations.AddField(
            model_name='office',
            name='political_body',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electoraid.PoliticalBody'),
        ),
        migrations.CreateModel(
            name='Candidacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballot_order', models.IntegerField(default=0)),
                ('incumbent', models.BooleanField()),
                ('candidate', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidacies', to='electoraid.Person')),
                ('election', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electoraid.Election')),
                ('office', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='electoraid.Office')),
            ],
            options={
                'verbose_name_plural': 'Candidacies',
            },
        ),
    ]