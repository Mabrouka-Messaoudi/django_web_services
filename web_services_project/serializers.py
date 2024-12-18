from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Client,Reservation,Voyage
from django.contrib.auth.models import User
class ClientSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Client
        fields = ['id','nom','prenom','num_tel','adresse']
    def create(self, validated_data):
        username = validated_data.get('prenom') + validated_data.get('nom')
        user = Client.objects.create_user(
            username=username,
            nom=validated_data['nom'],
            prenom=validated_data['prenom'],
            num_tel=validated_data['num_tel'],
            adresse=validated_data['adresse'],
            #phone_number=validated_data.get('phone_number')
        )
        return user

class VoyageSerializer(serializers.ModelSerializer):
    debut = serializers.DateField(format='%d/%m/%Y', input_formats=['%Y-%m-%d', '%d/%m/%Y'])
    fin = serializers.DateField(format='%d/%m/%Y', input_formats=['%Y-%m-%d', '%d/%m/%Y'])

    class Meta:
        model = Voyage
        fields = ['id', 'destination', 'debut', 'fin', 'prix']
    
    def validate(self, data):
        """
        Validation personnalisée des données.
        """
        if data['debut'] >= data['fin']:
            raise serializers.ValidationError("La date de début doit être antérieure à la date de fin.")
        if data['prix'] < 0:
            raise serializers.ValidationError("Le prix doit être supérieur ou égal à zéro.")
        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    nom = serializers.CharField(required=False, allow_blank=True)
    prenom = serializers.CharField(required=False, allow_blank=True)
    num_tel = serializers.CharField(required=False, allow_blank=True)
    adresse = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Client
        fields = ['username', 'email', 'password', 'nom', 'prenom', 'num_tel', 'adresse']

    def create(self, validated_data):
        user = Client.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            nom=validated_data.get('nom', ''),
            prenom=validated_data.get('prenom', ''),
            num_tel=validated_data.get('num_tel', ''),
            adresse=validated_data.get('adresse', '')
        )

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        return user
class ReservationSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()  # Returns the username of the client
    voyage = VoyageSerializer()  # Serialize the voyage data
    
    class Meta:
        model = Reservation
        fields = ['id', 'client', 'voyage', 'date_reservation']

    def create(self, validated_data):
        # Customize this if needed (e.g., if you need special handling of the user or voyage)
        return Reservation.objects.create(**validated_data)
class UserSerializer(serializers.ModelSerializer):
    # Including the Client fields in the User serializer
    nom = serializers.CharField(max_length=100, required=False)
    prenom = serializers.CharField(max_length=100, required=False)
    num_tel = serializers.CharField(max_length=15, required=False)
    adresse = serializers.CharField(style={'base_template': 'textarea.html'}, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'nom', 'prenom', 'num_tel', 'adresse']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract client fields
        client_data = {key: validated_data.pop(key) for key in ['nom', 'prenom', 'num_tel', 'adresse'] if key in validated_data}
        
        # Create the User instance
        user = User.objects.create_user(**validated_data)

        # Create the Client instance and associate it with the newly created User
        Client.objects.create(user=user, **client_data)

        return user