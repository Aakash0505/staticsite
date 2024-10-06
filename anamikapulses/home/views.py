from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from django.apps import apps
from . import models
from django.http import HttpResponse, JsonResponse, HttpResponseGone
import random
from datetime import datetime
from django.core.validators import validate_email
import json
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from . import forms
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from .threadings import send_mail

# Create your views here.


class Index(generic.TemplateView):
    template_name = 'home/index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(Index,self).get_context_data(*args, **kwargs)
        context['form'] = forms.FormContactusView()
        context['static_obj'] = Homestatic.objects.get(id=1)
        context['team_obj'] = Team.objects.filter(published=1)
        context['category_obj'] = Category.objects.filter(published=1)
        context['product_obj'] = Product.objects.filter(published=1)

        return context


def leadCreate(request):
    if request.method == 'POST':
        form = request.POST.get('form', '').strip()
        

        status = "Successfully subscribed"
        try:
            contactform = forms.FormContactusView(request.POST, request.FILES)
            print(contactform)
            resume = contactform.cleaned_data['document']
            print(resume)
            if contactform.is_valid():
                name = contactform.cleaned_data['name']
                phone_no = contactform.cleaned_data['contact_no'] 
                email_id = contactform.cleaned_data['email_id']  
                area_of_interest = contactform.cleaned_data['area_of_interest']  
                message = contactform.cleaned_data['message'] 
                status = "Successfully subscribed"
                subject = 'Contact us - Thankyou'
                subject_admin = 'Contact us Enquiry'
                email_body = render_to_string("emailers/contactus_email_thankyou.html",
                                            {"object":{'name':name,}})
                email_body_admin = render_to_string("emailers/contactus_email_admin.html",
                                                    {"object": {'name':name,'email_id':email_id,'contact_no':phone_no,
                                                                'area_of_interest':area_of_interest,'message':message,}})
                # user mail
                send_mail(subject=subject, template_object=email_body, from_email=settings.FROM_EMAIL, to=[email_id], resume=None,
                    fail_silently=False)
                # admin mail
                send_mail(subject=subject_admin, template_object=email_body_admin, from_email=settings.FROM_EMAIL, to=['aakashagrawal552@gmail.com'], resume=resume,
                    fail_silently=False)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'An error occurred while processing your request.'}, status=400)
        ctx = {'status': status}
        return JsonResponse(ctx, status=200)

    return HttpResponse(json.dumps({'msg':'success'}), content_type='application/json')


# class Index(SuccessMessageMixin, generic.CreateView):
#     template_name = 'careers/careers.html'
#     form_class = forms.FormCareersView 
#     success_url = reverse_lazy('careers:thankyou')
#     success_message = "Thank you for Contacting us, Our team wil get\
#                        back to you..!"
    
#     def get_context_data(self, *args, **kwargs):
#         context = super(Index,self).get_context_data(*args, **kwargs)
        
#         context['static_obj'] = models.CareerStatic.objects.get(id=1)
#         context['foundation_obj'] = models.Foundation.objects.filter(published=1)
#         context['testimonial_obj'] = models.Testimonial.objects.filter(published=1)
#         context['openings_obj'] = models.JobOpenings.objects.filter(published=1)

#         return context