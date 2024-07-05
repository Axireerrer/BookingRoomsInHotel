from rest_framework.generics import CreateAPIView
from users.serializers import UserAuthSerializer
from rest_framework.response import Response


class RegisterUserApi(CreateAPIView):
    serializer_class = UserAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
