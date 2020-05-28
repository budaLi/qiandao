
from django.http import HttpResponse
from app.models import Teacher,Student,QianDao
from django.utils.translation import ugettext as _
from django.forms import widgets as wid  #因为重名，所以起个别名
from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from functools import wraps
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum
session_name = ""
admin_name = ""

def index(request):
    return render(request,"templete.html")


def student_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')
    if request.method == 'POST':
        # obj = Student.objects.create(Student_id=1,Student_name="libuda", Student_password="123",Student_sex="男",Student_number="152056208",Student_class="001")
        # obj.save()
        user = Student.objects.filter(Student_name=request.POST['user_name']).first()
        global session_name
        session_name=request.POST['user_name']
        # if user and user.pwd == request.POST['password']:
        qians = QianDao.objects.filter(Student_name=user).all()
        return render(request, "student_index.html",{"user":user,"qians":qians})
        # return render(request, 'user_login.html')
    return render(request,"user_login.html")


def teacher_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')
    if request.method == 'POST':
        # obj = Student.objects.create(Student_id=1,Student_name="libuda", Student_password="123",Student_sex="男",Student_number="152056208",Student_class="001")
        # obj.save()
        user = Teacher.objects.filter(Teacher_name=request.POST['user_name']).first()
        global admin_name
        admin_name=request.POST['user_name']
        # if user and user.pwd == request.POST['password']:
        qians = QianDao.objects.all()
        return render(request, "admin_index.html",{"user":user,"qians":qians})
        # return render(request, 'user_login.html')
    return render(request,"user_login.html")


def student_index(request):
    user = Student.objects.filter(Student_name=session_name).first()

    qians = QianDao.objects.filter(Student_name=user).all()
    return render(request, "student_index.html",{"user":user,"qians":qians})

def teacher_index(request):
    user = Teacher.objects.filter(Teacher_name=admin_name).first()

    qians = QianDao.objects.all()
    return render(request, "admin_index.html",{"user":user,"qians":qians})


def qiandao(request):
    """
    签到
    Args:
        request:

    Returns:

    """
    user = Student.objects.filter(Student_name=session_name).first()
    print("user",user)
    obj = QianDao.objects.create(Student_name=user,qiandao="签到成功")
    # obj.save()
    #
    # QianDao.objects.filter(Student_name=user).all().delete()
    qians = QianDao.objects.filter(Student_name=user).all()
    return redirect(student_index)



#签到表单
class QianDaoForm(ModelForm):
    class Meta:
        model = QianDao
        fields = '__all__'     #字段，如果是__all__,就是表示列出所有的字段
        exclude = ('q_id',)          #排除的字段
        # help_texts = None       #帮助提示信息


def edit_qiandao(request,id):
    """
    编辑签到信息
    """
    obj = QianDao.objects.filter(q_id=id).first()
    if request.method == 'GET':
        personform=QianDaoForm(instance=obj)
        return render(request,'qiandao_edit.html',{'personform':personform})
    if request.method == 'POST':
        personform=QianDaoForm(request.POST,instance=obj)
        if personform.is_valid():
            instance = personform.save(commit=False)
            s = request.POST.getlist('qiandao')[0]
            if s=="0":
                instance.qiandao= "签到成功"
            elif s=="1":
                instance.qiandao= "签到失败"
            else:
                instance.qiandao= "签到异常"
            personform.save()
            return redirect(teacher_index)
        else:
            personform=QianDaoForm(obj)
            return redirect(teacher_index)

def delete_qiandao(request,id):
    obj = QianDao.objects.filter(q_id=id).first()
    obj.delete()

    return redirect(teacher_index)



if __name__ == '__main__':
    user = Student.objects.filter(Student_name="libuda").first()
    print("user",user)
    # obj = QianDao.objects.create(Student_name_id=user.Student_id,Student_name=user,qiandao="签到成功")
    # obj.save()
    #
    QianDao.objects.filter(Student_name=user).all().delete()
