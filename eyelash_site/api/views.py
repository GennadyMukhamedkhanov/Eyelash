from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions.permissions import OnlyTheCreator
from api.serializers import (ServiceSerializers, ServiceID, ServiceSheduleSerializers,
                             SheduleId, BookingSerializer, UsersId, UsersSerializer, UserCreateSerializer,
                             UserGetSerializer, TokenGetSerializers, ServiceCreateleSerializers)
from my_site.models import Service, Booking, User
from rest_framework.authtoken.models import Token


class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            phone=serializer.validated_data['phone']
        )
        Token.objects.create(user=obj)
        return Response(
            UserGetSerializer(obj).data
        )


class TokenGetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenGetSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'Token': (serializer.validated_data['user'].auth_token).key
        })


class ServiceGetCreateView(APIView):
    def get(self, request):
        service = Service.objects.all()
        serializers = ServiceSerializers(service, many=True).data
        return Response({
            'SERVICE': serializers
        })

    def post(self, request):
        self.permission_classes = [IsAdminUser]
        self.check_permissions(request)
        serializer = ServiceCreateleSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = Service.objects.create(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            price=serializer.validated_data['price'],
            image=serializer.validated_data['image']
                    )
        obj_ser = ServiceSerializers(instance).data
        return Response(obj_ser)



class ServiceSheduleGetView(APIView):
    def get(self, request, **kwargs):
        serializer = ServiceID(data=kwargs)
        serializer.is_valid(raise_exception=True)
        service_obj = serializer.validated_data['pk']
        obj_ser = ServiceSheduleSerializers(service_obj)
        return Response({
            'data': obj_ser.data
        })


class BookingView(APIView):
    def post(self, request, **kwargs):
        serializer = SheduleId(data=kwargs)
        serializer.is_valid(raise_exception=True)
        obj_shedule = serializer.validated_data['pk']
        obj_shedule.status = True
        obj_shedule.save()

        book = Booking.objects.create(
            shedule=obj_shedule,
            user=request.user
        )
        serializer_booking = BookingSerializer(book).data
        return Response({
            'Запись': serializer_booking
        })


class PersonalListView(APIView):

    def get(self, request, **kwargs):
        self.permission_classes = [OnlyTheCreator, ]
        serilizer = UsersId(data=kwargs)
        serilizer.is_valid(raise_exception=True)
        user = serilizer.validated_data['pk']
        self.check_object_permissions(request=request, obj=user)
        book = UsersSerializer(user).data
        return Response({
            'Запись': book
        })


class SearchServiceView(APIView):
    def get(self, request):
        service = Service.objects.filter(name__contains=request.data['name'])
        serializers = ServiceSerializers(service, many=True).data
        return Response({
            'SERVICE': serializers
        })


class CreatingServicesView(APIView):
    pass
