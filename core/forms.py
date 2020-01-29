# Django -------------------------------------------------------------------------------------------------------
from django import forms
# App ----------------------------------------------------------------------------------------------------------
class WorkItem_form(forms.ModelForm):
	class Meta:
		model = WorkItem
		exclude = ["children","parents"]
class Project_form(forms.ModelForm):
	class Meta:
		model = Project
		fields = "__all__"
