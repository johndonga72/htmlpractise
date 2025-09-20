class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().select_related("profile")
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        result = []
        for user in users:
            profile_instance = getattr(user, "profile", None)
            user_data = AdminUserSerializer(user).data
            user_data["profile"] = AdminUserProfileSerializer(profile_instance).data if profile_instance else None
            result.append(user_data)
        return Response(result)

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        profile_instance = getattr(user, "profile", None)
        user_data = AdminUserSerializer(user).data
        user_data["profile"] = AdminUserProfileSerializer(profile_instance).data if profile_instance else None
        return Response(user_data)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = AdminUserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path="block")
    def block_user(self, request, pk=None):
        user = self.get_object()
        user.is_blocked = True
        user.save()
        return Response({"message": f"User {user.email} blocked"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="unblock")
    def unblock_user(self, request, pk=None):
        user = self.get_object()
        user.is_blocked = False
        user.save()
        return Response({"message": f"User {user.email} unblocked"}, status=status.HTTP_200_OK)
