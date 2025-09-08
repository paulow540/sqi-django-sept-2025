from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "testimonials": {
            "Dan": "Good service",
            "Paul": "Bad service"
        },
        "services": {
            "Designing logos": 5000,
            "Backend devlopment": 25_000_000,
            
        }
    }

    return render(request, "freelancer/home.html", context)



def services_view(request):
    services ={"services": ["Web Development", "Mobile App Development", "Data Analysis", "AI Solutions"]}
    return render(request, "freelancer/services.html",  services)

def testimonials_view(request):
    testimonials = {
        "Alice Johnson": "Amazing service! They delivered beyond my expectations.",
        "Michael Smith": "Professional team with outstanding results.",
        "Sarah Lee": "I highly recommend their services to anyone."
    }
    return render(request, "freelancer/testimonials.html",  testimonials)

def pricing_view(request):
    pricing = {
        "Web Development": 1200,
        "Mobile App Development": 1500,
        "Data Analysis": 800,
        "AI Solutions": 2000
    }
    return render(request, "pricing.html",  pricing)
