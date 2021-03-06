from django.urls import reverse
from django.contrib import admin
from django.http import HttpResponseRedirect

from tcms.bugs.models import Bug
from tcms.core.history import ReadOnlyHistoryAdmin


class BugAdmin(ReadOnlyHistoryAdmin):
    actions = ['delete_selected']

    def add_view(self, request, form_url='', extra_context=None):
        return HttpResponseRedirect(reverse('bugs-new'))

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return HttpResponseRedirect(reverse('bugs-get', args=[object_id]))


admin.site.register(Bug, BugAdmin)
