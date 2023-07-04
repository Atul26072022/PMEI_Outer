from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PDIModelSerializer
from .models import PDIModel,ScheduleCancellation
from rest_framework import viewsets

# Create your views here.
class PDIView(APIView):
    def get(self,request):
        data = PDIModel.objects.filter(PDI_READ_FLAG=False)
        serializer = PDIModelSerializer(data,many=True)

        return Response({
            "status" : 200,
            "data" : serializer.data
        })    
    
    def post(self,request):
        data = request.data
        serializer  = PDIModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : 200,
                "msg" : "Data Saved Successfully"
            })
    
    def patch(self,request):
        pdi_id = request.data["PDI_ID_INPUT_COIL"]
        pdi_obj = PDIModel.objects.get(PDI_ID_INPUT_COIL=pdi_id)
        pdi_obj.PDI_READ_FLAG = True
        pdi_obj.save()
        return Response({
                "status" : 200,
                "msg" : "Data updated successfully"
            })
        # serializer = PDIModelSerializer(pdi_obj,data=request.data,partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     print("pdi id gets updated",pdi_obj)
            

class ScheduleCancellationView(APIView):
    def get(self, request):
        coil = list(ScheduleCancellation.objects.filter(read_flag = False).values_list('specific_coil_no', flat=True))
        return Response({
            "data":coil
        })
    def post(self, request):
        print("post call")
        coil = request.data['coil']
        obj = ScheduleCancellation.objects.filter(specific_coil_no = coil, read_flag = False)
        cancell_obj = obj[0]
        cancell_obj.read_flag = True
        cancell_obj.save()
        return Response({
            "status":200
        })