# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field favorite_songs on 'Artist'
        m2m_table_name = db.shorten_name(u'artists_artist_favorite_songs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artist', models.ForeignKey(orm[u'artists.artist'], null=False)),
            ('track', models.ForeignKey(orm[u'tracks.track'], null=False))
        ))
        db.create_unique(m2m_table_name, ['artist_id', 'track_id'])


    def backwards(self, orm):
        # Removing M2M table for field favorite_songs on 'Artist'
        db.delete_table(db.shorten_name(u'artists_artist_favorite_songs'))


    models = {
        u'albums.album': {
            'Album_Title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            'Cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'artists.artist': {
            'Biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'First_Name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'Meta': {'object_name': 'Artist'},
            'favorite_songs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'is_favorite_of'", 'blank': 'True', 'to': u"orm['tracks.Track']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tracks.track': {
            'Album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Album']"}),
            'Artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            'Meta': {'object_name': 'Track'},
            'Order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Track_File': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['artists']