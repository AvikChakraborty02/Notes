from django.shortcuts import render
from notesapp.models import User,Notes,Feedback,Admin
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
def index(req):
    return render(req,'index.html')

def login(req):
    return render(req,'login.html')

def admin_login(req):
    return render(req,'admin_login.html')

def admin_home(req):
    return render(req,'admin_home.html')

def admin_feedback(req):
    allFeedback=Feedback.objects.all()
    data={"allFeedback":list(allFeedback)}
    return render(req,'admin_feedback.html',data)

def admin_users(req):
    allUsers= User.objects.all()
    data = {"allUsers": list(allUsers)}
    return render(req,'admin_users.html',data)

def deletefeedback(req,id):
    obj=Feedback.objects.get(id=id)
    obj.delete()
    return redirect('admin_feedback')

def deleteuser(req,id):
    obj=User.objects.get(id=id)
    emailid=obj.emailid
    obj1=Notes.objects.filter(emailid=emailid)
    obj1.delete()
    obj.delete()
    return redirect('admin_users')

def logout(req):
    try:
        del req.session['email']
    except KeyError:
        pass
    return render(req,'index.html')

def registration(req):
    return render(req,'registration.html')

def forgot_password(req):
    return render (req,'forgot_password.html')

def home(req):
    emailid=req.session.get('emailid')
    username=User.objects.get(emailid=emailid)
    allNotes=Notes.objects.filter(emailid=emailid)
    data={'allNotes':list(allNotes),'username':username}
    return render(req,'home.html',data)

def view_content(req,id):
    return render(req,'view_content.html')

def view(req,id):
    content=Notes.objects.get(id=id)
    data={'content':content}
    return render(req,'view_content.html',data)

def aboutus(req):
    return render(req,'aboutus.html')

def contactus(req):
    return render(req,'contactus.html')

def add_notes(request):
    emailid=request.session.get('emailid')
    data={
        'email':emailid,
    }
    return render(request,'add_notes.html',data)

def admin_login_verification(request):
    if request.method == 'POST':
        emailid = request.POST['emailid']
        password = request.POST['password']
        storage = messages.get_messages(request)
        storage.used = True

        admin = Admin.objects.filter(emailid=emailid, password=password)

        if len(admin) > 0:
            request.session['emailid'] = emailid
            return redirect('admin_home')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('admin_login')
    else:
        return render(request, '')
    
def save_admin(request):
    if request.method == 'POST':
        emailid=request.POST["emailid"]
        password=request.POST["password"]
        if Admin.objects.filter(emailid=emailid).exists():
            messages.info(request, 'Email is already taken')
            return redirect(admin_home)
        else:
            admin = Admin.objects.create(emailid=emailid,password=password)
            messages.info(request,"Registration Successful")
            return redirect(admin_home)
    else:       
        return render(request,'admin_home.html')


def save(request):
    if request.method == 'POST':
        name=request.POST["name"]
        emailid=request.POST["emailid"]
        password=request.POST["password"]
        if User.objects.filter(emailid=emailid).exists():
            messages.info(request, 'Email is already taken')
            return redirect(registration)
        else:
            user = User.objects.create(name=name,emailid=emailid,password=password)
            messages.info(request,"Registration Successful")
            return redirect(registration)
    else:       
        return render(request,'registration.html')

def login_verification(request):
    if request.method == 'POST':
        emailid = request.POST['emailid']
        password = request.POST['password']
        storage = messages.get_messages(request)
        storage.used = True

        user = User.objects.filter(emailid=emailid, password=password)

        if len(user) > 0:
            request.session['emailid'] = emailid
            return redirect('home')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('login')
    else:
        return render(request, '')
    
def savecontent(request):
    if request.method=='POST':
        emailid=request.POST['emailid']
        title=request.POST['title']
        content=request.POST['content']

        new_note=Notes.objects.create(emailid=emailid,title=title,content=content)
        new_note.save()
        return redirect('home')
    else:
        return render(request,'add_notes.html')
    
def delete (request,id):
    obj=Notes.objects.get(id=id)
    obj.delete()
    allcontent=Notes.objects.all()
    data={"content":allcontent}
    return redirect('home')
    
def edit_content(req,id):
    value=Notes.objects.get(id=id)
    emailid=req.session.get('emailid')
    data={'content':value,'emailid':emailid}
    return render(req,"edit_content.html",data)

def update(req,id):
    emailid=req.POST['emailid']
    title=req.POST['title']
    content=req.POST['content']
    obj=Notes.objects.get(id=id)
    obj.emailid=emailid
    obj.title=title
    obj.content=content

    obj.save()
    allContent=Notes.objects.all()
    data={"content":list(allContent),}

    return redirect('home')

def feedback(request):
    emailid=request.session.get('emailid')
    obj=User.objects.get(emailid=emailid)
    data={
        'obj':obj,
    }
    return render(request,'feedback.html',data)

def give_feedback(request):
    if request.method=='POST':
        emailid=request.POST['emailid']
        name=request.POST['name']
        feedback=request.POST['feedback']

        new_note=Feedback.objects.create(emailid=emailid,name=name,feedback=feedback)
        new_note.save()
        return redirect('home')
    else:
        return render(request,'feedback.html')

def change_password(request):
    if request.method == 'POST':
        emailid=request.POST['emailid']
        old_password=request.POST['old_password']
        new_password=request.POST['new_password']
        storage = messages.get_messages(request)
        storage.used = True

        if User.objects.filter(emailid=emailid).exists():
            user=User.objects.get(emailid=emailid)
            if(old_password==user.password):
                user.password=new_password
                user.save()
                messages.info(request, 'You have successfully changed your password')
                return redirect(forgot_password)
            else:
                messages.info(request,'Old password is not matching.Try Again!!')
                return render(request,'forgot_password.html')
        else:
            messages.info(request,'Entered email does not exists')
            return render(request,'forgot_password.html')
    
    else:
        return redirect('login.html')