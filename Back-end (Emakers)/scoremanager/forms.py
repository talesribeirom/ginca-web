from django import forms
from .models import (
	Score,
	User_has_score
)

class Score_Form(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['type_score', 'score_description', 'equivalent_score']

    def save(self, commit=True):
        score = super().save(commit=False)
        if commit:
            score.save()
        return score

class Apply_Score_Form(forms.ModelForm):
	class Meta:
		model = User_has_score
		fields = ['user', 'score', 'score_comment']