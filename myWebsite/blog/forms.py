from django import forms

class contactForm (forms.Form):

    Nama_Lengkap = forms.CharField(
        label= "Nama Lengkap",
        max_length=20,
        widget=forms.TextInput(
                attrs = {
                'class':'form-control',
                'placeholder':'Masukan Nama Lengkap Anda'
            }
        )
    )

    Jenis_Kelamin = forms.ChoiceField(
        choices = [
            ('P','Pria'),
            ('W','Wanita'),
        ],
        label= "Pilih Jenis Kelamin Anda",
        widget=forms.RadioSelect(
            attrs={
                'class':'form-check-input'
            }
        )

    )

    Tanggal_Lahir = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1945,2023),
            attrs= {
                'class':'form-select mb-3 bg-light'
            }
        )
    )


    email = forms.EmailField(
        label="Email",
        max_length=30,
        widget=forms.TextInput(
            attrs= {
                'class':'form-control mt-1',
                'placeholder':'Masukan Email Anda',
            }
        )
    )

    alamat = forms.CharField(
        label="Masukan Alamat Anda",
        widget=forms.Textarea(
            attrs= {
                'class':'form-control mt-1',
                'rows':'5',
            }
        )
    )

    agree = forms.BooleanField(
        label="Agree Terms And Conditions",
        widget= forms.CheckboxInput(
            attrs={
                'class':'form-check-input'
            }
        )
    )
