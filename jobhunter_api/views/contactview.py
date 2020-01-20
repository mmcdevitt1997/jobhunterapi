from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from jobhunter_api.models.Companymodel import CompanyModel
from jobhunter_api.models.contactmodel import ContactModel

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactModel
        url = serializers.HyperlinkedIdentityField(
            view_name='contact',
            lookup_field='id'
        )
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'title', 'company','email')
        depth = 1

class Contact(ViewSet):
    queryset = ContactModel.objects.all()
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serializes college instance
        """
        new_contact = ContactModel()
        new_contact.first_name = request.data["first_name"]
        new_contact.last_name = request.data["last_name"]
        new_contact.title = request.data["title"]
        new_contact.email = request.data["email"]
        new_contact.phone_number = request.data["phone_number"]
        new_contact.company = CompanyModel.objects.get(pk=request.data['job'])
        new_contact.save()
        serializer = ContactSerializer(new_contact, context={'request': request})
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        try:
            contact = ContactModel.objects.get(pk=pk)
            serializer = ContactSerializer(contact, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        update_contact = ContactModel.objects.get(pk=pk)
        update_contact.first_name = request.data["first_name"]
        update_contact.last_name = request.data["last_name"]
        update_contact.title = request.data["title"]
        update_contact.email = request.data["email"]
        update_contact.phone_number = request.data["phone_number"]
        update_contact.company = CompanyModel.objects.get(pk=request.data['job'])
        update_contact.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            contact = ContactModel.objects.get(pk=pk)
            contact.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ContactModel.DoesNotExist as ex:
           return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)