from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    role = serializers.ChoiceField(choices=("passager", "operator"), required=False, default="passager")

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.role = validated_data.get("role")
        instance.set_password(validated_data.get("password"))
        instance.save()

        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else:
            return data
