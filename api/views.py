from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from api.serializers import CompanySerializer
from api.models import Company
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
 
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all() 
    serializer_class = CompanySerializer

    # can be used to filter the queryset (e.g., /api/companies/?IQ_SECTOR=Financials) 
    def get_queryset(self):
        queryset = Company.objects.all() 
        query_params = self.request.query_params 

        valid_fields = [f.name for f in Company._meta.get_fields()] 
        for field in valid_fields:
            if field in query_params:
                queryset = queryset.filter(**{field: query_params[field]})

        return queryset

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            # Logic for successful login
            return Response({"message": "Login successful"})
        else:
            # Logic for failed login
            return Response({"message": "Login failed"}, status=400)