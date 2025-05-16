from djoser import serializers

class UserCreateSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
        fields = [
            'id', 'first_name', 'last_name', 'email', 'username', 'password',
        ]


