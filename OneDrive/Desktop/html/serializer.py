class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "full_name"]  # include more fields if needed

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    # Nested serializers
    user = UserSerializer(read_only=True)  # ✅ show full user object instead of just ID
    educations = EducationSerializer(many=True, required=False)
    experiences = WorkExperienceSerializer(many=True, required=False)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",   # ✅ now will return full user data
            "dob",
            "gender",
            "contact",
            "address",
            "profile_photo",
            "resume",
            "skills",
            "languages",
            "educations",
            "experiences",
        ]
        read_only_fields = ["user"]

    def create(self, validated_data):
        educations_data = validated_data.pop("educations", [])
        experiences_data = validated_data.pop("experiences", [])

        profile = UserProfile.objects.create(**validated_data)

        for edu in educations_data:
            Education.objects.create(user_profile=profile, **edu)

        for exp in experiences_data:
            WorkExperience.objects.create(user_profile=profile, **exp)

        return profile

    def update(self, instance, validated_data):
        # Update basic profile info
        instance.dob = validated_data.get("dob", instance.dob)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.contact = validated_data.get("contact", instance.contact)
        instance.address = validated_data.get("address", instance.address)
        instance.profile_photo = validated_data.get("profile_photo", instance.profile_photo)
        instance.resume = validated_data.get("resume", instance.resume)
        instance.skills = validated_data.get("skills", instance.skills)
        instance.languages = validated_data.get("languages", instance.languages)
        instance.save()

        # Handle nested education
        educations_data = validated_data.get("educations", [])
        for edu in educations_data:
            Education.objects.update_or_create(
                user_profile=instance,
                degree=edu.get("degree"),
                defaults=edu
            )

        # Handle nested work experience
        experiences_data = validated_data.get("experiences", [])
        for exp in experiences_data:
            WorkExperience.objects.update_or_create(
                user_profile=instance,
                company_name=exp.get("company_name"),
                designation=exp.get("designation"),
                defaults=exp
            )

        return instance