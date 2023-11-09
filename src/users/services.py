from django.core.mail import send_mail


def send_activation_email(email, activation_key):
    send_mail(
        subject="User activation",
        message=f"Please activate your account: {activation_key}",
        from_email="admin@admin.com",
        recipient_list=[email],
        fail_silently=False,
    )


def send_response_email(email):
    send_mail(
        subject="User activation",
        message="User activated successfully.",
        from_email="admin@admin.com",
        recipient_list=[email],
        fail_silently=False,
    )
