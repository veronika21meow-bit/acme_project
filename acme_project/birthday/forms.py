# birthday/forms.py
from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday, Congratulation


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        } 
        # Указываем, что надо отобразить все поля.
        fields = '__all__'


class CongratulationForm(forms.ModelForm):
    
    class Meta:
        model = Congratulation
        fields = ('text',) 