from django.contrib.auth.forms import UserCreationForm


class CustomeUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
