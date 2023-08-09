from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from datetime import date,timedelta

# Create your views here.
def index(request):
    ind=indexform()
    return render(request,'index.html',{'ind':ind})
def admino(request):
    products=ProductTable.objects.all()
    #if request.method=="POST":      
        #products=ProductTable.objects.all()
        #return render(request,'admin.html',{'products':products,})

    return render(request,'admin.html',{'products':products,})
    
def category(request):
    cat=catform()
    if request.method=='POST':
        cat=catform(request.POST)
        if cat.is_valid():
            cname=cat.cleaned_data['category_name']
            cdescription=cat.cleaned_data['category_description']
            res=category_details(category_name=cname,category_description=cdescription)
            res.save()
            msg="category added"
        return render(request,'category.html',{'cat':cat,'msg':msg})
    
    return render(request,'category.html',{'cat':cat})

def seller(request):
    sel=sellerform()
    if request.method=="POST":
        sel=sellerform(request.POST)
        if sel.is_valid():
            sname=sel.cleaned_data['sellername']
            sadress=sel.cleaned_data['adress']
            semail=sel.cleaned_data['email']
            spassword=sel.cleaned_data['password']
            sphone=sel.cleaned_data['phone_number']
            res=SellerTable(sellername=sname,adress=sadress,email=semail,password=spassword,phone_number=sphone)
            res.save()
            msg="seller added"
        return render(request,'seller.html',{'sel':sel,'msg':msg})
    return render(request,'seller.html',{'sel':sel})

def product(request):
    prod=productform()
    if request.method=="POST":
        prod=productform(request.POST)
        if prod.is_valid():
            prname=prod.cleaned_data['Product_name']
            prprice=prod.cleaned_data['price']
            catid=prod.cleaned_data['category_ID']
            selid=prod.cleaned_data['Seller_ID']
            res=ProductTable(Product_name=prname,price=prprice,category_ID=catid,Seller_ID=selid)
            res.save()
            msg="product added"
        return render(request,'product.html',{'prod':prod,'msg':msg})
    return render(request,'product.html',{'prod':prod})

'''def register(request):
   form=createuserform()
   if request.method=="POST":
       form=createuserform(request.POST)
       if form.is_valid():
           form.save()
   return render(request,'register.html',{'form':form})'''

def register(request):
    refrm=registerform()
    if request.method=="POST":
        refrm=registerform(request.POST)
        if refrm.is_valid():
            nme=refrm.cleaned_data['name']
            uname=refrm.cleaned_data['username']
            dob=refrm.cleaned_data['date_of_birth']
            adr=refrm.cleaned_data['adress']
            ema=refrm.cleaned_data['email']
            ph=refrm.cleaned_data['phone_number']
            pwd=refrm.cleaned_data['password']
            uname_true=user.objects.filter(username=uname).exists()
            email_true=user.objects.filter(email=ema).exists()
            if uname_true or  email_true:
                already="Username or email already exists"
                return render(request,'register.html',{'refrm':refrm,'already':already})
            else:
                res=user(name=nme,username=uname,date_of_birth=dob,adress=adr,email=ema,phone_number=ph,password=pwd,)
                res.save()
                return redirect('eshopapp:login')   
    return render(request,'register.html',{'refrm':refrm})
def login(request):
    log=loginform()
    if request.method=="POST":
        log=loginform(request.POST)
        if log.is_valid():
            unme=log.cleaned_data['username']
            pwd=log.cleaned_data['password']
            login_true=user.objects.filter(username=unme,password=pwd).exists()
            login_truee=user.objects.filter(username=unme,password=pwd)
            print('login true is',login_truee)
            for lo in login_truee:
                print(lo) 
                print('name:',lo.name)
            if login_true:
                usrdata=user.objects.get(username=unme)
                print('userdata is:',usrdata,'usrdata object name',usrdata.name)
                request.session['userid']=usrdata.user_id
                return redirect('eshopapp:admino')
            else:
                error='incorrect username or password'
                return render(request,'login.html',{'error':error,'login':log})  
    return render(request,'login.html',{'login':log})  

def addcart(request,pid):
    pr=ProductTable.objects.get(Product_ID=pid)
    usr=user.objects.get(user_id=request.session['userid'])
    print(pr)
    qry=cart(Product_ID=pr,user_id=usr)
    
    qry_true=cart.objects.filter(Product_ID=pr,user_id=usr).exists()
    if qry_true:
        add="Already added"
        return render(request,'cartalreadyadd.html',{'add':add})
    else:        
        qry.save()
        return redirect('eshopapp:admino')
        
    
    #crt=cartform(instance=pr)
    return redirect('eshopapp:admino')

def dellogininfo(request):
    del request.session['username']
    request.session.flush()
    return redirect('eshopapp:login')

'''def buyprod(request):
    buy=buyprodform()
    pr=ProductTable.objects.all()

    return render(request,'buyprod.html',{'buy':buy,'pr':pr})'''

def cartdisplay(request):
    if 'userid' in request.session:
        cart_data=cart.objects.select_related('Product_ID').filter(user_id=request.session['userid']) #only filtering in products ordered each user
        pr=ProductTable.objects.all()
    return render(request,'addcart.html',{'cart_data':cart_data,'pr':pr})
def checkoutedit(request,pid):
    if 'userid' in request.session:
        
        ptab=ProductTable.objects.get(Product_ID=pid)
        usr=user.objects.get(user_id=request.session['userid'])
        qty=request.POST['price']
        for i in qty:
            qty_selected=i
        price=int(qty_selected)*ptab.price
        ord_date=date.today()
        exp_date=ord_date+timedelta(days=10)
        ord=orders(user_ID=usr,Product_ID=ptab,quantity=qty , TotalPrice=price,Order_date=ord_date,Expected_Delivery=exp_date)
        ordfm=orderform(instance=ord)
        ord.save()
        return render(request,'checkout.html',{'ord':ordfm})
    return render(request,'checkout.html')
