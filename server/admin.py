from django.contrib import admin
from .models import *

class InLineVM_Server(admin.TabularInline):
    model=VM_Server
    extra=1

admin.site.site_header="Server Inventory Admin Panel"
admin.site.site_title="Server Inventory"
admin.site.index_title="Server Inventory Administration"

class Host_SeverAdmin(admin.ModelAdmin):
    inlines=[InLineVM_Server]
    model = Host_Server
    list_display = ['name', 'ip_address','status' ]
    list_filter=['os','status','site']
    search_fields=['name','ip_address','site','status']

admin.site.register(Host_Server, Host_SeverAdmin)


class VM_ServerAdmin(admin.ModelAdmin):
    model = VM_Server
    list_display = ['name', 'ip_address','status','container','dpm']
    list_filter=['os','status','app_owner','container','dpm']
    search_fields=['name','ip_address','app_owner','status']

    #def get_container(self, obj):
        #return obj.container.name
    #get_container.short_description = 'Container'
    #get_container.admin_order_field = 'obj.container.name'

admin.site.register(VM_Server, VM_ServerAdmin)