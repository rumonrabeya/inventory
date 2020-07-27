from django.db import models

# Create your models here.

class Host_Server(models.Model):
    name= models.CharField(max_length=25, blank=False,unique=True, verbose_name="Host Name")
    ip_address= models.GenericIPAddressField(unique=True,default="192.168.1.100", verbose_name="IP Address")
    ram= models.DecimalField(max_digits=5, decimal_places=2,default=1, verbose_name="RAM")
    processor= models.IntegerField(blank=False, null=True, verbose_name="CPU")
    hdd= models.DecimalField(max_digits=7, decimal_places=2,default=1, verbose_name="Hard Disk")
    os= models.CharField(max_length=30,default="Windows", verbose_name="Operating System")
    descriptions= models.CharField(max_length=50,default="", verbose_name="Model")
    choices=(
        ('Running', 'Running'),
        ('Stopped', 'Stopped')
    )
    status= models.CharField(max_length=10, choices= choices, default="Running")
    choices=(
        ('Data Center','DC'),
        ('Disater Recovery', 'DR'),
        ('Far DR','fDR')
    )
    site=models.CharField(max_length=16, choices=choices, default="DC", null=True)
    sn= models.CharField(max_length=30,default="", verbose_name="Serial Number")


    class Meta:
        verbose_name = "Host Server"
        verbose_name_plural = "Host Servers"

    def __str__(self):
        return self.name



class VM_Server(models.Model):
    name= models.CharField(max_length=25, blank=False,unique=True, verbose_name="Server Name")
    ip_address= models.GenericIPAddressField(unique=True,default="192.168.1.100", verbose_name="IP Address")
    ram= models.DecimalField(max_digits=5, decimal_places=2,default=1,verbose_name="RAM")
    processor= models.IntegerField(blank=False, null=True,verbose_name="CPU")
    hdd= models.DecimalField(max_digits=7, decimal_places=2,default=1,verbose_name="Hard Disk")
    os= models.CharField(max_length=30,default="Windows", verbose_name="Operating System")
    descriptions= models.CharField(max_length=50,default="", verbose_name="Purpose")
    app_owner= models.CharField(max_length=20, default="Imran", verbose_name="Application Owner")
    choices=(
        ('Running', 'Running'),
        ('Stopped', 'Stopped')
    )
    status= models.CharField(max_length=10, choices= choices, default="Running")
    container=models.ForeignKey('Host_Server', on_delete=models.CASCADE,blank=False, null=True)
    choices=(
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    dpm= models.CharField(max_length=5, choices=choices, default="Yes", verbose_name="DPM Backup")

    class Meta:
        verbose_name = "VM Server"
        verbose_name_plural = "VM Servers"


    def __str__(self):
        return self.name