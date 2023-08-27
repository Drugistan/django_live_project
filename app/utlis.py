from django.conf import settings
from django.http import HttpRequest


def get_full_image_path(self, obj):
    if obj.image:
        if isinstance(self.context.get('request'), HttpRequest):
            print("self")
            request = self.context.get('request')
            full_url = request.build_absolute_uri(obj.image.url)
            return full_url
        else:
            # If request is not available (e.g., in the admin panel), use a different approach
            print("jnjn")
            return settings.BASE_URL + obj.image.url  # Replace BASE_URL with your domain
    return None