import django_filters
from .models import Kurslar, Darslar, LikeText, Izohlar, User
from rest_framework import serializers

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurslar
        fields = '__all__'

class KursFilter(django_filters.FilterSet):
    class Meta:
        model = Kurslar
        fields = ['kursi',  'muallifi'] 
class DarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Darslar
        fields = '__all__'

class DarsFilter(django_filters.FilterSet):
    class Meta:
        model = Darslar
        fields = ['dars',  'muallifi']  # Correct fields here
        
class LikeTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeText
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izohlar
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=150)
    message = serializers.CharField()
