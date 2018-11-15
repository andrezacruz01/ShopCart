# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Creditcard'
        db.create_table(u'mysite_creditcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('safety_key', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'mysite', ['Creditcard'])

        # Adding model 'SellObjects'
        db.create_table(u'mysite_sellobjects', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'mysite', ['SellObjects'])


    def backwards(self, orm):
        # Deleting model 'Creditcard'
        db.delete_table(u'mysite_creditcard')

        # Deleting model 'SellObjects'
        db.delete_table(u'mysite_sellobjects')


    models = {
        u'mysite.creditcard': {
            'Meta': {'object_name': 'Creditcard'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'safety_key': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'mysite.sellobjects': {
            'Meta': {'object_name': 'SellObjects'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mysite']