
from django.urls import path
from .views import TopBannerGetView, TestimonialGetView, CareersView, TopPacksGetView, CareersBannerView, \
    AboutBannerGetView, WhyChoseUsGetView, FAQGetView, PortFolioGetView, AboutAssertGetView

urlpatterns = [
    path('top-banner', TopBannerGetView.as_view()),
    path('testimonial', TestimonialGetView.as_view()),
    path('career', CareersView.as_view()),
    path('top-packs', TopPacksGetView.as_view()),
    path('career-banner', CareersBannerView.as_view()),
    path('about-banner', AboutBannerGetView.as_view()),
    path('why-chose-us', WhyChoseUsGetView.as_view()),
    path('our-faq', FAQGetView.as_view()),
    path('portfolio', PortFolioGetView.as_view()),
    path('about-asserts', AboutAssertGetView.as_view())
]

