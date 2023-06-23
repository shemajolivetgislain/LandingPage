from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mission, Vision, Objective, About
from .serializers import MissionSerializer, VisionSerializer, ObjectiveSerializer, AboutSerializer

class AboutAPIView(APIView):
    def get(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AboutSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AboutDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return About.objects.get(pk=pk)
        except About.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        about = self.get_object(pk)
        serializer = AboutSerializer(about)
        return Response(serializer.data)

    def put(self, request, pk):
        about = self.get_object(pk)
        serializer = AboutSerializer(about, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        about = self.get_object(pk)
        about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MissionAPIView(APIView):
    def get(self, request):
        mission = Mission.objects.all()
        serializer = MissionSerializer(mission, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MissionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class MissionDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Mission.objects.get(pk=pk)
        except Mission.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        mission = self.get_object(pk)
        serializer = MissionSerializer(mission)
        return Response(serializer.data)

    def put(self, request, pk):
        mission = self.get_object(pk)
        serializer = MissionSerializer(mission, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        mission = self.get_object(pk)
        mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class VisionAPIView(APIView):
    def get(self, request):
        vision = Vision.objects.all()
        serializer = VisionSerializer(vision, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VisionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class VisionDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Vision.objects.get(pk=pk)
        except Vision.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        vision = self.get_object(pk)
        serializer = VisionSerializer(vision)
        return Response(serializer.data)

    def put(self, request, pk):
        vision = self.get_object(pk)
        serializer = VisionSerializer(vision, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        vision = self.get_object(pk)
        vision.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ObjectiveAPIView(APIView):
    def get(self, request):
        objective = Objective.objects.all()
        serializer = ObjectiveSerializer(objective, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ObjectiveSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ObjectiveDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Objective.objects.get(pk=pk)
        except Objective.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        objective = self.get_object(pk)
        serializer = ObjectiveSerializer(objective)
        return Response(serializer.data)

    def put(self, request, pk):
        objective = self.get_object(pk)
        serializer = ObjectiveSerializer(objective, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        objective = self.get_object(pk)
        objective.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
