"""contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from contacts_app.views import main_page_view, new_person_view, modify_person_view, delete_person_view, \
    show_person_view, add_address_view, add_phone_view, add_email_view, delete_phone, delete_email, delete_address, \
    all_groups_view, modify_group_view, delete_group_view, new_group_view, group_details_view, add_person_to_group, \
    delete_from_grp, person_search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('new/', new_person_view),
    re_path(r'^modify/(?P<id>(\d)+)$', modify_person_view),
    re_path(r'^delete/(?P<id>(\d)+)$', delete_person_view),
    re_path(r'^show/(?P<id>(\d)+)/$', show_person_view),
    re_path(r'^(?P<id>(\d)+)/addAddress/$', add_address_view),
    re_path(r'^(?P<id>(\d)+)/addPhone/$', add_phone_view),
    re_path(r'^(?P<id>(\d)+)/addEmail/$', add_email_view),
    re_path(r'^(?P<id>(\d)+)/(?P<id2>(\d)+)/deletePhone/$', delete_phone),
    re_path(r'^(?P<id>(\d)+)/(?P<id2>(\d)+)/deleteMail/$', delete_email),
    re_path(r'^(?P<id2>(\d)+)/deleteAddress/$', delete_address),
    path('groups/', all_groups_view),
    re_path(r'^modify/group/(?P<id>(\d)+)/$', modify_group_view),
    re_path(r'^group/delete/(?P<id>(\d)+)/$', delete_group_view),
    path('newgroup/', new_group_view),
    re_path(r'^group/(?P<id>(\d)+)/$', group_details_view),
    re_path(r'^(?P<id>(\d)+)/addToGroup/$', add_person_to_group),
    re_path(r'^(?P<id>(\d)+)/(?P<id2>(\d)+)/delFromGrp/$', delete_from_grp),
    path('group-search/', person_search_view),

]
