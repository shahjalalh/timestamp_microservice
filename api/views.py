from django.views import View
from django.http import JsonResponse
import datetime, time
import re


# Create your views here.
class TimestampAPIView(View):

    def get(self, request, *args, **kwargs):

        value = str(request.path).split('/')[-1]

        if value:

            if re.match("^[0-9]*$", value):
                print("all digits")
                natural = datetime.datetime.fromtimestamp(int(value)).strftime('%B %d, %Y')
                unix = value
            else:
                try:
                    pro_time = time.strptime(value, "%B %d, %Y")
                    unix = int(time.mktime(pro_time))
                    natural = value

                except:
                    unix = None
                    natural = None

            data = {"unix": unix, "natural": natural}
        else:
            data = {"unix": None, "natural": None}

        return JsonResponse(data, safe=False)
