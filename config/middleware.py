from ipware import get_client_ip
from django.http import HttpResponseForbidden
import requests, json


class IPAccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the client's IP address
        client_ip, _ = get_client_ip(request)

        # Replace 'your_ip_check_function' with your IP-to-country checking logic
        if not self.your_ip_check_function(client_ip):
            return HttpResponseForbidden(
                """
                <div class="center-screen" style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                <div class="message-box" style="background-color: #f0f0f0; padding: 20px; border: 1px solid #ccc; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                    <h1>Uzur ushbu sayt faqat O'zbekistonliklar uchun</h1>
                    <p>Sayt xozirda faqatgina O'zbekistonda ishlaydi server kattalashishi bilan website boshqa davlatlarda ham ish faoliyatini boshlaydi</p>
                </div>
                </div>
                """
            )

        response = self.get_response(request)
        return response

    def your_ip_check_function(self, client_ip):
        print(client_ip)
        try:
            if client_ip == "127.0.0.1":
                return True
            else:
                res = requests.get(f"http://ip-api.com/json/{client_ip}")
                r = res.text
                data = json.loads(r)
                allowed_countries = ["UZ"]
                return True if data["countryCode"] in allowed_countries else False

        except KeyError:
            pass
