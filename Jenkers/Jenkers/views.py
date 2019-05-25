import os
import subprocess

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from jenkinsapi.jenkins import Jenkins

from .forms import JobForm

JENKINS_URL = os.environ.get("JENKINS_URL", 'http://localhost')
#JENKINS_PORT = os.environ.get('JENKINS_PORT', 8080)
JENKINS_USER = os.environ.get('JENKINS_USER', 'admin')
JENKINS_PASSWORD = os.environ.get('JENKINS_PASSWORD', 'cf4a43911dc24937bbd1092c6881b708')
#J = Jenkins(f"{JENKINS_URL}:{JENKINS_PORT}", JENKINS_USER, JENKINS_PASSWORD)
J = Jenkins(f"{JENKINS_URL}", JENKINS_USER, JENKINS_PASSWORD)

def get_jobs(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JobForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            job = form.cleaned_data['job']
            status = J[job].get_last_build().get_status()
            try:
                subprocess.check_output(['python ' + os.path.join(settings.BASE_DIR,'flipjenkins.py')+ ' ' + ' '.join([status, job])], stderr=subprocess.STDOUT, shell=True)
                form = JobForm()
                return render(request, 'jobs.html', {'form': form, 'success': True, "job": job, "status": status})
            except subprocess.CalledProcessError as e:
                return render(request, 'jobs.html', {'form': form, 'error': True, 'error_message': e.output})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = JobForm()

    return render(request, 'jobs.html', {'form': form})
