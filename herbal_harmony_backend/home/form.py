from django import forms

# Django ka 'forms.Form' ek simple form create karne ke liye use hota hai
class HealthForm(forms.Form):
    AGE_CHOICES = [
        ('child', 'Child(0-12)'),
        ('teen', 'Teenagers(13-19)'),
        ('adult', 'Adult(20-40)'),
        ('middle_aged', 'Middle Aged(41-60)'),
        ('elderly', 'Elderly(60+)'),
    ]

    # yahan 2 fields banayi gayi hain
    age_group = forms.ChoiceField(label="Select Age Group",choices=AGE_CHOICES)
    symptom = forms.CharField(label="Describe Your Problem", max_length=100)

# # Ye code ek simple Django form define karta hai jisme do fields hain: 'age_group' aur 'symptom'.
