from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile


@receiver(user_signed_up)
def populate_profile(sociallogin, user, **kwargs):
    user.profile = Profile()

    if sociallogin.account.provider == "facebook":
        user_data = user.socialaccount_set.filter(provider="facebook")[0].extra_data
        email = user_data["email"]
        first_name = user_data["first_name"]
        last_name = user_data["last_name"]
        picture_url = user_data["picture"]["data"]["url"]
    if sociallogin.account.provider == "google":
        user_data = user.socialaccount_set.filter(provider="google")[0].extra_data
        first_name = user_data["given_name"]
        last_name = user_data["family_name"]
        email = user_data["email"]
        picture_url = user_data["picture"]

    user.profile.first_name = first_name
    user.profile.last_name = last_name
    user.profile.email = email
    user.profile.profile_photo = picture_url
    user.profile.save()


@receiver(post_save, sender=Profile)
def updateprofile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        user.email = profile.email
        user.profile_photo = profile.profile_photo
        user.save()
