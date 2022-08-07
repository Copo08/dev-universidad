from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from estudiantes.models import Student
from estudiantes.serializers import StudentSerializer
# Create your views here por clase

class StudentView(APIView):

    def get(self, request):

        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)


 