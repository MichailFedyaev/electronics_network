from loguru import logger
from django.http import JsonResponse
from rest_framework import status


class LoguruLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Пропускаем логирование для админки
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        # Логирование входящего запроса
        logger.info(f"Request: {request.method} {request.path}")
        logger.debug(f"User: {request.user}")
        logger.debug(f"IP Address: {request.META.get('REMOTE_ADDR')}")

        try:
            # Обработка запроса
            response = self.get_response(request)

            # Логирование ответа
            logger.info(f"Response: {response.status_code}")
            logger.debug(f"Content-Type: {response.get('Content-Type')}")

            return response
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return JsonResponse(
                {"error": "Internal server error"},
                status=500
            )


class ActiveUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Пути, которые не требуют проверки активности/стаффа в этом middleware
        self.excluded_paths = [
            '/api/users/token/',
            '/api/users/token/refresh/',
            '/api/users/token/verify/',
            '/admin/',
            '/swagger/',
            '/redoc/',
        ]

    def __call__(self, request):
        # Пропускаем не-API запросы и исключенные пути
        if not request.path.startswith('/api/') or any(request.path.startswith(path) for path in self.excluded_paths):
            return self.get_response(request)

        # Стандартная аутентификация уже должна была отработать к этому моменту

        # Проверяем аутентификацию
        if not request.user.is_authenticated:
            return JsonResponse(
                {"error": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Проверяем активность пользователя
        if not request.user.is_active:
            return JsonResponse(
                {"error": "User account is inactive"},
                status=status.HTTP_403_FORBIDDEN
            )

        # Проверяем, является ли пользователь сотрудником (если нужно)
        if not request.user.is_staff:
            return JsonResponse(
                {"error": "Access denied. Staff privileges required"},
                status=status.HTTP_403_FORBIDDEN
            )

        return self.get_response(request)
