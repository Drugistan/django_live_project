from .base_view import BaseBannerView
from .models import TopBanner, Testimonial, Careers, CareerBanner, TopPacks, AboutBanner, FAQ, PortFolio, AboutAsserts
from .api.serializer import TopBannerGetSerializer, TestimonialGetSerializer, CareersGetSerializer, TopPacksSerializer, \
    AboutBannerGetSerializer, CareerBannerSerializer, FAQSerializer, PortfolioSerializer, AboutAssertsSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


# Create your views here.


class TopBannerGetView(BaseBannerView):
    model = TopBanner
    serializer_class = TopBannerGetSerializer
    queryset = TopBanner.objects.all()


class AboutBannerGetView(BaseBannerView):
    model = AboutBanner
    serializer_class = AboutBannerGetSerializer
    queryset = AboutBanner.objects.all()


class CareersBannerView(BaseBannerView):
    model = CareerBanner
    serializer_class = CareerBannerSerializer
    queryset = CareerBanner.objects.all()


class TestimonialGetView(APIView):

    @staticmethod
    def get(request):
        testimonials = Testimonial.active_testimonial.get_active_testimonial()
        if testimonials:
            serializer_ = TestimonialGetSerializer(testimonials, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"message": "Something Went Wrong", "status_code": 200},
                                status=HTTP_200_OK)
        else:
            return Response({"message": "Testimonial is not available at this time", "status_code": 400},
                            status=HTTP_200_OK)


class CareersView(APIView):

    @staticmethod
    def get(request):
        careers = Careers.active_career.get_active_career()
        if careers:
            serializer_ = CareersGetSerializer(careers, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"message": "Something Went Wrong", "status_code": 200},
                                status=HTTP_200_OK)
        else:
            return Response({"message": "Careers is not available at this time", "status_code": 200},
                            status=HTTP_200_OK)


class TopPacksGetView(APIView):

    @staticmethod
    def get(request):
        top_packs = TopPacks.get_active_packs.get_active_packs()
        if top_packs:
            serializer_ = TopPacksSerializer(top_packs, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"message": "Something Went Wrong", "status_code": 200},
                                status=HTTP_200_OK)
        else:
            return Response({"message": "TopPacks is not available at this time", "status_code": 200},
                            status=HTTP_200_OK)


class FAQGetView(APIView):

    @staticmethod
    def get(request):
        faq_ = FAQ.active_faq.get_active_faq()
        if faq_:
            serializer_ = FAQSerializer(faq_, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"message": "Something Went Wrong", "status_code": 200},
                                status=HTTP_200_OK)
        else:
            return Response({"message": "FAQ is not available at this time", "status_code": 200},
                            status=HTTP_200_OK)


class PortFolioGetView(APIView):

    @staticmethod
    def get(request):
        portfolio = PortFolio.active_portfolio.get_active_portfolio()
        if portfolio:
            serializer_ = PortfolioSerializer(portfolio, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"message": "Something Went Wrong", "status_code": 200},
                                status=HTTP_200_OK)
        else:
            return Response({"message": "portfolio is not available at this time", "status_code": 200},
                            status=HTTP_200_OK)


class AboutAssertGetView(APIView):

    @staticmethod
    def get(request):
        about_assert = AboutAsserts.objects.all()
        if about_assert:
            serializer_ = AboutAssertsSerializer(about_assert, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"message": "Something Went Wrong", "status_code": 200},
                                status=HTTP_200_OK)
        else:
            return Response({"message": "About Asserts  is not available at this time", "status_code": 200},
                            status=HTTP_200_OK)

