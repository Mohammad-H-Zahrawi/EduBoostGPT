from django.shortcuts import render, redirect 
from django.urls import reverse
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.conf import settings
from projects.models import TrackTeacherModel, ExamGPTModel, Donate, ContactUs
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect
from django.conf import settings



YOUR_DOMAIN = 'http://127.0.0.1:8000'



def hii(request):

    return render(request, 'homepage/hii.html')   



# def record(request, sec=7):
#     import sounddevice as sd
#     from scipy.io.wavfile import write
#     import wavio as wv
#     # Sampling frequency
#     freq = 44100
#     # Recording duration
#     duration = 5
#     # Start recorder with the given values
#     # of duration and sample frequency
    
#     recording = sd.rec(int(duration * freq),
#                     samplerate=freq, channels=2)
#     # Record audio for the given number of seconds
#     sd.wait()
#     # This will convert the NumPy array to an audio
#     # file with the given sampling frequency
#     write("recording0.wav", freq, recording)
    
#     # Convert the NumPy array to audio file
#     wv.write("recording1.wav", recording, freq, sampwidth=2)
#     return render(request, 'homepage/hii.html')   



def home(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name_contact_us')
        last_name = request.POST.get('last_name_contact_us')
        email = request.POST.get('email_contact_us')
        number = request.POST.get('number_contact_us')
        inquiry = request.POST.get('inquiry_contact_us')
        
        ContactUs.objects.create(first_name_contact_us=first_name, last_name_contact_us=last_name, email_contact_us=email, number_contact_us=number,  inquiry_contact_us=inquiry).save()
        
        return render(request, 'homepage/thankyouforsubmitting.html')
    return render(request, 'homepage/Home.html')

def thankyouforsubmitting(request):
    return render(request, 'homepage/thankyouforsubmitting.html')

def success(request):
    return render(request, 'homepage/success.html')
def cancel(request):
    return render(request, 'homepage/cancel.html')   
    
def donate(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        Donate.objects.create(full_name=full_name, email=email, amount=amount).save()
        
        context = {'amount':amount}
        return render(request, 'homepage/donate.html', context=context)

    return render(request, 'homepage/donate.html')
  



