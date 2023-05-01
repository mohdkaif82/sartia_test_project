from rest_framework import serializers
from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['name', 'phone_number',
                  'profile','email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user= MyUser.objects.create_user(email=self.validated_data['email'],
                 password=self.validated_data['password'],
                 )
        user.phone_number=self.validated_data['phone_number']
        user.profile=self.validated_data['profile']
        user.name=self.validated_data['name']
        user.save()
        return user
    
class UpdateUserProfile(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255,required=False)
    phone_number=serializers.CharField(max_length=255,required=False)
    email=serializers.CharField(max_length=255,required=False)
    profile=serializers.FileField(required=False)
    class Meta:
        model = MyUser
        fields = ['name', 'phone_number',
                  'profile','email', ]


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value