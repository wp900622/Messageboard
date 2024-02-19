import math
from django.http import  JsonResponse
from django.shortcuts import redirect, render,HttpResponse

from messageapp import forms,models
from django.contrib.auth import authenticate
from django.contrib import auth


page = 0
def index_admin_common(pageindex):
    global page, boardunits
    pagesize = 3
    global boardall
    boardall = models.modelUnits.objects.all().order_by('-id')
    datasize = len(boardall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex == None:
        page = 0
        boardunits = models.modelUnits.objects.all().order_by('-id')[:pagesize]
    elif pageindex == 'prev':
        start = (page - 1) * pagesize
        if start >= 0:
            boardunits = models.modelUnits.objects.all().order_by('-id')[start:(start + pagesize)]
        page -= 1
    elif pageindex == 'next':
        start = (page + 1) * pagesize
        if start < datasize:
            boardunits = models.modelUnits.objects.all().order_by('-id')[start:(start + pagesize)]
        page += 1
    currentpage = page
    context = {
        'boardall': boardall,
        'totpage': totpage,
        'currentpage': currentpage,
        'pageindex': pageindex,
        'pagesize': pagesize,
        'boardunits': boardunits,
    }
    return context
# Create your views here.
def index(request,pageindex=None):
    context = index_admin_common(pageindex)
    return render(request, 'index.html', context)

def post(request):
    if request.method == 'POST':
        postform = forms.PostForm(request.POST)
        if postform.is_valid():
            subject = postform.cleaned_data['boardsubject']
            name = postform.cleaned_data['boardname']
            gender = request.POST.get('boardgender',None)
            mail = postform.cleaned_data['boardEmail']
            content = postform.cleaned_data['boardcontent']
            unit = models.modelUnits.objects.create(bname = name, bgender=gender, bmail=mail, 
                                                    bcontent=content,bsubject=subject )
            unit.save()
            message = "已儲存"
            
            return redirect('/index/')
        else:
            message = "沒成功"
    else:
        message = '標題,姓名,內容及驗證碼必須輸入'
        postform = forms.PostForm()
    return render(request, 'post.html', locals())
def login(request):
    message=""
    if request.method == "POST":
        name = request.POST['username'].strip()
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/adminmain/')
            else:
                message="帳號尚未啟用"
        else:
            message = "登入失敗"
    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/index/')

def adminmain(request, pageindex=None):
    context =index_admin_common(pageindex)
    return render(request, 'adminmain.html',context)

def detail(request,messageindex = None , edittype=None):
    unit = models.modelUnits.objects.get(id=messageindex)
    if edittype == None:
        subject = unit.bsubject
        mail = unit.bmail
        time = unit.btime
        content = unit.bcontent
    elif edittype == "1":

        unit.bresponse = request.POST.get('boardresponse','')
        unit.save()
        return redirect('/adminmain/')

    return render(request, 'detail.html', locals())


