from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Instructor, Student , Track

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)  # 🔹 استخدام set_password() لضمان تشفير كلمة المرور
        user.save()
        return user

class InstructorSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    track_name = serializers.CharField(write_only=True, required=True)  # 🔹 التأكد من أن track_name مطلوب

    class Meta:
        model = Instructor
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        track_name = validated_data.pop("track_name")

        # تعيين دور المستخدم كمدرب
        user_data["role"] = "instructor"
        user = User.objects.create_user(**user_data)

        # البحث عن التراك أو إنشاؤه
        track, created = Track.objects.get_or_create(name=track_name)

        instructor = Instructor.objects.create(user=user, **validated_data)
        track.instructor = instructor
        track.save()

        return instructor


class StudentSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    track_name = serializers.CharField(write_only=True, required=True)  # 🔹 التأكد من أن track_name مطلوب

    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        track_name = validated_data.pop("track_name")

        # تعيين دور المستخدم كطالب
        user_data["role"] = "student"
        user = User.objects.create_user(**user_data)

        # البحث عن التراك
        track = Track.objects.filter(name=track_name).first()
        if not track:
            raise serializers.ValidationError({"track_name": "No track with this name."})

        student = Student.objects.create(user=user, track=track, **validated_data)

        return student
