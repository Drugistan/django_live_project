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

    def validate(self, attrs):
        image = attrs.get["add_image"]
        print(image)
