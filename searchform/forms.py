from django.core.exceptions import ValidationError
from django import forms


# class SearchFormVila(forms.Form):
#     ghabel_moaveze = (
#         ('','All'),
#         (1 ,'True'),
#         (0 ,'False'),
#         )
#     STATUS_BUY = (
#         ('baraye_kharid', 'baraye_kharid'),
#         ('braye_rahn_ejare', 'braye_rahn_ejare'),
#     )
#     SANAD_CHOICES = (
#         ('sheshdong', 'شش دانگ'),
#         ('mosha', 'مشاع'),
#         ('aslahat', 'اصلاحات ارضی'),
#     )
#     status_buy = forms.ChoiceField(choices=STATUS_BUY)
#     sanad = forms.ChoiceField(choices=SANAD_CHOICES,required=False)
#     ghabel_moaveze = forms.ChoiceField(choices=ghabel_moaveze,initial=True,required=False)
#     locations = forms.CharField(widget=forms.Textarea(attrs={'type':'text','class':'form-control'}),required=False)
#     tedad_otagh = forms.CharField(max_length=1,required=False)
#     min_gheymat = forms.CharField(max_length=20,required=False)
#     max_gheymat = forms.CharField(max_length=20,required=False)



    # def clean_tedad_otagh(self):
    #     tedad_otagh = self.cleaned_data['tedad_otagh']
    #     if not tedad_otagh.isnumeric():
    #         raise ValidationError("tedad_otagh be must number")
    #     else:
    #         return tedad_otagh


class SearchFormAparteman(forms.Form):
    ghabel_moaveze = (
        ('','All'),
        (1 ,'True'),
        (0 ,'False'),
        )
    STATUS_BUY = (
        ('baraye_kharid', 'baraye_kharid'),
        ('braye_rahn_ejare', 'braye_rahn_ejare'),
    )
    SANAD_CHOICES = (
        ('sheshdong', 'شش دانگ'),
        ('mosha', 'مشاع'),
        ('aslahat', 'اصلاحات ارضی'),
    )
    status_buy = forms.ChoiceField(choices=STATUS_BUY)
    sanad = forms.ChoiceField(choices=SANAD_CHOICES,required=False)
    ghabel_moaveze = forms.ChoiceField(choices=ghabel_moaveze,initial=True,required=False)
    locations = forms.CharField(widget=forms.Textarea(attrs={'type':'text','class':'form-control'}),required=False)
    tedad_otagh = forms.CharField(max_length=1,required=False)
    tabage = forms.CharField(max_length=3,required=False)
    sal_sakht = forms.CharField(max_length=3,required=False)
    min_gheymat = forms.CharField(max_length=20,required=False)
    max_gheymat = forms.CharField(max_length=20,required=False)



class SearchFormZamin(forms.Form):
    locations = forms.CharField(max_length=100,required=False)