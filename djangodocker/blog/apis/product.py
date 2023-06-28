from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from djangodocker.api.pagination import LimitOffsetPagination
from djangodocker.blog.models import product
from djangodocker.blog.services.products import create_product
from djangodocker.blog.selectors.products import get_products

from drf_spectacular.utils import extend_schema

class productAPI(APIView):
    class pagination(LimitOffsetPagination):
        default_limit = 15

    class inputSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=255)

    class outputSerializer(serializers.ModelSerializer):
        class Meta:
            model = product
            fields = ("id", "name", "created_at", "updated_at")


    @extend_schema(request=inputSerializer, responses=outputSerializer)
    def post(self, request):
        serializer = self.inputSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_product(name = serializer.validated_data.get("name"))
        except Exception as ex:
            return Response(f"Database Error {ex}", status=status.HTTP_400_BAD_REQUEST)
        return Response(self.outputSerializer(query, context = {"request":request}).data)

    @extend_schema(responses=outputSerializer)
    def get(self, request):
        query = get_products()
        return Response(self.outputSerializer(query, context = {"request":request}, many=True).data)

