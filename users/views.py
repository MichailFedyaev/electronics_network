from rest_framework_simplejwt.views import TokenObtainPairView
# from django_ratelimit.decorators import ratelimit
# from django.utils.decorators import method_decorator


# @method_decorator(ratelimit(key='ip', rate='5/m', block=True), name='dispatch')
# (надо использовать с редисом но мне было в падлу так расширять MVP)
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)  # Вызываем родительский метод для
        # выполнения стандартной аутентификации
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        role = "admin" if user.is_staff else "user"
        response.data['role'] = role
        return response
