from rest_framework import serializers
from app.models import TopBanner, Testimonial, Careers, CareerBanner, TopPacks


class TopBannerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopBanner
        fields = "__all__"


class TestimonialGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class CareersGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = "__all__"


class CareerBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerBanner
        fields = "__all__"


class TopPacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopPacks
        fields = "__all__"


# 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