# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Track'
        db.create_table('tracks_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('Track_File', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('tracks', ['Track'])


    def backwards(self, orm):
        # Deleting model 'Track'
        db.delete_table('tracks_track')


    models = {
        'tracks.track': {
            'Meta': {'object_name': 'Track'},
            'Order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Track_File': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tracks']