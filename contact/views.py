from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactView
from django.core.mail import EmailMessage


def contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            email = EmailMessage(subject='I love subject', body='I love body',
                                 from_email="sophie.flynn321@gmail.com", to=['request.POST.email'])
            email.send()
            our_form = form.save(commit=False)
            our_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent. Thank you.')
        return HttpResponseRedirect('/')
    else:
        form = ContactView()
        return render(request, 'contact.html', {'form': form})

