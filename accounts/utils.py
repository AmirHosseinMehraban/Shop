from django.core.mail import send_mail


def mail(code, email, name):
    send_mail(
        "Verification Code",
        f"hi {name} \n the verify code is  {code} \n this code will be deleted after 120 seconds ",
        "ahm.mehrabanamirh@gmail.com",
        [email],
        fail_silently=False,
    )
