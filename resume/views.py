from django.shortcuts import render
from .models import Resume,Post,Portfolio
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import ContactForm
import datetime

def home(request):
    return render(request, 'resume/home.html')

def about(request):
    resume = Resume.objects.get(pk=1)
    return render(request,'resume/about.html',{"resume":resume})

#def portfolio(request):
    #return render(request,'resume/portfolio.html')

def blogpost(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'resume/blog-post.html',{'post':post})

class PostListView(ListView):
    model=Post
    template_name='resume/blog.html'
    context_object_name='posts'
    ordering=['-date']

class PortfolioView(ListView):
    model=Portfolio
    template_name='resume/portfolio.html'
    context_object_name='posts'
    ordering=['-date']

def contactview(request):
    name=''
    email=''
    subject=''
    message=''

    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        subject=form.cleaned_data.get("subject")
        message=form.cleaned_data.get("message")

        if request.user.is_authenticated:
            subjec= str(request.user) + "'is Contacting u"
        else:
            subjec= "A Visitor's Comment"


        message1= name + " with the email, " + email + ", sent the following message:\n\n" + message
        send_mail(subjec, message1, 'swawnsai@gmail.com', ['swawnsai@gmail.com'])

        context= {'form': form}
        return render(request, 'resume/contact.html')

    else:
        context= {'form': form}
        return render(request, 'resume/contact.html', context)





