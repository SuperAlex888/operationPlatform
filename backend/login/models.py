from django.db import models


class roleTable(models.Model):
    roleName = models.CharField(default=None,max_length=20)

class filialeTable(models.Model):
    filialeName = models.CharField(default=None,max_length=20)


class userTable(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    filialeId = models.ForeignKey(filialeTable, on_delete=models.CASCADE)
    roleId = models.ForeignKey(roleTable, on_delete=models.CASCADE)




