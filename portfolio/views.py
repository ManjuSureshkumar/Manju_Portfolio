from django.shortcuts import render
from django.http import JsonResponse

from .models import (
    Profile,
    Skill,
    Education,
    Experience,
    Internship,
    Service,
    Project,
    Certificate,
    Contact
)

from .forms import ContactForm


def index(request):

    profile = Profile.objects.first()

    context = {

        "profile": profile,

        "services": Service.objects.all(),

        "skills": Skill.objects.all(),

        "education": Education.objects.all(),

        "experience": Experience.objects.all(),

        "internships": Internship.objects.all(),

        "projects": Project.objects.all(),

        "certificates": Certificate.objects.all(),

        "contact_form": ContactForm(),

    }

    return render(request, "portfolio/index.html", context)


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return JsonResponse({
                "status": "success",
                "message": "Thank you! Your message has been sent successfully."
            })

        return JsonResponse({
            "status": "error",
            "message": "Please fill all required fields.",
            "errors": form.errors
        })

    return JsonResponse({
        "status": "error",
        "message": "Invalid request."
    })