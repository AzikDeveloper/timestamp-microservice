from rest_framework.views import APIView
from datetime import datetime
from rest_framework.response import Response


# Create your views here.

class TimeStampView(APIView):
    def get(self, request, time: str):
        try:
            dt = datetime.strptime(time, '%Y-%m-%d')
            unix = datetime.timestamp(dt)
        except ValueError:
            try:
                dt = datetime.fromtimestamp(int(time))
                unix = time
            except ValueError:
                return Response(data={
                    'error': 'Invalid Date'
                })

        result = {
            'unix': unix,
            'utc': dt.strftime('%A, %d %b %Y %H:%M:%S GMT')
        }
        return Response(data=result)
