from django import forms


attrs = {'class': 'form-control'}


class CartForm(forms.Form):
    first_name = forms.CharField(label='ФИО', max_length=32, widget=forms.TextInput(attrs=attrs))
    phone_number = forms.RegexField(
        label='Телефон',
        regex=r'^\d{9,15}$',
        # error_message='Не вырный формат номера (пример: 8 913 123 4567)',
        widget=forms.TextInput(attrs={
            'class': 'form-control bfh-phone',
            'data-format': '+7 (ddd) ddd-dd-dd'
        })
    )
    city = forms.CharField(label='Город', max_length=64, widget=forms.TextInput(attrs=attrs))
    street = forms.CharField(label='Улица', max_length=64, widget=forms.TextInput(attrs=attrs))
    building = forms.CharField(label='Дом', required=False, max_length=4, widget=forms.TextInput(attrs=attrs))
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={
        **attrs,
        'rows': 5
    }))
