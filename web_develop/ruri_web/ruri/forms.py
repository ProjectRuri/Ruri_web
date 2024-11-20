from django import forms
from ruri.models import wav_file

class wav_files(forms.ModelForm):
    class Meta:
        model = wav_file
        fields = ['name','content']
        labels = {
            'name' : '제목',
            'content' : '내용',
        }