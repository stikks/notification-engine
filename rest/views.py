# import core python logic
import requests, json

# import core django modules
from django.http import HttpResponse

# import third party extensions modules
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import mixins, generics, status, views
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes

# import application modules
from .serializers import ClientApplicationSerializer, PushMessageSerializer
from .models import ClientApplication, PushMessage
from notification.settings import HTTP_POST_URL


class JSONResponse(HttpResponse):
    """ Custom HttpResponse to render its contents as JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'applications': reverse('app-list', request=request, format=format)
        # 'application-detail': reverse('app-detail', request=request, format=format)
    })


class ClientApplicationList(generics.ListCreateAPIView):
    """ API Endpoint for listing all user accounts or creating a new account
    """
    queryset = ClientApplication.objects.all()
    serializer_class = ClientApplicationSerializer
    permission_classes = [permissions.AllowAny]


class ClientApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    """ API Endpoint for listing all user accounts or creating a new account
    """
    queryset = ClientApplication.objects.all()
    serializer_class = ClientApplicationSerializer
    permission_classes = [permissions.AllowAny]


class SendDownstreamHTTP(views.APIView):
    """
    Send downstream messages from app server to client app
    """
    queryset = PushMessage.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        """
        Send downstream message via HTTP
        """
        api_key = request.data.get('api_key')
        if not api_key:
            return Response({"message": "GOOGLE API KEY Missing"}, status=status.HTTP_206_PARTIAL_CONTENT)

        application_name = request.data.get('name')

        if not application_name:
            return Response({"message": "application name missing"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            application = ClientApplication.objects.get(name=application_name)
        except ClientApplication.DoesNotExist:
            return Response({"message": "application not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['target'] = application.registration_id

        serializer = PushMessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            headers = {'Content-type': 'application/json', "Authorization": "key='%s'" % api_key}
            response = requests.post(url=HTTP_POST_URL, headers=headers, data=serializer.data)
            print 'response', response
            return Response(response.content, status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserList(views.APIView):
#     """ API Endpoint for listing all user accounts or creating a new account
#     """
#
#     def get(self, request, format=None):
#         """
#         Retrieve a list of all user accounts
#         """
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return Response(users_serializer.data)
#
#     def post(self, request, format=None):
#         """
#         Create a new user account from request information
#         """
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserDetail(views.APIView):
#     """ API Endpoint for retrieving, updating or deleting a user account
#     """
#
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Http404(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         """
#         Retrieve a user account
#         """
#         user = self.get_object(pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         """
#         Update a user account
#         """
#         user = self.get_object(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk,format=None):
#         """
#         Delete a user account
#         """
#         user = self.get_object(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class UserList(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
#     """ API Endpoint for listing all user accounts or creating a new account
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         """
#         Retrieve a list of all user accounts
#         """
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Create a new user account from request information
#         """
#         return self.create(request, *args, **kwargs)
#
#
# class UserDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
#     """ API Endpoint for retrieving, updating or deleting a user account
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         """
#         Retrieve a user account
#         """
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         """
#         Update a user account
#         """
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         """
#         Delete a user account
#         """
#         return self.destroy(request, *args, **kwargs)