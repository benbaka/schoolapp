# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AcademicYear'
        db.create_table(u'core_academicyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['AcademicYear'])

        # Adding M2M table for field students on 'AcademicYear'
        m2m_table_name = db.shorten_name(u'core_academicyear_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('academicyear', models.ForeignKey(orm[u'core.academicyear'], null=False)),
            ('student', models.ForeignKey(orm[u'core.student'], null=False))
        ))
        db.create_unique(m2m_table_name, ['academicyear_id', 'student_id'])

        # Adding model 'Stage'
        db.create_table(u'core_stage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Stage'])

        # Adding M2M table for field students on 'Stage'
        m2m_table_name = db.shorten_name(u'core_stage_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('stage', models.ForeignKey(orm[u'core.stage'], null=False)),
            ('student', models.ForeignKey(orm[u'core.student'], null=False))
        ))
        db.create_unique(m2m_table_name, ['stage_id', 'student_id'])


    def backwards(self, orm):
        # Deleting model 'AcademicYear'
        db.delete_table(u'core_academicyear')

        # Removing M2M table for field students on 'AcademicYear'
        db.delete_table(db.shorten_name(u'core_academicyear_students'))

        # Deleting model 'Stage'
        db.delete_table(u'core_stage')

        # Removing M2M table for field students on 'Stage'
        db.delete_table(db.shorten_name(u'core_stage_students'))


    models = {
        u'core.academicyear': {
            'Meta': {'object_name': 'AcademicYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Student']", 'symmetrical': 'False'})
        },
        u'core.stage': {
            'Meta': {'object_name': 'Stage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Student']", 'symmetrical': 'False'})
        },
        u'core.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']