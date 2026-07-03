from django.contrib.auth import get_user_model

User = get_user_model()

class AuthService:
    @staticmethod
    def create_user(email, first_name, last_name, password, role=User.Role.CUSTOMER):
        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role
        )
        return user
