from rest_framework import serializers
from django.contrib.auth import get_user_model

from core.models import Fields, PhysicalClass, Topics, ClassHolding



class Fieldserializer(serializers.ModelSerializer):
    'Serializing the Fields Model'


    class Meta:
        model = Fields
        fields = ('id', 'name', 'Field_id', 'topics')
        read_only_fields = ('id', 'topics')



class TopicSerializer(serializers.ModelSerializer):
    'Serializing the Topics Model'
    

    class Meta:
        model = Topics
        fields = ('id', 'name', 'Topic_id', 'topic')
        read_only_fields = ('id',)



class PhysicalClassSerializer(serializers.ModelSerializer):
    'Serializing the Location'


    class Meta:
        model = PhysicalClass
        fields = ('id', 'class_Location_id', 'is_smart_class', 'capacity', 'classes')
        read_only_fields = ('id', 'capacity', 'classes',)
    


class ClasshSerializer(serializers.ModelSerializer):
    'Serialize the Holding classes'



    class Meta:
        model = ClassHolding
        fields = ('id', 'stu_enrolled_classes', 'teacher', 'Location', 'field', 'is_class_active', 'is_class_online', 'classh_id',)
        read_only_fields = ('id', 'teacher',)


class UserSerializer(serializers.ModelSerializer):
    'Serializing the user Model to use in relationals Field'

    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'email', 'National_id')
        read_only_fields = ('id', 'name', 'email', 'National_id')



class UserDSerializer(serializers.ModelSerializer):
    'Serializing the user Model to use To Show All User Data'

    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'email', 'National_id', 'is_active', 'stu_id', 'prof_id', 'choosed_topics', 'created_at', 'updated_at', 'is_teacher', 'classes', 'enrolled_classes')
        read_only_fields = ('id', 'created_at', 'updated_at', 'is_teacher')




########    from Now we are implementing DetailViews to usde in viewsets    #############



class FieldDetailSerializer(Fieldserializer):
    'Show the clean Data of Specific Field'
    topics = TopicSerializer(many=True, read_only=True)



class TopicDetailSerializer(TopicSerializer):
    'Show the clean Data of Specific Topic'
    topic = Fieldserializer(read_only=True)



class PhysicalClassDetailSerializer(PhysicalClassSerializer):
    'Show the clean Data of Specific Topic'
    classes = ClasshSerializer(many=True, read_only=True)



class ClasshDetailSerializer(ClasshSerializer):
    'Show the clean Data of Specific Topic'
    stu_enrolled_classes = UserSerializer(many=True, read_only=True)
    teacher = UserDSerializer(read_only=True)
    Location = PhysicalClassSerializer(read_only=True)
    field = Fieldserializer(read_only=True)



class UserDetailSerializer(UserDSerializer):
    'Show the clean Data of Specific User'
    choosed_topics = Fieldserializer(read_only=True)
    classes = ClasshDetailSerializer(many=True, read_only=True)
    enrolled_classes = ClasshDetailSerializer(many=True, read_only=True)
