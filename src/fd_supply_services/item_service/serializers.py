from django.contrib.auth.models import User
from rest_framework import serializers
from item_service.models import *


class UserSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = User
        fields = '__all__'

class UnitIdentificationCodeSerializer(serializers.ModelSerializer):
    """
    """

    url = serializers.HyperlinkedIdentityField(
            view_name='uic-detail',
            format='html',
            lookup_field='uic')

    class Meta:
        model = UnitIdentificationCode
        fields = '__all__'


class UnitOfIssueSerializer(serializers.ModelSerializer):
    """
    """
    url = serializers.HyperlinkedIdentityField(
            read_only=True,
            view_name='unitofissue-detail',
            format='html',
            lookup_field='code')

    class Meta:
        model = UnitOfIssue
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    """
    """

    url = serializers.HyperlinkedIdentityField(
            view_name='item-detail',
            format='html',
            lookup_field='nsn')

    class Meta:
        model = Item
        fields = '__all__'
