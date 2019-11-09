from django import forms
from .models import (
	Score,
	User_has_score
)

# Formulário de pontuação, pode ser penalidade ou bônus
class Score_Form(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['type_score', 'score_description', 'equivalent_score', 'score_specification']

    # Função que salva a pontuação no banco de dados
    def save(self, commit=True):
        score = super().save(commit=False)
        if commit:
            score.save()
        return score

# Formulário para aplicação de pontuação a um usuário específico
class Apply_Score_Form(forms.ModelForm):
	class Meta:
		model = User_has_score
		fields = ['user', 'score', 'score_comment', 'admin_username']