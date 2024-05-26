from django.shortcuts import render , redirect
from .models import *
from django.db.models import Sum, F
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser , AllowAny
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction






class QuestionAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self ,request ):
        queryset = Question.objects.order_by('?')
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            with transaction.atomic():
                student_instance = serializer.save()    

                all_data = ['Back-end', 'Front-end', 'Design', '3D Modeling', 'Marketing']
                existing_interests = Interest.objects.filter(title__in=all_data, students=student_instance)


                new_interests = [Interest(students=student_instance, title=title) for title in all_data if title not in existing_interests.values_list('title', flat=True)]

                Interest.objects.bulk_create(new_interests)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        

        
                
    
       

class CheckAnswerAPIView(APIView):
    def post(self, request):             
        quiz_id = request.data.get("quiz_id")
        answer_id = request.data.get("answer_id")
        answer = get_object_or_404(Answer, id=answer_id)
        question = get_object_or_404(Question, id=quiz_id)
        student = Student.objects.latest('id')

        if answer.category == question.category:
            interest = Interest.objects.get(students=student, title=question.category.title)
            interest.quantity += 1
            interest.save()
            return Response(status=status.HTTP_200_OK)
        else:
            interest = Interest.objects.get(students=student, title=answer.category.title)
            interest.quantity += 1
            interest.save()
            return Response(status=status.HTTP_200_OK)
        


        


        
  

class ResultAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            student = Student.objects.latest('id')
            student_interests = Interest.objects.filter(students=student)
            sorted_interests = student_interests.order_by('-quantity')
            total_quantity = student_interests.aggregate(Sum('quantity'))['quantity__sum'] or 0

            if total_quantity == 0:
                return Response({'error': 'Total quantity is zero'}, status=400)

            for interest in sorted_interests:
                interest.percent = round((interest.quantity / total_quantity) * 100)

            serializer = InterestSerializer(sorted_interests, many=True)
            return Response(serializer.data)

        except Student.DoesNotExist as e:
            logger.error(f"An error occurred: {e}")
            return Response({'error': 'Student not found'}, status=404)
        except ZeroDivisionError as e:
            logger.error(f"An error occurred: {e}")
            return Response({'error': 'Division by zero'}, status=500)

