from django.urls import path
from . import views



app_name = 'b'


urlpatterns = [
    path('', views.Home, name='home'),
    path('UPLOADS/', views.upload, name='videos'),
    path("contact/", views.contact, name="contact"),
    path('SANCTUARY-KEEPERS/', views.Santuary, name='keepers'),
    path('TRANSPORTATION-UNIT/', views.Transport, name='transport'),
    path('welcome', views.Pastor_desk, name='pastor'),
    path('COMMUNION-SERVICE', views.Communion, name='communion'),
    path('JOIN-ME-IN-PRAYER/', views.PrayerView, name='pray'),
    path('Biblical-COUNSELling', views.Counselling, name='counsel'),
    path('ABOUT-US/', views.About, name='about'),
    path('I-AM-MORE-THAN-A-CONQUEROR/', views.Prophetic_Decleration, name='this-year'),
    path('Invite-a-friend/', views.Invitee, name='invite'),
    path('BREAKTHROUGH-TIME/', views.Testy, name='testimony'),
    path('WORD-OF-FAITH-BIBLE-INSTITUTE/', views.Wofbi, name='wofbi'),
    path('DOMINION-BOOKSHOP/', views.Books, name='book'),
    path('THE-MANDATE-PILLARS/', views.Pillars, name='faith'),
    path('THE-CHURCH-GROWTH-MANDATE/', views.Growth, name='church-growth'),
    path('GIVING-OUT', views.giving, name="giving"),
    path('MINISTRY-RESOURCES/', views.Resources, name='pdf'),
    path('MUSIC-MINISTRY/', views.choir, name='choir'),
    path('CHOIR-SONG', views.choirsong, name='songs'),
    path('VIGILANCE-MINISTRY/', views.security, name='security'),
    path('BEAUTIFYING-MINISTRY/', views.decorate, name='decorate'),
    path('CHILDREN-MINISTRY/', views.children, name='children'),
    path('PRAYER-MINISTRY/', views.prayerforce, name='prayerforce'),
    path('HOSPITALITY-MINISTRY/', views.hospitality, name='hospitality'),
    path('PROPHETIC-FOCUS/', views.Monthly, name='yt'),
    path('BOOKS-OF-THE-MONTH/', views.Book_of_Month, name='Bkm'),
    path('WINNERS-SATELLITE-FELLOWSHIP/', views.cell, name='wsf'),
    path('WEEK-OF-SPIRITUAL-EMPHASIS/', views.SpWE, name='week'),
    path('BELIEVERS-FOUNDATION-CLASS/', views.bfc, name='bfc'),
    path('MEDIA-CENTER/', views.Studio, name='studio'),
    path('USHERING-&-PROTOCOL/', views.ushering, name='usher'),
    path('PREACHINGS/', views.service, name='sunday'),
    path('WORD-OF-FAITH/', views.all_message, name='messages'), # messages or sms
    path('MESSAGE<int:id>', views.MDetail, name='detail'),
    path('all-category', views.all_category, name='all-category'),
    path('category<int:id>', views.category, name='category'),
    path('HARVESTER-&-FOLLOW-UP', views.Harvester, name='harvest'),
    path('GILEAD-TEAM', views.Gilead, name='gilead'),
    path('JOEL-COMPANY-INC', views.drama, name='joel'),
    path('DOMI/', views.domi, name='domi'),
    path('GALLERY', views.gal, name='gal')
    # path('ADE/', views.cool, name='ade'),
    # path('MINISTRY-PRAYER/', Prayer.as_view(), name='pd'),
    # path('MINISTRY-PRAYER/', views.Prayer, name='pd')
    # path('ABOUT US', views.About, name='about'),
    # path('ay', views.upload, name='upload' ),
    # path('archives', views.blog_view, name='archives'),
    # path('<int:id>/', views.detail_view, name='og'),
    # path('a', views.services, name='sss'),
    # path('cells', views.wsf, name='wsf_list'),
    # path('books', views.shop, name='book_list'),
    # path('media', views.studio, name='nice'),
    # path('halelluyah', views.tropics, name='wonder'),
    # path('congrat', views.topics, name='topics'),
    # path('mercy(?P<topic_id>\d+)$', views.topic, name='good'),
    # path('miracles(?P<tropic_id>\d+)$', views.tropic, name='no'),
    # path('yaf', views.Yaf, name='amen'),
    # path('wow', views.contact_form, name='back'),
    # path('woow', views.yafcontact, name='alayo'),
    # path('new', views.tops, name='new'),
    # path('(?P<pk>\d+)$', views.top, name='news')
]
