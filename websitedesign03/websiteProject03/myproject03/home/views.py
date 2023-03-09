from django.shortcuts import render

from home.models import WhyChooseUs, MeetTheTeamMembers


# Create your views here.
def home(request):
    whyObj =  WhyChooseUs.objects.all()
    memberObj = MeetTheTeamMembers.objects.all()
    return render(request, 'index.html', {'whyResult': whyObj, 'memberResult': memberObj})