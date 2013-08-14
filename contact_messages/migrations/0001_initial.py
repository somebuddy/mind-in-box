# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table('contact_messages_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender_IP', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, default='')),
            ('user_email', self.gf('django.db.models.fields.EmailField')(blank=True, max_length=75, default='')),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('contact_messages', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table('contact_messages_message')


    models = {
        'contact_messages.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender_IP': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'default': "''"}),
            'user_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'default': "''"})
        }
    }

    complete_apps = ['contact_messages']