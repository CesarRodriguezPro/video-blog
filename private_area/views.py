from django.views.generic import TemplateView

# private_area


class Home(TemplateView):
    template_name = "private_area/main.html"
