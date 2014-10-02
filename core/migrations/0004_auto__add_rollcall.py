# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RollCall'
        db.create_table(u'core_rollcall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Student'])),
            ('academicYear', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.AcademicYear'], unique=True)),
            ('stage', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Stage'], unique=True)),
            ('present', self.gf('django.db.models.fields.BooleanField')()),
            ('rollCall_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['RollCall'])


    def backwards(self, orm):
        # Deleting model 'RollCall'
        db.delete_table(u'core_rollcall')


    models = {
        u'core.academicyear': {
            'Meta': {'object_name': 'AcademicYear'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Student']", 'symmetrical': 'False'})
        },
        u'core.rollcall': {
            'Meta': {'object_name': 'RollCall'},
            'academicYear': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.AcademicYear']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'present': ('django.db.models.fields.BooleanField', [], {}),
            'rollCall_date': ('django.db.models.fields.DateTimeField', [], {}),
            'stage': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Stage']", 'unique': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Student']"})
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