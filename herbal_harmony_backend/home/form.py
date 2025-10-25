from django import forms

# Django ka 'forms.Form' ek simple form create karne ke liye use hota hai
class HealthForm(forms.Form):
    AGE_CHOICES = [
        ('child', 'child'),
        ('adult', 'adult'),
        ('elderly', 'elderly'),
    ]

    # yahan 2 fields banayi gayi hain
    age_group = forms.ChoiceField(label="Select Age Group",choices=AGE_CHOICES)
    symptom = forms.CharField(label="Describe Your Problem", max_length=100)

# # Ye code ek simple Django form define karta hai jisme do fields hain: 'age_group' aur 'symptom'.


#     # 'ChoiceField' dropdown menu ke liye aur 'CharField' text input ke liye hai
#     def clean_symptom(self):
#         data = self.cleaned_data['symptom']
#         # yahan hum ensure kar rahe hain ki symptom field empty na ho
#         if not data.strip():
#             raise forms.ValidationError("This field cannot be empty.")
#         return data
# # Note: Ye code sirf form definition ke liye hai. Form ko use karne ke liye views aur templates bhi banane honge.
# # Agar aapko database interaction bhi chahiye to wo alag se implement karna hoga, jaise ki 'herbal_harmony_backend/home/ai.py' mein dikhaya gaya hai.
#         "link": "/templates/kapalbhati.html/",