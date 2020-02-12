from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
    # form을 통해 받아들여야할 데이터가 명시되어 있는 메타 데이터(db 테이블을 연결)
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) #사용자로부터 form 통해 입력받을 데이터가
        
