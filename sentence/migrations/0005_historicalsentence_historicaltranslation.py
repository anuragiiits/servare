# Generated by Django 2.0.1 on 2018-03-28 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import share.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('language', '0002_language_default_variant'),
        ('sentence', '0004_auto_20180328_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSentence',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('SUG', 'Suggested'), ('EVL', 'Evaluated'), ('CFR', 'Confirmed'), ('RMV', 'Removed')], default='SUG', max_length=50)),
                ('audio', models.TextField(blank=True, max_length=100, null=True, validators=[share.validators.FileValidator(max_size=25165824)])),
                ('place', models.CharField(max_length=150)),
                ('creation_date', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical sentence',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTranslation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('creation_date', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='language.Language')),
                ('sentence', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sentence.Sentence')),
            ],
            options={
                'verbose_name': 'historical translation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
    ]
