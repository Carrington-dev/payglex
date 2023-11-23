import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from myauth.models import NewUser, Profile
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.mail import  send_mass_mail
from django.contrib import messages


from time import sleep
from django import template
from payglen import settings
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator

# socket.getaddrinfo('localhost', 8080)



# 
# @shared_task
def send_verification_email(modeladmin, request, queryset):
    sleep(5)

    """Task to send an e-mail notification when an order is successfully created."""
    # """
    for user in queryset:
        subject = "Verify your account"
        plaintext = template.loader.get_template('registration/password_reset_email.txt')
        htmltemp = template.loader.get_template('email/confirm_real.html')
        # htmltemp = template.loader.get_template('registration/password_reset_email.html')
        c = { 
        "email":user.email,
        'domain':request.META['HTTP_HOST'],
        'site_name': 'Carrington Driving Academy',
        "uid": urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
        "user": user,
        'token': default_token_generator.make_token(user),
        'protocol': request.scheme,
        'web_link':  request.scheme + "://" + request.META['HTTP_HOST'] + "/"
        }
        text_content = plaintext.render(c)
        html_content = htmltemp.render(c)
        try:
            msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [user.email], headers = {'Reply-To': f'{user.email}'})
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'You have successfully sent verification emails to {user.email}')
            return 
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        # """

    return


def make_tutor(modeladmin, request, queryset):
    queryset.update(is_teacher=True)
    queryset.update(is_admin=True)
    queryset.update(is_staff=True)
    queryset.update(is_superuser=False)
    # send_mass_mail()

def approve_tutor(modeladmin, request, queryset):
    queryset.update(occupation='Approved Tutor')

def put_on_probation(modeladmin, request, queryset):
    queryset.update(occupation='On Probation')

def make_applicant(modeladmin, request, queryset):
    queryset.update(occupation='Applicant Tutor')

def cancel_tutor(modeladmin, request, queryset):
    queryset.update(occupation='Cancelled')



def publish(self, request, queryset):
    queryset.update(status="published")

def mark_as_viewed(self, request, queryset):
    queryset.update(viewed=True)

mark_as_viewed.short_description = "Mark as read"
send_verification_email.short_description = "Send verification email to selected users"

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
            filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'

# Register your models here.
@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    '''Admin View for NewUser'''

    
    list_display = ('id','username','email', 'first_name','last_name','phone','country', 'is_teacher', 'is_verified', 'is_active', 'is_staff','is_admin','is_superuser') 
    readonly_fields=('date_joined', 'last_login', 'password','username','email', 'is_active')
    actions = [make_tutor, send_verification_email]# export_to_csv]
    search_fields = ['email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('user','occupation','preview', 'last_name', 'first_name')
    list_filter = ('occupation',)
    ordering = ('user',)
    actions = [approve_tutor, put_on_probation, make_applicant, cancel_tutor, export_to_csv]

    @mark_safe
    def preview(self, obj):
        template = u"""<img src="{url}" style="max-height: {size};" />"""
        config = {
            'image_field': 'image',
            'image_size': '50px',
        }
        custom_config = getattr(self, 'fancy_preview', {})
        config.update(custom_config)
        image = getattr(obj, config['image_field'], None)
        url = image.url if image else ''
        return template.format(url=url, size=config['image_size'])
    preview.short_description=_('preview')
    preview.allow_tags = True

    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name

"""
@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    '''Admin View for APIKey'''

    list_display = ('api_key', 'secret_key', 'user')
    # list_filter = ('',)
    readonly_fields = ('api_key', 'secret_key', 'user')
    search_fields = ('api_key', 'secret_key', 'user')
    # date_hierarchy = ''
    ordering = ('-pk',)

"""
