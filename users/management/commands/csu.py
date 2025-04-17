from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """Кастомная команда создания суперпользователя"""
    help = 'Создает суперпользователя с заданными параметрами'
    # python manage.py csu --username=myadmin --email=myadmin@example.com --password=mypassword

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='misha52',
            help='Имя пользователя для суперпользователя'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@example.com',
            help='Email для суперпользователя'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='123',
            help='Пароль для суперпользователя'
        )

    def handle(self, *args, **options):
        User = get_user_model()

        username = options['username']
        email = options['email']
        password = options['password']

        # Проверяем существование пользователя
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Пользователь {username} уже существует')
            )
            if input('Хотите обновить его? (y/n): ').lower() != 'y':
                return

        # Создаем или обновляем суперпользователя
        user, created = User.objects.update_or_create(
            username=username,
            defaults={
                'email': email,
                'is_staff': True,
                'is_superuser': True,
                'is_active': True
            }
        )

        # Устанавливаем пароль
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Суперпользователь {username} успешно создан')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Суперпользователь {username} успешно обновлен')
            )