from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Client,Reservation, Voyage
from .serializers import ClientSerializer,ReservationSerializer,VoyageSerializer
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


@api_view(['GET','POST'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, id, name):
    """
    Retrieve, update, or delete a client by id and name.
    """
    try:
        client = Client.objects.get(id=id, nom=name)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        client.delete()
        return Response({'message': 'Client deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail1(request, id):
    """
    Retrieve, update, or delete a client by id and name.
    """
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        client.delete()
        return Response({'message': 'Client deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_reservations(request):
    # Ensure user is authenticated
    client = Client.objects.first()  # The user should be authenticated at this point

    # Fetch reservations for the authenticated client
    reservations = Reservation.objects.filter(client=client)

    # Check if reservations exist
    if not reservations.exists():
        return Response({"message": "No reservations found."}, status=status.HTTP_200_OK)

    # Serialize the reservations
    serializer = ReservationSerializer(reservations, many=True)

    # Return the list of reservations
    return Response({
        'message': 'Reservations fetched successfully',
        'reservations': serializer.data
    }, status=status.HTTP_200_OK)

    


@api_view(['POST'])
def create_reservation(request):
    # Debug: Bypass authentication for testing
    client = Client.objects.first()  # Replace with specific client if needed

    # Validate voyage_id
    voyage_id = request.data.get('voyage_id')
    if not voyage_id:
        return Response({'error': 'Voyage ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        voyage = Voyage.objects.get(id=voyage_id)
        reservation = Reservation.objects.create(client=client, voyage=voyage)
        serializer = ReservationSerializer(reservation)
        return Response({
            'message': f'Reservation created successfully for {voyage.destination}',
            'reservation': serializer.data
        }, status=status.HTTP_201_CREATED)
    except Voyage.DoesNotExist:
        return Response({'error': 'Voyage not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@api_view(['GET', 'POST'])
def voyage_list(request):
    """
    Gèrer les recherches et l'ajout de voyages .
    """
    if request.method == 'GET':
        # Recherche des voyages selon les critères
        
        voyage_id = request.query_params.get('id')
        destination = request.query_params.get('destination')
        debut = request.query_params.get('debut')
        fin = request.query_params.get('fin')
        prix = request.query_params.get('prix')

        voyages = Voyage.objects.all()
        try:
            if debut:
                debut = datetime.strptime(debut, "%d/%m/%Y").date()
            if fin:
                fin = datetime.strptime(fin, "%d/%m/%Y").date()
        except ValueError:
            return Response({'error': 'Format de date invalide. Utilisez DD/MM/YYYY.'}, status=status.HTTP_400_BAD_REQUEST)

        # Appliquer les filtres
        if voyage_id:
            voyages = voyages.filter(id=voyage_id)
        if destination:
            voyages = voyages.filter(destination__icontains=destination)
        if debut:
            voyages = voyages.filter(debut__gte=debut)
        if fin:
            voyages = voyages.filter(fin__lte=fin)
        if prix:
            voyages = voyages.filter(prix=prix)

        serializer = VoyageSerializer(voyages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Ajouter un nouveau voyage
        serializer = VoyageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def reservation_detail(request, id):
    """
    Retrieve, update, or delete a reservation by id.
    """
    try:
        reservation = Reservation.objects.get(id=id)
    except Reservation.DoesNotExist:
        return Response({'error': 'Reservation not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve a single reservation
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        # Update an existing reservation
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # Delete a reservation
        reservation.delete()
        return Response({'message': 'Reservation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def voyage_detail(request, pk):
    """
    Gèrer la récupération, la modification et la suppression d'un voyage .
    """
    try:
        voyage = Voyage.objects.get(pk=pk)
    except Voyage.DoesNotExist:
        return Response({'error': 'Voyage non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retourne les détails d'un voyage spécifique
        serializer = VoyageSerializer(voyage)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Modifier un voyage existant
        serializer = VoyageSerializer(voyage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Supprimer un voyage existant
        voyage.delete()
        return Response({'message': 'Voyage supprimé avec succès'}, status=status.HTTP_204_NO_CONTENT)



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientMeView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this endpoint

    def get(self, request):
        serializer = ClientSerializer(request.user)  # `request.user` is the authenticated user
        return Response(serializer.data)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    reservation_data = []

    for reservation in reservations:
        reservation_data.append({
            'id': reservation.id,
            'trip_destination': reservation.voyage.destination,
            'trip_debut': reservation.voyage.debut,
            'trip_fin': reservation.voyage.fin,
            'price': reservation.voyage.prix,
            
        })

    return Response(reservation_data, status=status.HTTP_200_OK)