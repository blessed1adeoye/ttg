from django.contrib import admin
# from .models import Prayer, Carousel, Book, Post, PostImage, Video, Topic, Entry,Now, New, Tropic, Dentry, Contact, YafContact, Bookshop
from .models import Praye, Counsel, Invite, Ivpg, Testimony, WOFBI, Book, Bookshop, PDF, Choir, Security,\
    Decoration, CHILDREN, PF, HOSPITALITY, PROPHET_FOCUS,  BOOKS_of_the_Months, Recommended_Books, WSF, SPIRITUAL,\
    Recommended_Books_Time,TECHNICAL, USHERING, Services, Category, Video, SANCTUARY, ChoirPage1, ChoirPage2,\
    HomeCarousel, ChoirSong, Gal, imgCool, CA, Contact, Pastor_Desk




class Church(admin.AdminSite):
    site_title = 'GLORY'

church_site = Church(name='church')


# church_site.site_header = "LFC TOTAL GARDEN Admin   DASHBOARD"
# church_site.site_title = "WINNERS' TOTAL GARDEN Portal"
# church_site.index_title = "Welcome to WINNERS'   TOTAL   GARDEN "

# class Aadd(admin.ModelAdmin):
#     list_display = [
#         'name'
#     ]
# church_site.register(Author, Aadd)

church_site.register(CA)
church_site.register(imgCool)
church_site.register(Gal)
church_site.register(ChoirPage1)
church_site.register(ChoirPage2)
church_site.register(Contact)
church_site.register(Pastor_Desk)

class ChoirD(admin.ModelAdmin):
    list_display = [
        'title',
        'song'
    ]
church_site.register(ChoirSong, ChoirD)

class SANCTUARYGB(admin.ModelAdmin):
    list_display = [
        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'joined_date',
        'new_birth_date',
        'occupation',
        'foundation_class',
        'job',
        'status',
        'message'
    ]
church_site.register(SANCTUARY, SANCTUARYGB)



class Cat(admin.ModelAdmin):
    list_display = [
        'title',
        'category_image'
    ]
church_site.register(Category, Cat)


class HC(admin.ModelAdmin):
    lit_display =[
        'img'
    ]

church_site.register(HomeCarousel, HC)


class TsM(admin.ModelAdmin):
    list_display = [
        'd',
        'm',
        'y',
        # 'category',
        'img',
        'Theme',
        'Theme_reference',
        'message'
    ]
church_site.register(Services, TsM)
class USHERINGB(admin.ModelAdmin):
    list_display = [
        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'joined_date',
        'new_birth_date',
        'occupation',
        'foundation_class',
        'job',
        'status',
        'message'
    ]
church_site.register(USHERING, USHERINGB)




class TECHNICALITYGB(admin.ModelAdmin):
    list_display = [
        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'joined_date',
        'new_birth_date',
        'occupation',
        'foundation_class',
        'job',
        'status',
        'message'
    ]
church_site.register(TECHNICAL, TECHNICALITYGB)

class RWSFB(admin.ModelAdmin):
    list_display = [
        'location',
        'centre',
        'residence',
        'Host',
        'minister',
        'phone'
    ]
church_site.register(WSF, RWSFB)

class SPB(admin.ModelAdmin):
    list_display = [
        'm_y',
        'start',
        'end',
        'img',
        'year',
        'remark_1',
        'remark_2'
    ]
church_site.register(SPIRITUAL, SPB)


class RAB(admin.ModelAdmin):
    list_display = [
        'month',
        'year'
    ]
church_site.register(Recommended_Books_Time, RAB)


class RB(admin.ModelAdmin):
    list_display = [
        'book_title',
        'book_img',
        'book_body'
    ]
church_site.register(Recommended_Books, RB)



class Badd(admin.ModelAdmin):
    list_display = [
        'name',
        'book',

    ]
church_site.register(BOOKS_of_the_Months, Badd)

class PROPHET_FOCUSGB(admin.ModelAdmin):
    list_display = [
        'reference',
        'img',
        'month',
        'year',
        'theme',
        'body'
    ]
church_site.register(PROPHET_FOCUS, PROPHET_FOCUSGB)

class HOSPITALITYGB(admin.ModelAdmin):
    list_display = [
        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'joined_date',
        'new_birth_date',
        'occupation',
        'foundation_class',
        'job',
        'status',
        'message'
    ]
church_site.register(HOSPITALITY, HOSPITALITYGB)

class PrayerAdmIN(admin.ModelAdmin):
    list_display = [
        'title',
        'img',
        'document',
    ]

church_site.register(PF, PrayerAdmIN)


class CHILDRENGB(admin.ModelAdmin):
    list_display = [
        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'joined_date',
        'new_birth_date',
        'occupation',
        'foundation_class',
        'job',
        'status',
        'message'
    ]
church_site.register(CHILDREN, CHILDRENGB)


class BookshopAdmin(admin.ModelAdmin):
    list_display = [
        'buyer_name',
        'mailing_address',
        'email',
        'book',
        'copies',
        'phone',
        'message'
    ]

church_site.register(Bookshop, BookshopAdmin)

class DecorationGB(admin.ModelAdmin):
    list_display = [
        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'joined_date',
        'new_birth_date',
        'design_experience',
        'foundation_class',
        'job',
        'status',
        'message'
    ]
church_site.register(Decoration, DecorationGB)

class SecurityGB(admin.ModelAdmin):
    list_display = [
        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'joined_date',
        'new_birth_date',
        'occupation',
        'foundation_class',
        'job',
        'status',
        'message'
    ]
church_site.register(Security, SecurityGB)

class PDFMINE(admin.ModelAdmin):
    list_display = [
        'title',
        'date_day',
        'date_month',
        'date_year',
        'language',
        'document'
    ]

church_site.register(PDF, PDFMINE)

class WOFBIAdmin(admin.ModelAdmin):
    list_display = [
        'jbs_title',
        'img',
        'jbs_st_dt',
        'jbs_st_sup',
        'jbs_sp_dt',
        'jbs_sp_sup',
        'jbs_orient',
        'jbs_orient_sup',
        'jbs_orient_remark',
        'jbs_resume',
        'jbs_resume_sup',
        'jbs_resume_remark',
        'jbs_graduate',
        'jbs_graduate_sup',
        'jbs_graduate_remark',
        'bcc_title',
        'bcc_st_dt',
        'bcc_st_sup',
        'bcc_sp_dt',
        'bcc_sp_sup',
        'bcc_orient',
        'bcc_orient_sup',
        'bcc_orient_remark',
        'bcc_resume',
        'bcc_resume_sup',
        'bcc_resume_remark',
        'bcc_graduate',
        'bcc_graduate_sup',
        'bcc_graduate_remark',
        'lcc_title',
        'lcc_st_dt',
        'lcc_st_sup',
        'lcc_sp_dt',
        'lcc_sp_sup',
        'lcc_orient',
        'lcc_orient_sup',
        'lcc_orient_remark',
        'lcc_resume',
        'lcc_resume_sup',
        'lcc_resume_remark',
        'lcc_graduate',
        'lcc_graduate_sup',
        'lcc_graduate_remark',
        'ldc_title',
        'ldc_st_dt',
        'ldc_st_sup',
        'ldc_sp_dt',
        'ldc_sp_sup',
        'ldc_orient',
        'ldc_orient_sup',
        'ldc_orient_remark',
        'ldc_resume',
        'ldc_resume_sup',
        'ldc_resume_remark',
        'ldc_graduate',
        'ldc_graduate_sup',
        'ldc_graduate_remark'
    ]

church_site.register(WOFBI, WOFBIAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'buk'

    ]

church_site.register(Book, BookAdmin)

class ChoirAdmin(admin.ModelAdmin):
    list_display = [

        'full_name',
        'residence',
        'email',
        'phone',
        'city',
        'born_again',
        'church',
        'date_of_new_birth',
        'instrument',
        'foundation_class',
        'part_sing',
        'marital_status',
        'message',
    ]
church_site.register(Choir, ChoirAdmin)

class TestimonyAdmin(admin.ModelAdmin):
    list_display = [
        'msg_id',
        't_img',
        't_month',
        't_day',
        't_year',
        't_name',
        't_title',
        't_body',

    ]

church_site.register(Testimony, TestimonyAdmin)

class PrayerAdmin(admin.ModelAdmin):
    list_display = [
        'msg_id',
        'full_name',
        'residential',
        'email',
        'phone',
        'church',
        'city',
        'call',
        'pray_for',
        'prayer',
        'time'
    ]

church_site.register(Praye, PrayerAdmin)

class CounselAdmin(admin.ModelAdmin):
    list_display = [
        'msg_id',
        'full_name',
        'residential',
        'email',
        'phone',
        'church',
        'city',
        'call',
        'counsel',
        'message',
        'time'
    ]


church_site.register(Counsel, CounselAdmin)

class InviteAdmin(admin.ModelAdmin):
    list_display = [
        'msg_id',
        'y_full_name',
        'y_email',
        'next_sunday_date',
        'y_friend_full_name',
        'y_friend_email',
        'theme',
        'message'
    ]


church_site.register(Invite, InviteAdmin)


class IvpgAdmin(admin.ModelAdmin):
    list_display = [
        'msg_id',
        'sun_no',
        'sun_alp',
        'sun_img',
        'theme'
    ]

church_site.register(Ivpg, IvpgAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'videofile'
    ]

church_site.register(Video, VideoAdmin)

# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('text', 'date_added')
#
#
#
# class EntryAdmin(admin.ModelAdmin):
#     list_display = ('topic', 'text', 'date_added')
#
# class CarouselAdmin(admin.ModelAdmin):
#     list_display = ('title', 'img', 'sub_title')
#
# class TropicAdmin(admin.ModelAdmin):
#     list_display = ('text', 'date_added')
#
#
# class DentryAdmin(admin.ModelAdmin):
#     list_display = ('tropic', 'text', 'date_added', 'testifier')
#
#
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name','email', 'phone', 'message', 'date_created' )
#
#
# class YafContactAdmin(admin.ModelAdmin):
#   list_display = ('name','email', 'subject', 'message', 'date_created' )
#
#
# class NowAdmin(admin.ModelAdmin):
#     list_display = ('gallery',  'topic')
#
#
# class NewAdmin(admin.ModelAdmin):
#     list_display = ('top', 'text','date_added' )
#
#
#
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ('name', 'videofile' )
#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'pdf')
#
#
# class BookshopAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'pdf')
#
#
# class PostImageAdmin(admin.StackedInline):
#     model = PostImage
#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]
#
#     class Meta:
#         model = Post
#
#
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass
#
#
#
#
# admin.site.register(YafContact, YafContactAdmin)
# admin.site.register(New, NewAdmin)
# admin.site.register(Dentry, DentryAdmin)
# admin.site.register(Tropic, TropicAdmin)
# admin.site.register(Topic, TopicAdmin)
# admin.site.register(Entry, EntryAdmin)
# admin.site.register(Contact, ContactAdmin)
# admin.site.register(Now,NowAdmin )
# admin.site.register(Video, VideoAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(Bookshop, BookshopAdmin)
# admin.site.register(Carousel, CarouselAdmin)