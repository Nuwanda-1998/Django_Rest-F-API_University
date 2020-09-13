from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError 

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Fields, PhysicalClass, Topics, ClassHolding

from . import serializers
from .permissions import IsAuthorOrReadOnly

from rest_framework import response, decorators, permissions, status




User = get_user_model()


class FieldViewset(viewsets.ModelViewSet):
    'The ViewSet For the fields list and field detail'
    queryset = Fields.objects.all()
    serializer_class = serializers.Fieldserializer
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        'Return Appropriate Serializer Class'
        if self.action == 'retrieve':
            return serializers.FieldDetailSerializer
        
        return self.serializer_class



class TopicViewset(viewsets.ModelViewSet):
    'The ViewSet For the fields list and field detail'
    queryset = Topics.objects.all()
    serializer_class = serializers.TopicSerializer
    permission_classes = [IsAuthenticated]



    def get_serializer_class(self):
        'Return Appropriate Serializer Class'
        if self.action == 'retrieve':
            return serializers.TopicDetailSerializer
        
        return self.serializer_class



class LocationViewset(viewsets.ModelViewSet):
    'The ViewSet For the fields list and field detail'
    queryset = PhysicalClass.objects.all()
    serializer_class = serializers.PhysicalClassSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        'Return Appropriate Serializer Class'
        if self.action == 'retrieve':
            return serializers.PhysicalClassDetailSerializer
        
        return self.serializer_class



class classViewset(viewsets.ModelViewSet):
    'The ViewSet For the classes list and classes Detail'
    queryset = ClassHolding.objects.all()
    serializer_class = serializers.ClasshSerializer
    #permission_classes = [IsAuthenticated]


    def get_queryset(self):
        'Return Object For the current authenticated user'
        user = self.request.user
        if user.is_teacher:
            return self.queryset.filter(teacher=user).order_by('-classh_id')
        else:
            #return self.queryset.filter(stu_enrolled_classes=user).order_by('-classh_id')
            return self.queryset.order_by('-classh_id')
        


    def perform_create(self, serializer):
        'Create A New Class'
        user = self.request.user
        if user.is_teacher:
            serializer.save(teacher=user)
        else:
            raise ValidationError("User Is not Teacher, So the acces is denied to create new class.")


    def perform_update(self, serializer):
        # Save with the new value for the target model fields
        user = self.request.user
        userid = str(user.id)
        serializer.save(stu_enrolled_classes=userid)
        


    def get_serializer_class(self):
        'Return Appropriate Serializer Class'
        if self.action == 'retrieve':
            return serializers.ClasshDetailSerializer
        
        return self.serializer_class




class UserUViewset(viewsets.ModelViewSet):
    'The ViewSet For the classes list and classes Detail'
    queryset = User.objects.all()
    serializer_class = serializers.UserDSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        'Return Appropriate Serializer Class'
        if self.action == 'retrieve':
            return serializers.UserDetailSerializer
        
        return self.serializer_class



# class TopicsList(generics.ListCreateAPIView):
#     queryset = Topics.objects.all()
#     serializer_class = TopicSerializer


# class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
#     'Shows the details of the detail of specific Topic'
#     queryset = Topics.objects.all()
#     serializer_class = TopicSerializer



# class LocationList(generics.ListCreateAPIView):
#     queryset = PhysicalClass.objects.all()
#     serializer_class = PhysicalClassSerializer


# class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
#     'Shows the details of the detail of specific Location'
#     queryset = PhysicalClass.objects.all()
#     serializer_class = PhysicalClassSerializer



# class classhList(generics.ListCreateAPIView):
#     queryset = ClassHolding.objects.all()
#     serializer_class = ClasshSerializer


# class classhDetail(generics.RetrieveUpdateDestroyAPIView):
#     'Shows the details of the detail of specific Class'
#     queryset = ClassHolding.objects.all()
#     serializer_class = ClasshSerializer


# class FieldsList(generics.ListCreateAPIView):
#     queryset = Fields.objects.all()
#     serializer_class = Fieldserializer


# class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
#     'Shows the details of the detail of specific Detail'
#     queryset = Fields.objects.all()
#     serializer_class = FieldDetailSerializer
