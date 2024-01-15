
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render



urlpatterns = [
    path('admin/', admin.site.urls),

    # EMAIL DESIGN TEMPLATE VIEW
    path("templates/", include("templates.url")),

    #  USER PROFILES AND AUTH VIEWS
    path("api/auth/", include("routes.auth")),
    path("api/user/profile/", include("routes.profile")),

    # GENERAL LISTINGS VIEW
    path("api/listings/", include("routes.houses")),
    path("api/listings/properties/", include("routes.properties")),

    # DASHBOARD URLS
    path("api/dashboard/", include("routes.dashboard")),
    
    path("__debug__/", include("debug_toolbar.urls")),
]
