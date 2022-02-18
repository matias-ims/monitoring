# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework import serializers

class Telemetria(models.Model):
    p_id = models.AutoField(db_column='p_Id', primary_key=True)  # Field name made lowercase.
    atime = models.DateTimeField(db_column='Atime')  # Field name made lowercase.
    ano = models.FloatField(blank=True, null=True)
    mes = models.FloatField(blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)
    hora = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    seg = models.IntegerField(blank=True, null=True)
    rpm = models.FloatField(blank=True, null=True)
    stop = models.IntegerField(blank=True, null=True)
    slwd = models.IntegerField(blank=True, null=True)
    ind = models.IntegerField(blank=True, null=True)
    indst = models.IntegerField(blank=True, null=True)
    indsuf = models.IntegerField(blank=True, null=True)
    spsetecr = models.FloatField(db_column='spsetECR', blank=True, null=True)  # Field name made lowercase.
    spsetbrd = models.FloatField(db_column='spsetBRD', blank=True, null=True)  # Field name made lowercase.
    scav = models.FloatField(blank=True, null=True)
    psca = models.FloatField(blank=True, null=True)
    pcor = models.FloatField(blank=True, null=True)
    pmor = models.FloatField(blank=True, null=True)
    insul = models.FloatField(blank=True, null=True)
    carga = models.FloatField(blank=True, null=True)
    pi1 = models.FloatField(db_column='Pi1', blank=True, null=True)  # Field name made lowercase.
    pi2 = models.FloatField(db_column='Pi2', blank=True, null=True)  # Field name made lowercase.
    pi3 = models.FloatField(db_column='Pi3', blank=True, null=True)  # Field name made lowercase.
    pi4 = models.FloatField(db_column='Pi4', blank=True, null=True)  # Field name made lowercase.
    pi5 = models.FloatField(db_column='Pi5', blank=True, null=True)  # Field name made lowercase.
    pi6 = models.FloatField(blank=True, null=True)
    piavg = models.FloatField(blank=True, null=True)
    pidev1 = models.FloatField(blank=True, null=True)
    pidev2 = models.FloatField(blank=True, null=True)
    pidev3 = models.FloatField(blank=True, null=True)
    pidev4 = models.FloatField(blank=True, null=True)
    pidev5 = models.FloatField(blank=True, null=True)
    pidev6 = models.FloatField(blank=True, null=True)
    ofpi1h = models.FloatField(blank=True, null=True)
    ofpi2h = models.FloatField(blank=True, null=True)
    ofpi3h = models.FloatField(blank=True, null=True)
    ofpi4h = models.FloatField(blank=True, null=True)
    ofpi5h = models.FloatField(blank=True, null=True)
    ofpi6h = models.FloatField(blank=True, null=True)
    ofpi1l = models.FloatField(blank=True, null=True)
    ofpi2l = models.FloatField(blank=True, null=True)
    ofpi3l = models.FloatField(blank=True, null=True)
    ofpi4l = models.FloatField(blank=True, null=True)
    ofpi5l = models.FloatField(blank=True, null=True)
    ofpi6l = models.FloatField(blank=True, null=True)
    pc1 = models.FloatField(db_column='Pc1', blank=True, null=True)  # Field name made lowercase.
    pc2 = models.FloatField(db_column='Pc2', blank=True, null=True)  # Field name made lowercase.
    pc3 = models.FloatField(db_column='Pc3', blank=True, null=True)  # Field name made lowercase.
    pc4 = models.FloatField(db_column='Pc4', blank=True, null=True)  # Field name made lowercase.
    pc5 = models.FloatField(db_column='Pc5', blank=True, null=True)  # Field name made lowercase.
    pc6 = models.FloatField(db_column='Pc6', blank=True, null=True)  # Field name made lowercase.
    pcavg = models.FloatField(blank=True, null=True)
    pcdev1 = models.FloatField(blank=True, null=True)
    pcdev2 = models.FloatField(blank=True, null=True)
    pcdev3 = models.FloatField(blank=True, null=True)
    pcdev4 = models.FloatField(blank=True, null=True)
    pcdev5 = models.FloatField(blank=True, null=True)
    pcdev6 = models.FloatField(blank=True, null=True)
    ofpcall = models.FloatField(blank=True, null=True)
    ofpc1 = models.FloatField(blank=True, null=True)
    ofpc2 = models.FloatField(blank=True, null=True)
    ofpc3 = models.FloatField(blank=True, null=True)
    ofpc4 = models.FloatField(blank=True, null=True)
    ofpc5 = models.FloatField(blank=True, null=True)
    ofpc6 = models.FloatField(blank=True, null=True)
    evdop1 = models.FloatField(blank=True, null=True)
    evdop2 = models.FloatField(blank=True, null=True)
    evdop3 = models.FloatField(blank=True, null=True)
    evdop4 = models.FloatField(blank=True, null=True)
    evdop5 = models.FloatField(blank=True, null=True)
    evdop6 = models.FloatField(blank=True, null=True)
    evdcl1 = models.FloatField(blank=True, null=True)
    evdcl2 = models.FloatField(blank=True, null=True)
    evdcl3 = models.FloatField(blank=True, null=True)
    evdcl4 = models.FloatField(blank=True, null=True)
    evdcl5 = models.FloatField(blank=True, null=True)
    evdcl6 = models.FloatField(blank=True, null=True)
    pm1 = models.FloatField(db_column='Pm1', blank=True, null=True)  # Field name made lowercase.
    pm2 = models.FloatField(db_column='Pm2', blank=True, null=True)  # Field name made lowercase.
    pm3 = models.FloatField(db_column='Pm3', blank=True, null=True)  # Field name made lowercase.
    pm4 = models.FloatField(db_column='Pm4', blank=True, null=True)  # Field name made lowercase.
    pm5 = models.FloatField(db_column='Pm5', blank=True, null=True)  # Field name made lowercase.
    pm6 = models.FloatField(db_column='Pm6', blank=True, null=True)  # Field name made lowercase.
    pmavg = models.FloatField(blank=True, null=True)
    pmdev1 = models.FloatField(blank=True, null=True)
    pmdev2 = models.FloatField(blank=True, null=True)
    pmdev3 = models.FloatField(blank=True, null=True)
    pmdev4 = models.FloatField(blank=True, null=True)
    pmdev5 = models.FloatField(blank=True, null=True)
    pmdev6 = models.FloatField(blank=True, null=True)
    ofpmall = models.FloatField(blank=True, null=True)
    ofpm1 = models.FloatField(blank=True, null=True)
    ofpm2 = models.FloatField(blank=True, null=True)
    ofpm3 = models.FloatField(blank=True, null=True)
    ofpm4 = models.FloatField(blank=True, null=True)
    ofpm5 = models.FloatField(blank=True, null=True)
    ofpm6 = models.FloatField(blank=True, null=True)
    fps1 = models.FloatField(blank=True, null=True)
    fps2 = models.FloatField(blank=True, null=True)
    fps3 = models.FloatField(blank=True, null=True)
    fps4 = models.FloatField(blank=True, null=True)
    fps5 = models.FloatField(blank=True, null=True)
    fps6 = models.FloatField(blank=True, null=True)
    fqaof = models.FloatField(blank=True, null=True)
    flowcal = models.FloatField(blank=True, null=True)
    fdens = models.FloatField(blank=True, null=True)
    talign = models.FloatField(blank=True, null=True)
    tdelt = models.FloatField(blank=True, null=True)
    swashp1 = models.FloatField(blank=True, null=True)
    swashp2 = models.FloatField(blank=True, null=True)
    swashp3 = models.FloatField(blank=True, null=True)
    sumtot = models.FloatField(blank=True, null=True)
    hydbef = models.FloatField(blank=True, null=True)
    hydaft = models.FloatField(blank=True, null=True)
    hydspt = models.FloatField(blank=True, null=True)
    lub1 = models.FloatField(blank=True, null=True)
    lub2 = models.FloatField(blank=True, null=True)
    lub3 = models.FloatField(blank=True, null=True)
    lub4 = models.FloatField(blank=True, null=True)
    lub5 = models.FloatField(blank=True, null=True)
    lub6 = models.FloatField(blank=True, null=True)
    lubrn1 = models.FloatField(blank=True, null=True)
    lubrn2 = models.FloatField(blank=True, null=True)
    lubrn3 = models.FloatField(blank=True, null=True)
    lubrn4 = models.FloatField(blank=True, null=True)
    lubrn5 = models.FloatField(blank=True, null=True)
    lubrn6 = models.FloatField(blank=True, null=True)
    lubtot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telemetria'

class TelemetriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetria
        fields = '__all__'

