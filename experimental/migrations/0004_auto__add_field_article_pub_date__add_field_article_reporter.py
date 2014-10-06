# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.pub_date'
        db.add_column(u'experimental_article', 'pub_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'Article.reporter'
        db.add_column(u'experimental_article', 'reporter',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['experimental.Reporter'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.pub_date'
        db.delete_column(u'experimental_article', 'pub_date')

        # Deleting field 'Article.reporter'
        db.delete_column(u'experimental_article', 'reporter_id')


    models = {
        u'experimental.article': {
            'Meta': {'ordering': "('headline',)", 'object_name': 'Article'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['experimental.Publication']", 'symmetrical': 'False'}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['experimental.Reporter']", 'null': 'True'})
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