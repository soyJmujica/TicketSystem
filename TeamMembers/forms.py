from django.forms import ModelForm
from django import forms
from .models import TeamMembers

class TeamForm(ModelForm):
	"""docstring for TeamForm"""
	class Meta:
		model = TeamMembers
		fields = ['name', 'phone','email']
