from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Job,Category,Company, Tech_included,Job_Application
from django.http import HttpResponse

def index(request):
    jobs = Job.objects.order_by('-post_date').filter(is_featured=True)
    paginator = Paginator(jobs,3)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)
    context = {
         'jobs' : paged_jobs
     }
    return render(request, 'jobs/job_list.html', context)


def job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {
        'job': job
    }
    return render(request, 'jobs/job_single.html', context)




def search(request):
    jobs = Job.objects.order_by('-post_date').filter(is_featured=True)
    
    # if title in search keyword
    if 'title' in request.GET:
        title = request.GET.get('title')
        if title:
            jobs =jobs.filter(title__icontains = title)
            
    #  if    location in search keyword  
    if 'location' in request.GET:
        location = request.GET.get('location')
        if location:
            jobs =jobs.filter(location__iexact = location)
    context = {
        'jobs':jobs,
    
        'values': request.GET    
        
    }

    return render (request, 'jobs/search.html', context)


def apply(request):
    if request.method == 'POST':

        job_id = request.POST.get('job_id')
        job = request.POST.get('job')
        name = request.POST.get('name')
        cv = request.POST.get('cv')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        company_email = request.POST.get('company_email')



        #check if user has already applied

        if request.user.is_authenticated:
            user_id = request.user.id
            has_applied = Job_Application.objects.all().filter(job_id=job_id, user_id=user_id)
            if has_applied:
                messages.error(request, 'you have already applied for this job')
                return redirect('job/job_id' )

        apply = Job_Application( job=job, job_id=job_id,  name=name, email=email, phone=phone, cv=cv, message=message, user_id=user_id)
        apply.save()

        #send send_mail
        send_mail(
           'Job  listing application',
           'there has been an application for ' +job+ '. sign into the admin parnel for to review',
           'ianmuhia3@gmail.com',
           ['ianmuhiajohn@gmail.com'],
           fail_silently=False
        )
        messages.success(request, 'your request has been submitted,  will get back to you soon')

        return redirect('index')