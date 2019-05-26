from django import forms
from .models import Video,VideoUpload

class Form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title','Embed_code','Description',)

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model= VideoUpload
        fields= ('__all__')