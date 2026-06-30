import base64
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class GenerateLinksView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        site_file = request.FILES.get("site")
        emails_file = request.FILES.get("emails")

        if not site_file or not emails_file:
            return HttpResponse("Missing files", status=400)

        site_link = site_file.read().decode("utf-8").strip()
        emails = emails_file.read().decode("utf-8").splitlines()

        # Build output lines: only links
        links = []
        for email in emails:
            if email.strip():
                # ✅ Encode the email, not the site
                encoded_email = base64.b64encode(email.encode("utf-8")).decode("utf-8")
                link = f"{site_link}?email={encoded_email}"
                links.append(link)

        # Return as downloadable text file
        response = HttpResponse("\n".join(links), content_type="text/plain")
        response["Content-Disposition"] = 'attachment; filename="links.txt"'
        return response
