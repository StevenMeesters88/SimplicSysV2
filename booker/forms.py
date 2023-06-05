from django import forms


class NewUserForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=6, label='Reg Nr')
    first_name = forms.CharField(max_length=255, label='Förnamn')
    last_name = forms.CharField(max_length=255, label='Efternamn')
    email = forms.EmailField(max_length=255, label='E-post')
    phone = forms.CharField(max_length=20, label='Telefon')
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255, label='Lösenord')


class BokaLoggedIn(forms.Form):
    service_date = forms.DateTimeField(widget=forms.DateTimeInput)
    notes = forms.CharField(widget=forms.Textarea)


class BokaLoggedOut(forms.Form):
    regnr = forms.CharField(min_length=6, max_length=6, label='regnr')
    first_name = forms.CharField(max_length=255, label='Förnamn')
    last_name = forms.CharField(max_length=255, label='Efternamn')
    email = forms.EmailField(max_length=255, label='E-post')
    phone = forms.CharField(max_length=20, label='Telefon')
    service_date = forms.DateTimeField(widget=forms.DateTimeInput)
    notes = forms.CharField(widget=forms.Textarea)


class KontaktLoggedIn(forms.Form):
    meddelande = forms.CharField(widget=forms.Textarea)


class KontaktLoggedOut(forms.Form):
    regnr = forms.CharField(min_length=6, max_length=6, label='Reg Nr')
    namn = forms.CharField(max_length=255, label='Namn')
    email = forms.EmailField(max_length=255, label='E-post')
    phone = forms.CharField(max_length=20, label='Telefon')
    meddelande = forms.CharField(widget=forms.Textarea, label='Meddelande')
