from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import PrayerForm, BookshopForm, choirForm
from django.views.generic import ListView, View
from .models import Praye, Counsel, Invite, Ivpg, Testimony, WOFBI, Bookshop, PDF, Choir, Security, Decoration, CHILDREN,\
    PF, HOSPITALITY, PROPHET_FOCUS, BOOKS_of_the_Months, Recommended_Books, WSF, SPIRITUAL, Recommended_Books_Time,\
    TECHNICAL, USHERING, Services, Category,  Video, SANCTUARY, TRANSPORTATION, HARVESTER, HEALTH_WORKERS, DRAMA,\
    ChoirPage1, ChoirPage2, HomeCarousel, ChoirSong, CA, Contact, Pastor_Desk
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages



# from django.views.generic import TemplateView
# from django.core.files.storage import FileSystemStorage
# from .forms import BookForm, ContactForm, YafContactForm
# from .models import Carousel, Post, PostImage, Book, Video, Topic,  Tropic,Dentry, Bookshop, Contact, Now, YafContact
#
# from django.contrib import messages





#
def About(request):
    return render(request, 'b/aboutus.html')






def service(request):
    # first_sms = Services.objects.first()
    side_sms = Services.objects.all()
    three_category = Category.objects.all()
    context = {
        # 'first_sms' : first_sms,
        'side_sms' : side_sms,
        'three_category' : three_category
    }
    return  render(request, 'b/test.html', context)

def all_message(request):
    all_sms = Services.objects.all()
    context = {
        'all_sms': all_sms
    }
    return render(request, 'b/3.html', context)

def MDetail(request, id):
    sms = Services.objects.get(pk=id)
    # category = Category.objects.get(id=sms.category.id)
    # rel_name = Services.objects.filter(category=category) #.excluded(id=id)

    context = {
        'sms': sms,
        # 'rel_name': rel_name
    }
    return render(request, 'b/2.html', context)

def all_category(request):
    cats = Category.objects.all()
    context = {
        'cats' : cats,
    }
    return render(request, 'b/a.html', context)

def category(request, id):
    category = Category.objects.get(id=id)
    sms = Services.objects.filter(category=category)
    context = {
        'all_news': sms,
        'category': category,
    }
    return render(request, 'b/b.html', context)

def Transport(request):

    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        t = TRANSPORTATION (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        t.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/trans.html')

def Gilead(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = HEALTH_WORKERS (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/health.html')



def drama(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = DRAMA (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/joel.html')

def cool(request):
    return render(request, 'b/ade.html')

def domi(request):
    return render(request, 'b/domi.html')

def ushering(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = USHERING (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/usher.html')



def Home(request):
    img = HomeCarousel.objects.all()

    context = {
        'img':img
    }
    return render(request, 'b/d.html', context)

def Pillars(request):
    return render(request, 'b/pillar.html')

def Communion(request):
    return render(request, 'b/ara_ati_eje_JESU.html')

def cell(request):
    wsf = WSF.objects.all()
    context = {
        'wsf':wsf
    }
    return render(request, 'b/wsf.html', context)

def giving(request):
    a = CA.objects.all()

    context = {
        'a': a
    }
    return render(request, 'b/giv.html', context)


def bfc(request):
    return render(request, 'b/bfc.html')


def Studio(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = TECHNICAL (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/studio.html')

def SpWE(request):
    week = SPIRITUAL.objects.all()
    context = {
        'week': week
    }
    return render(request,'b/spiritual.html', context)


def Book_of_Month(request):
    recommended = Recommended_Books.objects.all()
    record = Recommended_Books_Time.objects.all()
    context = {
        'recommended': recommended,
        'record':record
    }
    return render(request, 'b/b_o_m.html', context)

def Monthly(request):
    focus = PROPHET_FOCUS.objects.all()
    # author = Author.objects.all()
    book = BOOKS_of_the_Months.objects.all()
    context = {
        'focus' : focus,
        # 'author' : author,
        'book' : book,
    }
    return render(request, 'b/focus.html', context)


def prayerforce(request):
    pf = PF.objects.all()
    context = {
        'pf':pf
    }
    return render(request, 'b/p_force.html', context)

def hospitality(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = HOSPITALITY (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request,'b/hosp.html')
        # return render(request, 'b/hosp.html', messages.error('FORM NOT CORRECTLY FILED TRY AGAIN'))

def Santuary(request):
    if request.method =='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = SANCTUARY (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request,'b/santkeeper.html')


def children(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = CHILDREN (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/children.html')

def decorate(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        design_experience = request.POST.get('design_experience', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        d = Decoration (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            design_experience=design_experience,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        d.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/decorate.html')
def Growth(request):
    return render(request, 'b/growth_mandate.html')

def Resources(request):
    pdf = PDF.objects.all()
    context = {
        'pdf':pdf
    }
    return render(request, 'b/pdf.html', context)
#
def Pastor_desk(request):
    desk = Pastor_Desk.objects.all()
    context = {
        'desk': desk
    }
    return render(request, 'b/pastors_desk.html', context)

def choir(request):

    car = ChoirPage1.objects.all()
    card = ChoirPage2.objects.all()

    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        church = request.POST.get('church', '')
        date_of_new_birth = request.POST.get('date_of_new_birth', '')
        instrument = request.POST.get('instrument', '')
        foundation_class = request.POST.get('foundation_class', '')
        part_sing = request.POST.get('part_sing', '')
        marital_status = request.POST.get('marital_status', '')
        message = request.POST.get('message', '')

        g = Choir(
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            church=church,
            date_of_new_birth=date_of_new_birth,
            instrument=instrument,
            foundation_class=foundation_class,
            part_sing=part_sing,
            marital_status=marital_status,
            message=message
        )
        g.save()
        return redirect('b:this-year')
    context = {
        'obj': obj,
        'car': car,
        'card': card
    }
    return render(request, 'b/akorin.html', context)

def choirsong(request):
    orin = ChoirSong.objects.all()

    context = {
        'orin': orin
    }
    return render(request, 'b/orin.html', context)





def security(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        s = Security (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        s.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/security.html')

def Wofbi(request):
    wofbi = WOFBI.objects.all()
    context = {
        'wofbi': wofbi
    }
    return render(request, 'b/wofbi.html', context)




def PrayerView(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residential = request.POST.get('residential', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        church = request.POST.get('church', '')
        city = request.POST.get('city', '')
        call = request.POST.get('call', '')
        pray_for = request.POST.get('pray_for', '')
        prayer = request.POST.get('prayer', '')

        p = Praye(
            full_name=full_name,
            residential=residential,
            email=email,
            phone=phone,
            church=church,
            city=city,
            call=call,
            pray_for=pray_for,
            prayer=prayer
        )
        p.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/request.html')




def Counselling(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residential = request.POST.get('residential', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        church = request.POST.get('church', '')
        city = request.POST.get('city', '')
        call = request.POST.get('call', '')
        counsel = request.POST.get('counsel', '')
        message = request.POST.get('message', '')

        c = Counsel (
                full_name=full_name,
                residential=residential,
                email=email,
                phone=phone,
                church=church,
                city=city,
                call=call,
                counsel=counsel,
                message=message
            )
        c.save()
        return redirect('b:home')

    return render(request, 'b/counselling.html')



def About(request):
    return render(request, 'b/aboutus.html')


def Prophetic_Decleration(request):

    return render(request, 'b/this-year.html')


def Books(request):

    if request.method == "POST":
        form = BookshopForm(request.POST)
        if form.is_valid():
            buyer_name =  form.cleaned_data.get('buyer_name')
            mailing_address =  form.cleaned_data.get('mailing_address')
            email =  form.cleaned_data.get('email')
            book =  form.cleaned_data.get('book')
            copies =  form.cleaned_data.get('copies')
            phone =  form.cleaned_data.get('phone')
            message =  form.cleaned_data.get('message')

            b = Bookshop(
                buyer_name=buyer_name,
                mailing_address=mailing_address,
                email=email,
                book=book,
                copies=copies,
                phone=phone,
                message=message
            )
            b.save()
            return redirect('b:this-year')
    else:
        form = BookshopForm()

    return render(request, 'b/bookshop.html', {'form':form})


def Invitee(request):
    posts = Ivpg.objects.all()
    if request.method == "POST":
        y_full_name = request.POST.get('y_full_name', '')
        y_email = request.POST.get('y_email', '')
        next_sunday_date = request.POST.get('next_sunday_date', '')
        y_friend_full_name = request.POST.get('y_friend_full_name', '')
        y_friend_email = request.POST.get('y_friend_email', '')
        theme = request.POST.get('theme', '')
        message = request.POST.get('message', '')

        i = Invite(
            y_full_name=y_full_name,
            y_email=y_email,
            next_sunday_date=next_sunday_date,
            y_friend_full_name=y_friend_full_name,
            y_friend_email=y_friend_email,
            theme=theme,
            message=message
        )
        i.save()
        return redirect('b:this-year')
    context = {
        'posts': posts
    }

    return render(request, 'b/invite-a-friend.html', context)

def upload(request):
    videos = Video.objects.all()
    paginator = Paginator(videos, 4)
    page = request.GET.get('page')

    try:
        videos = paginator.page(page)

    except PageNotAnInteger:
        videos = paginator.page(1)

    except EmptyPage:
        test = paginator.page(paginator.num_pages)
    context = {
        'videos': videos,
        'page': page
    }
    return render(request, 'b/upload.html', context)

def Testy(request):
    test = Testimony.objects.all()
    paginator = Paginator(test, 2)
    page = request.GET.get('page')

    try:
        test = paginator.page(page)

    except PageNotAnInteger:
        test = paginator.page(1)

    except EmptyPage:
        test = paginator.page(paginator.num_pages)
    context = {
        'test': test,
        'page': page
    }
    return render(request, 'b/testimonies.html', context)

def Harvester(request):
    if request.method=='POST':
        full_name = request.POST.get('full_name', '')
        residence = request.POST.get('residence', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        born_again = request.POST.get('born_again', '')
        joined_date = request.POST.get('joined_date', '')
        new_birth_date = request.POST.get('new_birth_date', '')
        occupation = request.POST.get('occupation', '')
        foundation_class = request.POST.get('foundation_class', '')
        job = request.POST.get('job', '')
        status = request.POST.get('status', '')
        message = request.POST.get('message', '')

        e = HARVESTER (
            full_name=full_name,
            residence=residence,
            email=email,
            phone=phone,
            city=city,
            born_again=born_again,
            joined_date=joined_date,
            new_birth_date=new_birth_date,
            occupation=occupation,
            foundation_class=foundation_class,
            job=job,
            status=status,
            message=message
        )
        e.save()
        return redirect('b:this-year')
    else:
        return render(request, 'b/harvest.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        c = Contact(name=name, email=email, message=message)
        c.save()
        return render(request, 'b/cont.html', {
            'name': name,
            'email': email,
            'navbar': 'cont'
        })
    context = {

        'navbar': 'cont'
    }

    return render(request, 'b/cont.html', context)



def gal(request):
    return render(request, 'b/img.html')




#
#
#
# def blog_view(request):
#     posts = Post.objects.all()
#     return render(request, 'b/archies.html', {'posts': posts })
#
# def detail_view(request, id):
#     post = get_object_or_404(Post, id=id)
#     photos = PostImage.objects.filter(post=post)
#     return render(request, 'b/og.html', {
#         'post': post,
#         'photos': photos
#     })
#
# def upload(request):
#     videos = Video.objects.all()
#     return render(request, 'b/upload.html', {
#         'videos': videos
#     })
#
# def services(request):
#     return render(request, 'b/sss.html', {})
#
#
# def wsf(request):
#     books = Book.objects.all()
#     return render(request,'b/wsf_list.html', {
#         'books': books
#     })
#
# def get(self, *args, **kwargs):
    #     form = PrayerForm
    #     context = {
    #         'form':form
    #     }
    #     return render(self.request, 'b/request.html', context)
    #
    # def post(self, *args, **kwargs):
    #     form = PrayerForm(self.request.POST or None)
    #     if form.is_valid():
    #         full_name = form.cleaned_data.get('full_name')
    #         residential = form.cleaned_data.get('residential')
    #         email = form.cleaned_data.get('email')
    #         phone = form.cleaned_data.get('phone')
    #         church = form.cleaned_data.get('church')
    #         city = form.cleaned_data.get('city')
    #         call = form.cleaned_data.get('call')
    #         pray_for = form.cleaned_data.get('pray_for')
    #         prayer = form.cleaned_data.get('prayer')
    #
    #         prayer_request = Prayer (
    #             full_name=full_name,
    #             residential=residential,
    #             email=email,
    #             phone=phone,
    #             church=church,
    #             city=city,
    #             call=call,
    #             pray_for=pray_for,
    #             prayer=prayer
    #         )
    #         prayer_request.save()
    #         print(form.cleaned_data)
    #         return redirect('b:home')
    #     else:
    #         print('form invalid')
    #         return redirect('b:this-year')
#
#
# def shop(request):
#     bookshops = Bookshop.objects.all()
#     return render(request,'b/book_list.html', {
#         'bookshops': bookshops
#     })
#
#
# def contact_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         phone = request.POST.get('phone', '')
#         message =  request.POST.get('message', '')
#         contact_form = Contact(name=name, email=email, phone=phone, message=message)
#         contact_form.save()
#         return render(request, 'b/back.html', {'name': name })
#     else:
#         return render(request, 'b/back.html', {})
#
# def yafcontact(request):
#     if request.method == 'POST':
#         email_a = request.POST.get('email')
#         name_b = request.POST.get('name')
#         subject_c = request.POST.get('subject')
#         message_d = request.POST.get('message')
#
#         d = YafContact(email=email_a, name=name_b, subject=subject_c, message=message_d)
#         d.save()
#         return render(request, 'b/alayo.html', {})
#     else:
#         return render(request, 'b/alayo.html')
#
#
# def studio(request):
#     return render(request, 'b/nice.html')
#
#
#
# def topics(request):
#     topics = Topic.objects.order_by('date_added')
#     context = {'topics': topics}
#     return render(request, 'b/topics.html', context)
#
#
# def topic(request, topic_id):
#     topic = Topic.objects.get(id=topic_id)
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'b/good.html', context)
#
#
#
#
# def tropics(request):
#     tropics = Tropic.objects.order_by('date_added')
#     context = {'tropics': tropics}
#     return render(request, 'b/wonder.html', context)
#
#
# def tropic(request, tropic_id):
#     tropic = Tropic.objects.get(id=tropic_id)
#     dentries = tropic.dentry_set.order_by('-date_added')
#     context = {'tropic': tropic, 'dentries': dentries}
#     return render(request, 'b/no.html', context)
#
#
# def Yaf(request):
#     return render(request, 'b/amen.html')
#
#
#
#
#
#
#
# def tops(request):
#     tops = Now.objects.order_by('date_added')
#     context = {'tops':tops}
#     return render(request, 'b/new.html', context)
#
#
# def top(request, pk):
#     top = Now.objects.get(pk=pk)
#     news = top.new_set.order_by('-date_added')
#     context = {'top':top, 'news':news}
#     return render(request, 'b/news.html', context)
#
#
#
#
#
