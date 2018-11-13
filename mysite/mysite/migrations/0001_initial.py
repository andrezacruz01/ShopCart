# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'creditcard'
        db.create_table(u'mysite_creditcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'mysite', ['creditcard'])

        # Adding model 'list_object'
        db.create_table(u'mysite_list_object', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('img_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'mysite', ['list_object'])


    def backwards(self, orm):
        # Deleting model 'creditcard'
        db.delete_table(u'mysite_creditcard')

        # Deleting model 'list_object'
        db.delete_table(u'mysite_list_object')


    models = {
        u'mysite.creditcard': {
            'Meta': {'object_name': 'creditcard'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'mysite.list_object': {
            'Meta': {'object_name': 'list_object'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['mysite']