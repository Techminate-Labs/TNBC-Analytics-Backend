# Generated by Django 3.2.5 on 2021-10-27 15:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('tnbc_pk', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('discord', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/team/')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Contributor',
            },
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(upload_to='images/qr/')),
                ('public_key', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Donate',
            },
        ),
        migrations.CreateModel(
            name='FaqType',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'FAQ Categories',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('facebook', models.CharField(max_length=255)),
                ('youtube', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('reddit', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('discord', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('faqType_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='v2.faqtype')),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
