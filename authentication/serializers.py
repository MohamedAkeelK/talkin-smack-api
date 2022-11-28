from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerialization(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)
    avatar = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password',
                  'first_name', 'last_name', 'avatar', 'created_at', 'updated_at']

    def validate(self, attrs):
        username_exists = User.objects.filter(
            username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(
                detail="User with username exists")

        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")

        phone_number_exists = User.objects.filter(
            phone_number=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError(
                detail="User with phone number exists")

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            avatar=validated_data['avatar']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
