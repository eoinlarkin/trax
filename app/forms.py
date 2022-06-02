from django.forms import ModelForm
from .models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        #fields = ['gpx_file']
        fields = '__all__'
        exclude = ('user',) 
    
    def get_slug(self):
        # data = self.data.copy()
        # data['distance'] = 1000
        # self.data = data
         
        print(self.data['slug'])
        return self.data['slug']