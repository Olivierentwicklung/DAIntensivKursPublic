from django.urls import path

from .views import single_gadget_view, start_page_view

urlpatterns = [
    path("start/", start_page_view),
    path("", start_page_view),
    path("gadgets", single_gadget_view),
]
