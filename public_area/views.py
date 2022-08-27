from django.views.generic import TemplateView

# public area


class Home(TemplateView):
    template_name = "public_area/main.html"
