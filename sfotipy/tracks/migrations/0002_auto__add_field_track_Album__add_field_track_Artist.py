# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Track.Album'
        db.add_column('tracks_track', 'Album',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['albums.Album']),
                      keep_default=False)

        # Adding field 'Track.Artist'
        db.add_column('tracks_track', 'Artist',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['artists.Artist']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Track.Album'
        db.delete_column('tracks_track', 'Album_id')

        # Deleting field 'Track.Artist'
        db.delete_column('tracks_track', 'Artist_id')


    models = {
        'albums.album': {
            'Album_Title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artists.Artist']"}),
            'Cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Album'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'artists.artist': {
            'Biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'First_Name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tracks.track': {
            'Album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['albums.Album']"}),
            'Artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artists.Artist']"}),
            'Meta': {'object_name': 'Track'},
            'Order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Track_File': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tracks']