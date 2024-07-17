
from rest_framework.request import Request
from rest_framework import filters, status, viewsets
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from .models import Darslar, Kurslar, Izohlar, LikeText, User


from .permissions import DarslarPermission,KurslarPermission

from .serializers import (
    KursSerializer,
    LikeTextSerializer,
    DarsSerializer,
    IzohSerializer,
    KursFilter,
    UserSerializer,
    EmailSerializer,
   
)




class KursViewSet(viewsets.ModelViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Kurslar.objects.all()
    serializer_class = KursSerializer
    permission_classes = [KurslarPermission]



class DarsViewSet(viewsets.ModelViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Darslar.objects.all()
    serializer_class = DarsSerializer
    permission_classes = [DarslarPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "izoh"]

class IzohViewSet(viewsets.ModelViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Izohlar.objects.all()
    serializer_class = IzohSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmailJonatishView(APIView):
    def post(self,request:Request):

        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        email_users=[]

        for user in users:
            email_users.append(user.email)
        email_users.append('anosirjonov320@gmail.com')


        send_mail(
            serializer.validated_data.get('subject'),
            serializer.validated_data.get('massage'),
            settings.EMAIL_HOST_USER,
            email_users,
            fail_silently=False,
        )
        return Response({"massage":"success"})







class LikeBosishQismi(APIView):
    def get(self, request, pk):
        likes = LikeText.objects.filter(like_or_dislike=True, dars_like_id=pk).count()
        dislikes = LikeText.objects.filter(like_or_dislike=False, dars_like_id=pk).count()
        
     
        return Response({
            "likes": likes,
            "dislikes": dislikes,
        
        })

    

class LikeTextCreateView(APIView):
    def post(self, request):
        try:
            likes_or_dislikes = LikeText.objects.filter(author_id=request.data.get("author"))
            for l_or_d in likes_or_dislikes:
                l_or_d.delete()
        except:
            pass

        serializer = LikeTextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(LikeTextSerializer(like_or_dislike).data)



