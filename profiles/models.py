from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """

    class UserProfile(models.Model):
        A model to store additional information for a user profile.

        Attributes:
        user : OneToOneField
            A one-to-one relationship to the User model, ensures each user has one UserProfile.
        default_phone_number : CharField
            Stores the default phone number of the user, can be null or blank.
        default_country : CountryField
            Stores the default country of the user, can be null or blank.
        default_postcode : CharField
            Stores the default postcode of the user, can be null or blank.
        default_city : CharField
            Stores the default city of the user, can be null or blank.
        default_street_address1 : CharField
            Stores the first line of the default street address of the user, can be null or blank.
        default_street_address2 : CharField
            Stores the second line of the default street address of the user, can be null or blank.
        default_county : CharField
            Stores the default county of the user, can be null or blank.
        default_profile_image : ImageField
            Stores the default profile image of the user, can be null or blank.
        default_bio : TextField
            Stores the default bio of the user, can be null or blank, up to 500 characters.
        default_location : CharField
            Stores the default location of the user, can be null or blank.
        default_birth_date : DateField
            Stores the default birth date of the user, can be null or blank.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country *", null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_profile_image = models.ImageField(
        upload_to="profile_images", null=True, blank=True
    )
    default_bio = models.TextField(max_length=500, null=True, blank=True)
    default_location = models.CharField(max_length=30, null=True, blank=True)
    default_birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile when a new user is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
