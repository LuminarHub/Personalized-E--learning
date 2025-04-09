from django.contrib import admin
from .models import CustUser, Feedback, UploadedFile, CourseDB, CourseRegistration, Placement,JobApplication,Payment
from Faculty.models import Video, Comment,WatchHistory
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import CustUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustUser
        fields = ('username', 'email', 'phone', 'gender', 'age', 'Course', 'is_student', 'is_faculty', 'is_hr')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class CustUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustUser
        fields = ('username', 'email', 'phone', 'gender', 'age', 'Course', 'is_student', 'is_faculty', 'is_hr')

# Custom UserAdmin to register the custom user model
class CustUserAdmin(UserAdmin):
    add_form = UserCreationForm  # Use the default UserCreationForm
    form = UserChangeForm  # Use the default UserChangeForm

    model = CustUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_student', 'is_faculty', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']

    # The password fields are handled by UserCreationForm and UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('is_student', 'is_faculty')}),
    )

    # Define the fieldsets for add_view
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Custom Fields', {'fields': ('is_student', 'is_faculty')}),
    )

    # These fields are used when creating or changing a user
    filter_horizontal = ('groups', 'user_permissions')

# Register the custom user model in the admin
admin.site.register(CustUser, CustUserAdmin)
admin.site.register(Feedback)
admin.site.register(UploadedFile)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(CourseDB)
admin.site.register(CourseRegistration)
admin.site.register(Placement)
admin.site.register(JobApplication)
admin.site.register(Payment)

