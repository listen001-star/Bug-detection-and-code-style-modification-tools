import json
import os
from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.function import report
from app01.function import gpt

# default user id
user_id = 1


@csrf_exempt
def user_register(request):
    data = json.loads(request.body.decode('utf-8'))
    name = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if models.UserInfo.objects.filter(user_email=email):
        return_info = {
            "success": False,
            "message": "This user already exists"
        }
    else:
        models.UserInfo.objects.create(user_name=name, user_password=password, user_email=email,
                                       user_role=0, create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return_info = {
            "success": True,
            "message": "Registration successful"
        }
    return JsonResponse(return_info)


@csrf_exempt
def user_login(request):
    data = json.loads(request.body.decode('utf-8'))
    password = data.get('password')
    email = data.get('email')

    user = models.UserInfo.objects.filter(user_email=email).values()

    if user:
        if password == user[0]['user_password']:
            global user_id
            user_id = user[0]['id']
            return_info = {
                "success": True,
                "message": "Login successfully!",
                "username": user[0]['user_name']
            }
        else:
            return_info = {
                "success": False,
                "message": "Wrong password!",
                "username": None
            }
    else:
        return_info = {
            "success": False,
            "message": "No such user!",
            "username": None
        }
    return JsonResponse(return_info)


@csrf_exempt
def file_analyse(request):
    file_object = request.FILES.get("upload_file")
    print(file_object.name)

    file_path = os.path.join(r'D:\WorkingSpace\PyCharmProjects\Project_SE\app01\file', file_object.name)
    if file_object:
        destination = open(file_path, 'wb+')
        for chunk in file_object.chunks():
            destination.write(chunk)
        destination.close()

    results = report.ReportRet(file_path)
    error = report.HistoryRet(file_path)

    print(results)
    print(error)

    # with open(file_path, 'rb') as file:
    #     file_object_content = file.read()
    #
    # file_saved = models.File.objects.create(user_id=user_id, file_name=file_object.name,
    #                                         file_content=file_object_content,
    #                                         file_c=error['C'], file_w=error['W'], file_e=error['E'],
    #                                         file_r=error['R'], file_score=error['Score'], file_date=error['Date'])
    #
    # for item in results:
    #     models.Report.objects.create(user_id=user_id, file_id=file_saved.id,
    #                                  report_line=item['Line'], report_column=item['Column'],
    #                                  report_error_type=item['Error Type'],
    #                                  report_message=item['Message'], report_rule_id=item['Rule ID'])

    return_info = {
        "success": True,
        "data": {
            "results": results,
            "error": error
        }
    }
    return JsonResponse(return_info)


@csrf_exempt
def history(request):
    data = json.loads(request.body.decode('utf-8'))
    file_name = data.get('filename')
    print(file_name)
    file_list = models.File.objects.filter(user_id=user_id, file_name=file_name).values()
    file_detailed = []
    for item in file_list:
        file_report = []
        for item1 in models.Report.objects.filter(user_id=user_id, file_id=item['id']).values():
            file_report.append(item1)

        item['file_report'] = file_report
        file_detailed.append(item)
    print(file_detailed)
    return_info = {
        "success": True,
        "data": file_detailed
    }
    return JsonResponse(return_info)


@csrf_exempt
def chatgpt(request):
    data = json.loads(request.body.decode('utf-8'))
    question = data.get('question')
    print(question)
    answer = gpt.SugRet(question)




def user_list(request):
    # get user_list from MySQL
    # 返回queryset类型，类似于列表[对象,对象,对象]
    queryset = models.UserInfo.objects.all()
    for obj in queryset:
        print(obj.id, obj.user_name, obj.user_password, obj.get_user_role_display(), obj.create_time,
              obj.create_time.strftime("%Y-%m-%d"))
    return HttpResponse("user_list")


@csrf_exempt
def user_add(request):
    # if request.method == "GET":
    #     return HttpResponse("user_add")
    # 获取提交数据
    print(request.method == "POST")
    print(request)
    # name = request.POST.get("name")
    # password = request.POST.get("password")

    data = json.loads(request.body.decode('utf-8'))
    name = data.get('name')
    password = data.get('password')

    print(name, password)
    # 保存
    # models.UserInfo.objects.create(user_name="ddd", user_password="111")

    aaa = {"a": "1111",
           "b": "2222"}
    # return HttpResponse("user_add")
    return JsonResponse(aaa)



