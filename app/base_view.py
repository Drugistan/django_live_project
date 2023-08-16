from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class BaseBannerView(APIView):
    model = None
    serializer_class = None

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({"error_message": "Something Went Wrong", "status_code": 400},
                            status=HTTP_400_BAD_REQUEST)
