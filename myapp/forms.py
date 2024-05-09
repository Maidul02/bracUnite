from django import forms
from .models import Profile, GENDER_CHOICES, BLOOD_GROUP_CHOICES

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['is_active', 'user']

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=GENDER_CHOICES),
            'blood_group': forms.Select(choices=BLOOD_GROUP_CHOICES),
            'profile_pic': forms.FileInput(attrs={'accept': 'image/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Rename the first_name field's label
        self.fields['facinitial'].label = 'Faculty Initial (Only for faculties)'
        self.fields['gsuiteEmail'].label = 'Regular Email'