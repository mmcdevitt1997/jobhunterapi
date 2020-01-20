from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from jobhunter_api.models.jobmodel import JobModel

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobModel
        url = serializers.HyperlinkedIdentityField(
            view_name='job',
            lookup_field='id'
        )
        fields = ('id', 'user', 'title', 'salary', 'job_link', 'active') 
        depth = 1

class Job(ViewSet):
    queryset = JobModel.objects.all()
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serializes college instance
        """
        new_job = JobModel()
        new_job.user = request.auth.user
        new_job.title = request.data["title"]
        new_job.salary = request.data["salary"]
        new_job.job_link = request.data["job_link"]
        new_job.active = request.data["active"]
        new_job.save()
        serializer = JobSerializer(new_job, context={'request': request})
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        try:
            job = JobModel.objects.get(pk=pk)
            serializer = JobSerializer(job, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        update_job = JobModel.objects.get(pk=pk)
        update_job.title = request.data["title"]
        update_job.salary = request.data["salary"]
        update_job.job_link = request.data["job_link"]
        update_job.active = request.data["active"]
        update_job.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            job = JobModel.objects.get(pk=pk)
            job.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except JobModel.DoesNotExist as ex:
           return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)