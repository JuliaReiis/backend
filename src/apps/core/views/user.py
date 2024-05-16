import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models'))) 
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models.model import User


class UserView(User):

    @action(methods=['post'],
            detail=True,
            url_path='user',
            url_name='user')
    def create_user(self, request, pk=None):
        return Response({"teste":"teste"})
    
    @action(methods=['put'],
            detail=True,
            url_path='user',
            url_name='user')
    def update_user(self, request, pk=None):
        return Response({"testePUT":"testePUT"})
    