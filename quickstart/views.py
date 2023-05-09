from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from quickstart.models import FriendRequest, Friends
from quickstart.serializers import UserSerializer, RequestSerializer, OutcomingRequestSerializer, \
    IncomingRequestSerializer, FriendsSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['POST'], authentication_classes=[BasicAuthentication],
            permission_classes=[AllowAny])
    def register(self, request, *args, **kwargs):
        # print(args, kwargs)
        User.objects.create_user(username=request.POST['username'],
                                 password=request.POST['password'])
        return Response({'registered': True})


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
# serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

class RequestViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FriendRequest.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET', 'POST'], authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def outcoming(self, request, *args, **kwargs):
        # print(args, kwargs)
        objects = FriendRequest.objects.filter(from_id=request.user).filter(is_active=True)
        serializer = OutcomingRequestSerializer(objects, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    @action(detail=False, methods=['GET', 'POST'], authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def incoming(self, request, *args, **kwargs):
        # print(args, kwargs)
        objects = FriendRequest.objects.filter(to_id=request.user).filter(is_active=True)
        serializer = IncomingRequestSerializer(objects, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    @action(detail=False, methods=['POST'], authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def register(self, request, *args, **kwargs):
        # поиск уже имеющихся добавить
        FriendRequest.objects.create(from_id=request.user, to_id=User.objects.get(id=request.POST['id'])).save()
        return Response({'registered': True})


class FriendsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET', 'POST'], authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def outcoming(self, request, *args, **kwargs):
        # print(args, kwargs)
        objects = Friends.objects.filter(from_id=request.user).filter(is_active=True)
        serializer = OutcomingRequestSerializer(objects, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    @action(detail=False, methods=['POST'], authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def delete(self, request, *args, **kwargs):
        # print(args, kwargs)
        try:
            object = Friends.objects.filter(from_id=request.user).filter(to_id=request.POST['id']).filter(is_active=True).first()
            object.is_active = False
            object.save()
            object = Friends.objects.filter(from_id=request.POST['id']).filter(to_id=request.user).filter(is_active=True).first()
            object.is_active = False
            object.save()
        except:
            return Response({'completed': False})
        return Response({'completed': True})
