from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count, F, Value, Sum
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


def home(request, *args, **kwargs):
    # return render(request, 'home.html')
    host = Host_Server.objects.all()
    #hdd_host=VM_Server.objects.filter(host=host).aggregate(Sum('hdd')).get('hdd__sum')
    context = {
        'host': host,
        'header': 'Host Machines'
    }

    return render(request, 'home.html', context)


def display_vm(request, *args, **kwargs):
    servers = VM_Server.objects.all()
    context = {
        'servers': servers,
        'header': 'VM Machines',

    }
    return render(request, 'vm.html', context)


def display_host(request):
    host = Host_Server.objects.all()
    context = {
        'host': host,
        'header': 'Host Machines'
    }
    return render(request, 'home.html', context)


def add_host(request):
    if request.method == "POST":
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = HostForm()
        return render(request, 'add_host.html', {'form': form})


def add_vm(request):
    if request.method == "POST":
        form = VMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_vm')

    else:
        form = VMForm()
        return render(request, 'add_vm.html', {'form': form})


def edit_host(request, pk):
    host = get_object_or_404(Host_Server, pk=pk)

    if request.method == "POST":
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = HostForm(instance=host)
        return render(request, 'edit_host.html', {'form': form})


def edit_vm(request, pk):
    host = get_object_or_404(VM_Server, pk=pk)

    if request.method == "POST":
        form = VMForm(request.POST, instance=host)
        if form.is_valid():
            form.save()
            return redirect('display_vm')

    else:
        form = VMForm(instance=host)
        return render(request, 'edit_vm.html', {'form': form})


def delete_host(request, pk):
    Host_Server.objects.filter(pk=pk).delete()
    host = Host_Server.objects.all()

    context = {
        'host': host
    }

    return render(request, 'home.html', context)


def delete_vm(request, pk):
    VM_Server.objects.filter(pk=pk).delete()
    servers = VM_Server.objects.all()

    context = {
        'servers': servers
    }

    return render(request, 'vm.html', context)


def container_items(request, pk):
    template = 'container_items.html'
    container = get_object_or_404(Host_Server, pk=pk)
    servers = VM_Server.objects.filter(container=container)
    #ram_host=Host_Server.objects.aggregate(Sum('ram'))
    ram_vm=VM_Server.objects.filter(container=container).aggregate(Sum('ram')).get('ram__sum')
    cpu_vm=VM_Server.objects.filter(container=container).aggregate(Sum('processor')).get('processor__sum')
    hdd_vm=VM_Server.objects.filter(container=container).aggregate(Sum('hdd')).get('hdd__sum')

    context = {
        'container': container,
        'servers': servers,
        'ram_vm':ram_vm,
        'cpu_vm':cpu_vm,
        'hdd_vm':hdd_vm
    }

    return render(request, template, context)


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match_vm = VM_Server.objects.filter(Q(name__icontains=srch) |
                                                Q(ip_address__icontains=srch)|
                                                Q(os__icontains=srch)|
                                                Q(app_owner__icontains=srch)|
                                                Q(status__icontains=srch)|
                                                Q(descriptions__icontains=srch)

                                                )

            match_host = Host_Server.objects.filter(Q(name__icontains=srch) |
                                                    Q(ip_address__icontains=srch)|
                                                    Q(os__icontains=srch)|
                                                    Q(status__icontains=srch)|
                                                    Q(descriptions__icontains=srch)|
                                                    Q(site__icontains=srch)|
                                                    Q(sn__icontains=srch)

                                                    )


            if match_vm:
                return render(request, 'search.html', {'sr': match_vm})
            
            elif match_host:
                return render(request, 'search_host.html', {'sr_h': match_host})
            else:
                messages.error(request,'No result Found')

        else:
            return redirect('home')

    return render(request, 'search.html')


def dc_items(request, *args, **kwargs):
    template = 'dc_items.html'
    dc_site=Host_Server.objects.filter(site__contains='Data Center')
    context = {
        'dc_site': dc_site,
        'header': 'Data Center Servers'
    }

    return render(request, template, context)


def dr_items(request, *args, **kwargs):
    template = 'dr_items.html'
    dr_site=Host_Server.objects.filter(site__contains='Disater Recovery')
  
    context = {
        'dr_site': dr_site,
        'header': 'Disater Recovery Center Servers'
    }

    return render(request, template, context)

def far_dr_items(request, *args, **kwargs):
    template = 'far_dr_items.html'
    far_dr=Host_Server.objects.filter(site__contains='Far DR')
    #dc_site=Host_Server.objects.values('site').order_by('site').annotate(count=Count('site'))
    context = {
        'far_dr': far_dr,
        'header': 'Far DR Center Servers'
    }

    return render(request, template, context)


def about(request):
    template= 'about.html'
    context={
        'header': 'About the Server Inventory Management System'
    }
    return render(request, template, context)