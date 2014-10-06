# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table(u'experimental_restaurant', (
            ('place', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['experimental.Place'], unique=True, primary_key=True)),
            ('serves_hot_dogs', self.gf('django.db.models.fields.BooleanField')()),
            ('serves_pizza', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'experimental', ['Restaurant'])

        # Adding model 'Waiter'
        db.create_table(u'experimental_waiter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['experimental.Restaurant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'experimental', ['Waiter'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table(u'experimental_restaurant')

        # Deleting model 'Waiter'
        db.delete_table(u'experimental_waiter')


    models = {
        u'experimental.article': {
            'Meta': {'ordering': "('headline',)", 'object_name': 'Article'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['experimental.Publication']", 'symmetrical': 'False'}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['experimental.Reporter']", 'null': 'True'})
        },
        u'experimental.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        },
        u'experimental.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'place': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['experimental.Place']", 'unique': 'True', 'primary_key': 'True'}),
            'serves_hot_dogs': ('django.db.models.fields.BooleanField', [], {}),
            'serves_pizza': ('django.db.models.fields.BooleanField', [], {})
        },
        u'experimental.waiter': {
            'Meta': {'object_name': 'Waiter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['experimental.Restaurant']"})
        }
    }

    complete_apps = ['experimental']