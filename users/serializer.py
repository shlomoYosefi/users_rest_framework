from rest_framework.serializers import ModelSerializer
from .models import User

class UserSeriazer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone','address_country','address_city','address_street','address_house_number','user_name','password')
        extra_kwargs = {'password': {'write_only': True}}