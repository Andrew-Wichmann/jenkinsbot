from django import forms
import os
from jenkinsapi.jenkins import Jenkins

JENKINS_URL = os.environ.get("JENKINS_URL", 'http://localhost')
#JENKINS_PORT = os.environ.get('JENKINS_PORT', 8080)
JENKINS_USER = os.environ.get('JENKINS_USER', 'admin')
JENKINS_PASSWORD = os.environ.get('JENKINS_PASSWORD', 'cf4a43911dc24937bbd1092c6881b708')
#J = Jenkins(f"{JENKINS_URL}:{JENKINS_PORT}", JENKINS_USER, JENKINS_PASSWORD)
J = Jenkins(f"{JENKINS_URL}", JENKINS_USER, JENKINS_PASSWORD)

class JobForm(forms.Form):
    job = forms.ChoiceField(choices=[(job, job) for job in J.keys()])
