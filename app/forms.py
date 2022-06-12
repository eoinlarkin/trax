from django.forms import ModelForm
from .models import Activity


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        # fields = ['gpx_file']
        fields = "__all__"
        exclude = (
            "user",
            "likes",
            "distance",
            "slug",
            "start_time",
            "end_time",
            "average_heartrate",
            "gpx_thumbnail",
            "gpx_thumb_path",
            "heartrate_avg",
            "elev_max",
            "elev_min",
        )

    def update_activity(self, commit=True):
        self.cleaned_data = dict(
            [
                (k, v)
                for k, v in self.cleaned_data.items()
                if k in ["description", "title"]
            ]
        )
        return super(ActivityForm, self).save(commit=commit)
