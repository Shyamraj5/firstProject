from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .forms import RegForm,login,ManagermodelForm
from django.contrib import messages
from .models import Employee,Manager
# Create your views here.
# def home(request):
#     return render(request,'home.html')
class Home(View):
    def get(self,request):
        names=['syam','ayy','nig']
        return render(request,"home.html",{'data':names})
    


class Add(View):
    def get(self,request):
        return render(request,'add.html')
    def post(self,request):
        f=request.POST.get("fnum")
        s=request.POST.get("snum")
        res=int(f)+int(s)
        return render(request,"add.html",{"data":res})
    
class Count(View):
    def get(self,request):

        return render(request,"wordcount.html")
    def post(self,request):
        
        return render(request,"wordcount.html")
class Cal(View):
    def get(self,request):
        return render(request,"calculator.html")
    def post(self,request):
        num=request.POST.get("num")
        res4=eval(num)
        return render(request,'calculator.html',{"data3":res4})
    
class Regview(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request,*args, **kwargs):
        print(request.POST)
        form_data=RegForm(data= request.POST)
        if form_data.is_valid():
           fname=(form_data.cleaned_data.get("first_name"))
           lname=(form_data.cleaned_data.get("last_name"))
           email1=(form_data.cleaned_data.get("email"))
           pass1=(form_data.cleaned_data.get("password"))
           age1=(form_data.cleaned_data.get("age"))
           Employee.objects.create(first_name=fname,last_name=lname,email=email1,password=pass1,age=age1)

           messages.success(request, "regisstration successfull")
           return redirect("home")
        else:
            messages.error(request,"registration faild")
            return render(request,"reg.html",{"form":form_data})
class Log(View):
    def get(self,request):
        logob=login()
        return render(request,'login.html',{"data7":logob})
    def post(self,request):
  
        print(request.POST)
        form_data1=login(data=request.POST)


        if form_data1.is_valid():
            print(form_data1.cleaned_data.get("username"))
            print(form_data1.cleaned_data.get("password"))
            messages.success(request,"login success")
            return redirect("home")
        else:
            messages.error(request,"login faild")
            return render(request,"login.html",{"data7":form_data1})
 

class employeelist(View):
    def get(self,request,*args, **kwargs):
        res=Employee.objects.all()
        print(res)
        return render(request,"viewemp.html",{'data8':res})

class Deletemp(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("eid")
        emp=Employee.objects.get(id=eid)
        emp.delete()
        return redirect('vemp1')
class Update(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("eid")
        emp=Employee.objects.get(id=id)
        form=RegForm(initial={"first_name":emp.first_name,"last_name":emp.last_name,'email':emp.email,"password":emp.password,"age":emp.age})
        return render(request,'updateemp.html',{"form1":form})
    def post(self,request,*args, **kwargs):
        id=kwargs.get("eid")
        emp=Employee.objects.get(id=id)
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            fname=form_data.cleaned_data.get("first_name")
            lname=form_data.cleaned_data.get("last_name")
            email1=form_data.cleaned_data.get("email")
            pass1=form_data.cleaned_data.get("password")
            age1=form_data.cleaned_data.get("age")

            emp.first_name=fname
            emp.last_name=lname
            emp.email=email1
            emp.age=age1
            emp.password=pass1
            emp.save()
            messages.success(request,"emplyee updated successfully")
            return redirect("vemp1")
        else:
            return render(request,"viewemp.html",{"form":form_data})
        


class Addman(View):
    def get(self,request,*args, **kwargs):
        data=ManagermodelForm()
        return render(request,"managerview.html",{"form":data})
    def post(self,request,*args, **kwargs):
        form_data=ManagermodelForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"manager added")
            return redirect("home")
        else:
            return render(request,"managerview.html",{"form":form_data})
class managerLIst(View):
    def get(self,request,*args, **kwargs):
        res=Manager.objects.all()
        return render(request,"viewMnager.html",{"data5":res})
class delman(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("eid")
        Manager.objects.filter(id=id).delete()
        messages.success(request,"manager deleted")
        return redirect("vman")
    
class updateMan(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("eid")
        man=Manager.objects.get(id=id)
        form=ManagermodelForm(instance=man)
        return render(request,'updateMan.html',{"datas":form})
    def post(self,request,*args, **kwargs):
        id=kwargs.get("eid")
        man=Manager.objects.get(id=id)
        form_pdata=ManagermodelForm(request.POST,instance=man,files=request.FILES )
        if form_pdata.is_valid():
           
            man.save()
            messages.success(request,'manager updated successfully')
            return redirect("vman")
        else:
            return render(request,"viewMnager.html",{"datas":form_pdata})

