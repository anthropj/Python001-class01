from django.db import models

class Douban1(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    star = models.TextField(blank=True, null=True)
    new_star = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban1'


