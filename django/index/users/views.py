from users.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class Signup(APIView):
    def post(self, request): 
        email = request.data.get('email')

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email is already in use."}, status=400)

        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        except Exception as error:
            return Response({"error": str(error)}, status=500)

        
class Login(APIView):
    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
            if user:
                serializer = UserSerializer(user)
                return Response(serializer.data, status=200)
            return Response({"error": "User not found."}, status=404)
        except User.DoesNotExist:
            return Response({"error": "Failed to fetch user."}, status=500)
