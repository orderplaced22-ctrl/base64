from django.urls import path
from .views import GenerateLinksView

urlpatterns = [
    path(
        "generate-links/", GenerateLinksView.as_view(), name="generate_links"
    ),  # ✅ correct
]
