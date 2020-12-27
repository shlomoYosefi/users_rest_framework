from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSeriazer
from .models import User
from rest_framework import filters
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets



class UserViewSet(ModelViewSet):
    serializer_class = UserSeriazer
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('address_country','address_city','address_street')
    authentication_classes =  (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class loginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self,request):
        print("shlomo osnat")
        return ObtainAuthToken().post(request)


# class CustomSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         if request.query_params.get('user_name'):
#             return ['user_name']
#         return super(CustomSearchFilter, self).get_search_fields(view, request)