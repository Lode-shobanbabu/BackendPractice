from django.shortcuts import render, redirect, get_object_or_404
from .models import SiteHeader, Hero, About, Service, Feature, WhyChooseItem, Footer, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    context = {
        'site_header': SiteHeader.objects.first(),
        'hero': Hero.objects.first(),
        'about': About.objects.first(),
        'services': Service.objects.all(),
        'features': Feature.objects.all(),
        'whychoose': WhyChooseItem.objects.all(),
        'footer': Footer.objects.first(),
    }
    return render(request, 'core/index.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'core/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


# ---------------------- DASHBOARD VIEWS ----------------------

@login_required(login_url='login')
def dashboard_home(request):
    """Default dashboard page"""
    return render(request, 'core/dashboard.html')


@login_required(login_url='login')
def dashboard_hero(request):
    hero = Hero.objects.first() or Hero.objects.create()
    if request.method == "POST":
        hero.title = request.POST.get('title', '').strip()
        hero.subtitle = request.POST.get('subtitle', '').strip()
        hero.button_text = request.POST.get('button_text', '').strip()
        hero.button_url = request.POST.get('button_url', '').strip()
        hero.image_path = request.POST.get('image_path', '').strip()
        hero.save()
        messages.success(request, "Hero section updated successfully!")
        return redirect('dashboard_hero')
    return render(request, 'core/dashboard_hero.html', {'hero': hero})


@login_required(login_url='login')
def dashboard_about(request):
    about = About.objects.first() or About.objects.create()
    if request.method == "POST":
        about.small_title = request.POST.get('small_title', '').strip()
        about.heading = request.POST.get('heading', '').strip()
        about.content = request.POST.get('content', '').strip()
        about.image_path = request.POST.get('image_path', '').strip()
        about.save()
        messages.success(request, "About section updated successfully!")
        return redirect('dashboard_about')
    return render(request, 'core/dashboard_about.html', {'about': about})


@login_required(login_url='login')
def dashboard_services(request):
    services = Service.objects.all()

    # Add new service
    if request.method == "POST" and request.POST.get('action') == 'add':
        Service.objects.create(
            title=request.POST.get('title', '').strip(),
            description=request.POST.get('description', '').strip(),
            image_path=request.POST.get('image_path', '').strip(),
            icon_path=request.POST.get('icon_path', '').strip()
        )
        messages.success(request, "Service added successfully!")
        return redirect('dashboard_services')

    # Update service
    if request.method == "POST" and request.POST.get('action') == 'update':
        s = get_object_or_404(Service, id=request.POST.get('id'))
        s.title = request.POST.get('title', '').strip()
        s.description = request.POST.get('description', '').strip()
        s.image_path = request.POST.get('image_path', '').strip()
        s.icon_path = request.POST.get('icon_path', '').strip()
        s.save()
        messages.success(request, "Service updated successfully!")
        return redirect('dashboard_services')

    # Delete service
    delete_id = request.GET.get('delete')
    if delete_id:
        Service.objects.filter(id=delete_id).delete()
        messages.success(request, "Service deleted successfully!")
        return redirect('dashboard_services')

    return render(request, 'core/dashboard_services.html', {'services': services})


@login_required(login_url='login')
def dashboard_features(request):
    features = Feature.objects.all()

    # Add feature
    if request.method == "POST" and request.POST.get('action') == 'add':
        Feature.objects.create(
            title=request.POST.get('title', '').strip(),
            description=request.POST.get('description', '').strip(),
            icon_path=request.POST.get('icon_path', '').strip()
        )
        messages.success(request, "Feature added successfully!")
        return redirect('dashboard_features')

    # Update feature
    if request.method == "POST" and request.POST.get('action') == 'update':
        f = get_object_or_404(Feature, id=request.POST.get('id'))
        f.title = request.POST.get('title', '').strip()
        f.description = request.POST.get('description', '').strip()
        f.icon_path = request.POST.get('icon_path', '').strip()
        f.save()
        messages.success(request, "Feature updated successfully!")
        return redirect('dashboard_features')

    # Delete feature
    delete_id = request.GET.get('delete')
    if delete_id:
        Feature.objects.filter(id=delete_id).delete()
        messages.success(request, "Feature deleted successfully!")
        return redirect('dashboard_features')

    return render(request, 'core/dashboard_features.html', {'features': features})


@login_required(login_url='login')
def dashboard_whychoose(request):
    items = WhyChooseItem.objects.all()

    # Add item
    if request.method == "POST" and request.POST.get('action') == 'add':
        WhyChooseItem.objects.create(
            title=request.POST.get('title', '').strip(),
            description=request.POST.get('description', '').strip(),
            icon_path=request.POST.get('icon_path', '').strip()
        )
        messages.success(request, "Item added successfully!")
        return redirect('dashboard_whychoose')

    # Update item
    if request.method == "POST" and request.POST.get('action') == 'update':
        w = get_object_or_404(WhyChooseItem, id=request.POST.get('id'))
        w.title = request.POST.get('title', '').strip()
        w.description = request.POST.get('description', '').strip()
        w.icon_path = request.POST.get('icon_path', '').strip()
        w.save()
        messages.success(request, "Item updated successfully!")
        return redirect('dashboard_whychoose')

    # Delete item
    delete_id = request.GET.get('delete')
    if delete_id:
        WhyChooseItem.objects.filter(id=delete_id).delete()
        messages.success(request, "Item deleted successfully!")
        return redirect('dashboard_whychoose')

    return render(request, 'core/dashboard_whychoose.html', {'whychoose': items})


@login_required(login_url='login')
def dashboard_footer(request):
    footer = Footer.objects.first() or Footer.objects.create()
    if request.method == "POST":
        footer.about_text = request.POST.get('about_text', '').strip()
        footer.contact_email = request.POST.get('contact_email', '').strip()
        footer.contact_phone = request.POST.get('contact_phone', '').strip()
        footer.contact_address = request.POST.get('contact_address', '').strip()
        footer.copyright_text = request.POST.get('copyright_text', '').strip()
        footer.save()
        messages.success(request, "Footer updated successfully!")
        return redirect('dashboard_footer')
    return render(request, 'core/dashboard_footer.html', {'footer': footer})


# ---------------------- CONTACT FORM ----------------------

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message_text = request.POST.get('message', '').strip()

        contact_entry = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message_text
        )

        subject = f"New Contact Message from {name}"
        message_body = (
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message_text}\n"
            f"Submitted at: {contact_entry.submitted_at.strftime('%d %b %Y, %I:%M %p')}"
        )

        try:
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                ['shobanbabulode291@gmail.com'],
                fail_silently=False,
            )
        except Exception as e:
            print("Email sending failed:", e)

        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')

    return redirect('home')
