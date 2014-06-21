# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'artists_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('First_Name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Last_Name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('Biography', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'artists', ['Artist'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'artists_artist')


    models = {
        u'artists.artist': {
            'Biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'First_Name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'Meta': {'object_name': 'Artist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['artists']