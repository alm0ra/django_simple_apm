from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from common.tasks import my_task
from time import sleep

class SimpleView(APIView):
    @staticmethod
    def get(request):
        my_task.delay()
        sleep(5)
        data = {
            'status': 'success',
            'id': 0,
            'detail': 'Task start to run'
        }
        return Response(data, status=status.HTTP_200_OK)

    