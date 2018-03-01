# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-01 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0034_auto_20171214_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('provisional', models.BooleanField(default=False, help_text=b'True if the allergy is only suspected. Defaults to False.', verbose_name=b'Suspected?')),
                ('details', models.CharField(blank=True, max_length=255)),
                ('drug_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_allergies_subrecords', to=settings.AUTH_USER_MODEL)),
                ('drug_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drug')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_allergies_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Allergies',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('hospital_number', models.CharField(blank=True, help_text=b'The unique identifier for this patient at the hospital.', max_length=255)),
                ('nhs_number', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'NHS Number')),
                ('surname', models.CharField(blank=True, max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name=b'Date of Birth')),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name=b'Date of Death')),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('gp_practice_code', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'GP Practice Code')),
                ('death_indicator', models.BooleanField(default=False, help_text=b'This field will be True if the patient is deceased.')),
                ('sex_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('title_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('marital_status_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('ethnicity_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('birth_place_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('birth_place_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Destination')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_demographics_subrecords', to=settings.AUTH_USER_MODEL)),
                ('ethnicity_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Ethnicity')),
                ('marital_status_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.MaritalStatus')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('sex_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Gender')),
                ('title_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Title')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_demographics_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Demographics',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('provisional', models.BooleanField(default=False, help_text=b'True if the diagnosis is provisional. Defaults to False', verbose_name=b'Provisional?')),
                ('details', models.CharField(blank=True, max_length=255)),
                ('date_of_diagnosis', models.DateField(blank=True, null=True)),
                ('condition_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('condition_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Condition')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_diagnosis_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_diagnosis_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Diagnoses',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('test', models.CharField(max_length=255)),
                ('date_ordered', models.DateField(blank=True, null=True)),
                ('details', models.CharField(blank=True, max_length=255)),
                ('microscopy', models.CharField(blank=True, max_length=255)),
                ('organism', models.CharField(blank=True, max_length=255)),
                ('sensitive_antibiotics', models.CharField(blank=True, max_length=255)),
                ('resistant_antibiotics', models.CharField(blank=True, max_length=255)),
                ('result', models.CharField(blank=True, max_length=255)),
                ('igm', models.CharField(blank=True, max_length=20)),
                ('igg', models.CharField(blank=True, max_length=20)),
                ('vca_igm', models.CharField(blank=True, max_length=20)),
                ('vca_igg', models.CharField(blank=True, max_length=20)),
                ('ebna_igg', models.CharField(blank=True, max_length=20)),
                ('hbsag', models.CharField(blank=True, max_length=20)),
                ('anti_hbs', models.CharField(blank=True, max_length=20)),
                ('anti_hbcore_igm', models.CharField(blank=True, max_length=20)),
                ('anti_hbcore_igg', models.CharField(blank=True, max_length=20)),
                ('rpr', models.CharField(blank=True, max_length=20)),
                ('tppa', models.CharField(blank=True, max_length=20)),
                ('viral_load', models.CharField(blank=True, max_length=20)),
                ('parasitaemia', models.CharField(blank=True, max_length=20)),
                ('hsv', models.CharField(blank=True, max_length=20)),
                ('vzv', models.CharField(blank=True, max_length=20)),
                ('syphilis', models.CharField(blank=True, max_length=20)),
                ('c_difficile_antigen', models.CharField(blank=True, max_length=20)),
                ('c_difficile_toxin', models.CharField(blank=True, max_length=20)),
                ('species', models.CharField(blank=True, max_length=20)),
                ('hsv_1', models.CharField(blank=True, max_length=20)),
                ('hsv_2', models.CharField(blank=True, max_length=20)),
                ('enterovirus', models.CharField(blank=True, max_length=20)),
                ('cmv', models.CharField(blank=True, max_length=20)),
                ('ebv', models.CharField(blank=True, max_length=20)),
                ('influenza_a', models.CharField(blank=True, max_length=20)),
                ('influenza_b', models.CharField(blank=True, max_length=20)),
                ('parainfluenza', models.CharField(blank=True, max_length=20)),
                ('metapneumovirus', models.CharField(blank=True, max_length=20)),
                ('rsv', models.CharField(blank=True, max_length=20)),
                ('adenovirus', models.CharField(blank=True, max_length=20)),
                ('norovirus', models.CharField(blank=True, max_length=20)),
                ('rotavirus', models.CharField(blank=True, max_length=20)),
                ('giardia', models.CharField(blank=True, max_length=20)),
                ('entamoeba_histolytica', models.CharField(blank=True, max_length=20)),
                ('cryptosporidium', models.CharField(blank=True, max_length=20)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_investigation_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_investigation_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('hospital', models.CharField(blank=True, max_length=255)),
                ('ward', models.CharField(blank=True, max_length=255)),
                ('bed', models.CharField(blank=True, max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_location_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_location_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PastMedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('year', models.CharField(blank=True, max_length=4)),
                ('details', models.CharField(blank=True, max_length=255)),
                ('condition_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('condition_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Condition')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_pastmedicalhistory_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_pastmedicalhistory_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Past medical histories',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PatientConsultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('when', models.DateTimeField(blank=True, null=True)),
                ('initials', models.CharField(blank=True, help_text=b'The initials of the user who gave the consult.', max_length=255)),
                ('discussion', models.TextField(blank=True)),
                ('reason_for_interaction_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_patientconsultation_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('reason_for_interaction_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.PatientConsultationReasonForInteraction')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_patientconsultation_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SymptomComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('duration', models.CharField(blank=True, choices=[(b'3 days or less', b'3 days or less'), (b'4-10 days', b'4-10 days'), (b'11-21 days', b'11-21 days'), (b'22 days to 3 months', b'22 days to 3 months'), (b'over 3 months', b'over 3 months')], help_text=b'The duration for which the patient had been experiencing these symptoms when recorded.', max_length=255, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_symptomcomplex_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('symptoms', models.ManyToManyField(blank=True, related_name='symptoms', to='opal.Symptom')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_symptomcomplex_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Symptom complexes',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('dose', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, help_text=b'The date on which the patient began receiving this treatment.', null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('frequency_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('drug_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('route_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_openodonto_treatment_subrecords', to=settings.AUTH_USER_MODEL)),
                ('drug_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drug')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('frequency_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drugfreq')),
                ('route_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drugroute')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_openodonto_treatment_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]