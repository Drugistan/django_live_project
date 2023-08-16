
from django.urls import path
from .views import TopBannerGetView, TestimonialGetView, CareersView, TopPacksGetView

urlpatterns = [
    path('top-banner', TopBannerGetView.as_view()),
    path('testimonial', TestimonialGetView.as_view()),
    path('career', CareersView.as_view()),
    path('top-packs', TopPacksGetView.as_view()),
]
