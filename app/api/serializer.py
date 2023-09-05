from django.conf import settings
from rest_framework import serializers
from app.models import TopBanner, Testimonial, Careers, CareerBanner, TopPacks, AboutBanner, FAQ, PortFolio, \
    AboutAsserts
from django.http import HttpRequest

from app.utlis import get_full_image_path


class TopBannerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopBanner
        fields = ['title', 'description', 'images']


class TestimonialGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class CareersGetSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Careers
        fields = "__all__"

    def get_image(self, obj):
        return get_full_image_path(self, obj)


class CareerBannerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CareerBanner
        fields = "__all__"

    def get_image(self, obj):
        return get_full_image_path(self, obj)


class TopPacksSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = TopPacks
        fields = "__all__"

    def get_add_image(self, obj):
        return get_full_image_path(self, obj)



class AboutBannerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutBanner
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PortFolio
        fields = "__all__"

    def get_image(self, obj):
        return get_full_image_path(self, obj)


class AboutAssertsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutAsserts
        fields = "__all__"

    def get_image(self, obj):
        return get_full_image_path(self, obj)

# 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
