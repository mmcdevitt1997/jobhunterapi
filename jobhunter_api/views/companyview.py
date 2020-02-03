from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from jobhunter_api.models.companymodel import CompanyModel
from jobhunter_api.models.jobmodel import JobModel

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyModel
        url = serializers.HyperlinkedIdentityField(
            view_name='company',
            lookup_field='id'
        )
        fields = ('id', 'name', 'should_apply', 'job')
        depth = 1

class Company(ViewSet):
    queryset = CompanyModel.objects.all()
    def list(self, request):
        """
        GET all
        List out all of contacts for a user
        """
        company = CompanyModel.objects.all()

        serializer = CompanySerializer(
        company, many=True, context={'request': request})
        return Response(serializer.data, status=200)
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serializes college instance
        """
        new_company = CompanyModel()
        new_company.name = request.data["name"]
        new_company.should_apply = request.data["should_apply"]
        new_company.job = JobModel.objects.get(pk=request.data['job'])
        new_company.save()
        serializer = CompanySerializer(new_company, context={'request': request})
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        try:
            company = CompanyModel.objects.get(pk=pk)
            serializer = CompanySerializer(company, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        update_company = CompanyModel.objects.get(pk=pk)
        update_company.name = request.data["name"]
        update_company.should_apply = request.data["should_apply"]
        update_company.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            company = CompanyModel.objects.get(pk=pk)
            company.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except CompanyModel.DoesNotExist as ex:
           return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)