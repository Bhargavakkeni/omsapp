from rest_framework import serializers
from loginapp.models import OmsAdmin


class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = OmsAdmin
        fields = ['id','brand','shipMethod','processingDays','processingDaysType','min','max','processingDate','availableToPromiseDate','cutOff','username']