from .base_view import BaseBannerView
from .models import TopBanner, Testimonial, Careers, CareerBanner, TopPacks, AboutBanner
from .api.serializer import TopBannerGetSerializer, TestimonialGetSerializer, CareersGetSerializer, TopPacksSerializer, \
    AboutBannerGetSerializer, TopBannerImageSerializer
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


class TestimonialGetView(APIView):

    @staticmethod
    def get(request):
        testimonials = Testimonial.active_testimonial.get_active_testimonial()
        if testimonials:
            serializer_ = TestimonialGetSerializer(testimonials, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"error_message": "Something Went Wrong", "status_code": 400},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"error_message": "Testimonial is not available at this time", "status_code": 400},
                            status=HTTP_400_BAD_REQUEST)


class CareersView(APIView):

    @staticmethod
    def get(request):
        careers = Careers.active_career.get_active_career()
        if careers:
            serializer_ = CareersGetSerializer(careers, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"error_message": "Something Went Wrong", "status_code": 400},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"error_message": "Careers is not available at this time", "status_code": 400},
                            status=HTTP_400_BAD_REQUEST)


class CareersBannerView(BaseBannerView):
    model = CareerBanner
    serializer_class = TopBannerGetSerializer
    queryset = CareerBanner.objects.all()


class TopPacksGetView(APIView):

    @staticmethod
    def get(request):
        top_packs = TopPacks.get_active_packs.get_active_packs()
        if top_packs:
            serializer_ = TopPacksSerializer(top_packs, many=True)
            if serializer_:
                return Response(serializer_.data, status=HTTP_200_OK)
            else:
                return Response({"error_message": "Something Went Wrong", "status_code": 400},
                                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"error_message": "TopPacks is not available at this time", "status_code": 400},
                            status=HTTP_400_BAD_REQUEST)
