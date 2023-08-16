from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.middleware.csrf import get_token
from .models import userTable

def login(request):
    # 接收account和password，返回token
    cfs_token = get_token(request)



    if request.method == 'POST':

        account = request.POST.get('account')
        password = request.POST.get('password')

        # name = userTable.objects.all() #获取所有数据
        # name = userTable.objects.all()[:4] #获取前四条数据
        # name =  userTable.objects.get(name="xiaofei") # 查询某个数据
        # name =  userTable.objects.values(roleid="4") #获取所有值是roldid是4的成员

        try:
        # 检索是否存在
            userTable.objects.get(account=account)
            userTable.objects.get(account=account,password=password)

            response = HttpResponse()
            response["Access-Control-Expose-Headers"] = 'csrf_token'
            response["csrf_token"] = cfs_token
            response["Access-Control-Allow-Origin"] = "*"

            return response

        except:
            response = HttpResponse('账号密码错误')
            response.status_code = 403
            return response




