from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from jobhunter_api.models.stagemodel import StageModel
from jobhunter_api.models.jobmodel import JobModel
from jobhunter_api.views.jobview import JobSerializer

class StageSerializer(serializers.HyperlinkedModelSerializer):
    # job = serializers.StringRelatedField(many=False)
    class Meta:
        model = StageModel
        url = serializers.HyperlinkedIdentityField(
            view_name='stage',
            lookup_field='id'
        )
        fields = ('id', 'name', 'note', 'date', 'job_id')


class Stage(ViewSet):
    queryset = StageModel.objects.all()

    def list(self, request):
        """
        GET all
        List out all of contacts for a user
        """
        stage = StageModel.objects.all()
        serializer = StageSerializer(
            stage, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serializes college instance
        """
        new_stage = StageModel()
        new_stage.name = request.data["name"]
        new_stage.note = request.data["note"]
        new_stage.date = request.data["date"]
        new_stage.job = JobModel.objects.get(pk=request.data['job'])
        new_stage.save()
        serializer = StageSerializer(new_stage, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            stage = StageModel.objects.get(pk=pk)
            serializer = StageSerializer(stage, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        update_stage = StageModel.objects.get(pk=pk)
        update_stage.name = request.data["name"]
        update_stage.note = request.data["note"]
        update_stage.date = request.data["date"]
        update_stage.job = JobModel.objects.get(pk=request.data['job'])
        update_stage.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            stage = StageModel.objects.get(pk=pk)
            stage.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except StageModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
