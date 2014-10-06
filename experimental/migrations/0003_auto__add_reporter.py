# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reporter'
        db.create_table(u'experimental_reporter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'experimental', ['Reporter'])


    def backwards(self, orm):
        # Deleting model 'Reporter'
        db.delete_table(u'experimental_reporter')


    models = {
        u'experimental.article': {
            'Meta': {'ordering': "('headline',)", 'object_name': 'Article'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['experimental.Publication']", 'symmetrical': 'False'})
        },
        u'experimental.publication': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Publication'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'experimental.reporter': {
            'Meta': {'object_name': 'Reporter'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['experimental']