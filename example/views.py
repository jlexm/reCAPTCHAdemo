from django.shortcuts import render, redirect

from .forms import ContactForm

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("VALID!")
            print(form.cleaned_data["captcha"])
            context = {"title": "Success!",
                       "result": "You're not a robot!"
                       }
            return render(request, 'result.html', context)
        else:
            print("INVALID!")
            context = {"title": "Fail!",
                       "result": "You're a robot!"
                       }
            return render(request, 'result.html', context)
    else:
        form = ContactForm()
        
    context = {"form": form}
    return render(request, 'index.html', context)

def result(request):
    
    return render(request, 'result.html')
