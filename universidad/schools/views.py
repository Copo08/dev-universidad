from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from schools.models import School
from schools.serializers import SchoolSerializer
# Create your views here por clase

class SchoolView(APIView):

    def get(self, request):

        schools = School.objects.all()
        print(schools)
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=SchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

# Create your views here.
