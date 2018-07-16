from rest_framework.response import Response
from rest_framework.views import APIView


class LogAPI(APIView):
	"""
	Logs API
	"""
	
	def post(self, request, *args, **kwargs):
		log = request.data
		return Response(data='hello '+log.get('user_name'),status=201)
