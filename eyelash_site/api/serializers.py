from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from my_site.models import Service, Shedule, Time, Booking, User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'phone',
        )


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'phone',
        )


class TokenGetSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        obj = User.objects.filter(username=attrs['username'])
        if (not obj.first()) or (not obj.first().check_password(attrs['password'])):
            raise ValidationError('User not found')
        attrs['user'] = obj.first()
        return attrs


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'name',
            'image'
        )


class TimeSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('start_date',)


class SheduleSerializer(serializers.ModelSerializer):
    # date = serializers.DateTimeField(source='date.start_date')
    # date = TimeSeralizer()

    date = serializers.SerializerMethodField()

    def get_date(self, obj):
        data_time = obj.date
        obj = TimeSeralizer(data_time).data
        return obj

    class Meta:
        model = Shedule
        fields = ('date',)


class ServiceSheduleSerializers(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        shedule = obj.shedule.filter(service=obj, status=False)
        return SheduleSerializer(shedule, many=True).data

    class Meta:
        model = Service
        fields = (
            'name',
            'image',
            'description',
            'price',
            'time',
        )


class BookingSerializer(serializers.ModelSerializer):
    shedule = serializers.CharField(source='shedule.service.name')
    user = serializers.CharField(source='user.username')
    time = serializers.DateTimeField(source='shedule.date.start_date')

    class Meta:
        model = Booking
        fields = (
            'shedule',
            'user',
            'time'
        )


class BookingUserSerializer(serializers.ModelSerializer):
    shedule = serializers.CharField(source='shedule.service.name')
    time = serializers.DateTimeField(source='shedule.date.start_date')

    class Meta:
        model = Booking
        fields = (
            'shedule',
            'time'
        )


class UsersSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        book = obj.bookings.all()
        return BookingUserSerializer(book, many=True).data

    class Meta:
        model = User
        fields = (
            'description',
            'username'
        )


class ServiceCreateleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'name',
            'image',
            'description',
            'price',
        )


class ServiceID(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())


class TimeId(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(queryset=Time.objects.all())


class SheduleId(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(queryset=Shedule.objects.all())


class UsersId(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
