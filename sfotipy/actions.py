import csv
import logging
import tablib
from datetime import datetime
from django.db.models import Model
from django.db.models.fields.files import FieldFile
from unicodedata import normalize
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
from django.core.urlresolvers import reverse
#import unicodedata



def export_as_excel(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' %opts.app_label
    
    try:
        field_names = modeladmin.model.get_csv_fields()
        v_field_names = field_names
    except:
        field_names = [field.name for field in opts.fields]
        v_field_names = [getattr(field, 'verbose_name') or field.name for field in opts.fields]
    v_field_names = map(lambda x: x.encode('850') if x != 'ID' else 'Id', v_field_names)

     
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        acc = []
        for field in field_names:
            try:
                uf = getattr(obj, field)()
            except TypeError:
                try:
                    uf = getattr(obj, field)
                except:
                    uf = ' error obteniendo el dato'
            if uf is None:
                uf = ''
            elif isinstance(uf, datetime):
                uf = uf
            elif isinstance(uf, Model):
                uf = uf
            elif isinstance(uf, FieldFile):
                uf = uf.url
            acc.append(uf)

        
        
        writer.writerow(acc)

    return response

export_as_excel.short_description = "Exportar a Excel"