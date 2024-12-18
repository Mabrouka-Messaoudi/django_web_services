from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
class Client(AbstractUser):
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    num_tel = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='client_groups',  # Custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='client_permissions',  # Custom related name
        blank=True
    )
    
    def __str__(self):
        return self.username


# Signal to create Client when User is created
@receiver(post_save, sender=AbstractUser)
def create_client_for_user(sender, instance, created, **kwargs):
    if created:
        # Create a Client object when a User is created
        Client.objects.create(user=instance)


class Voyage(models.Model):
    id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=100)
    debut = models.DateField()
    fin = models.DateField()
    prix = models.FloatField()

    def __str__(self):
        return f"Voyage à {self.destination} du {self.debut.strftime('%d/%m/%Y')} au {self.fin.strftime('%d/%m/%Y')}"

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(prix__gte=0), name="prix_positive"),
            models.CheckConstraint(check=models.Q(debut__lt=models.F("fin")), name="valid_date_range"),
        ]
        indexes = [
            models.Index(fields=["destination"]),
            models.Index(fields=["debut", "fin"]),
        ]


class Reservation(models.Model):
    client = models.ForeignKey(Client, related_name="reservations", on_delete=models.CASCADE)  # User who made the reservation
    voyage = models.ForeignKey(Voyage, related_name="reservations", on_delete=models.CASCADE)  # Trip that was reserved
    date_reservation = models.DateTimeField(auto_now_add=True)  # When the reservation was made

    def __str__(self):
        return f"Reservation by {self.client.username} for {self.voyage.destination} on {self.date_reservation}"
