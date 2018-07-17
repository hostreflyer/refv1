from django.db import models
import datetime
# Create your models here.

class Check(models.Model):
    FLIGHT_SEGMENT_CHOICES = (
        ('1', '1 segment'),
        ('2', '2 segments'),
        ('3', '3 segments'),
        ('4', '4 segments'),
        ('5', '5 segments'),
        ('6', '6 segments'),
    )
    flight_segments = models.CharField(
        max_length=1,
        choices=FLIGHT_SEGMENT_CHOICES,
        default='1',
    )

    AIRLINE_CHOICES = (
        ('CHOS', 'Choose Airline'),
        ('LUHG', 'Lufthansa Group'),
        ('RYAN', 'Ryanair'),
        ('INAG', 'International Airlines Group'),
        ('AKLM', 'Air France-KLM'),
        ('EASJ', 'easyJet'),
        ('AERO', 'Aeroflot Group'),
        ('NASA', 'Norwegian Air Shuttle ASA'),
        ('SASG', 'SAS Group'),
        ('WZZA', 'Wizz Air'),
        ('AITA', 'Alitalia'),
        ('TAAP', 'TAP Air Portugal'),
        ('S7GP', 'S7 Group'),
        ('AEGA', 'Aegean Airlines'),
        ('FINA', 'Finnair'),
        ('AEUR', 'Air Europa'),
        ('JET2', 'Jet2.com'),
        ('FLYB', 'flybe'),
        ('LOTP', 'LOT Polish Airlines'),
        ('NORD', 'Nordica'),
        ('TRSA', 'Travel Service Airlines '),
        ('CZAL', 'Czech Airlines'),
        ('URAI', 'Ural Airlines'),
        ('UTAV', 'UTair Aviation'),
        ('UKIA', 'Ukraine International Airlines'),
        ('VIAT', 'Virgin Atlantic'),
        ('BLUA', 'Blue Air'),
        ('VOLO', 'Volotea'),
        ('ICEG', 'Icelandair Group'),
        ('AIBA', 'AirBaltic'),
        ('NOAI', 'Nordwind Airlines'),
        ('BELA', 'Belavia'),
        ('WOWA', 'WOW air'),
        ('AISE', 'Air Serbia'),
        ('TARO', 'TAROM'),
        ('VIMA', 'VIM Airlines'),
        ('CROA', 'Croatia Airlines'),
        ('MERI', 'Meridiana'),
        ('AIRM', 'Air Malta'),
        ('LUXA', 'Luxair'),
        ('AZAI', 'Azerbaijan Airlines'),
        ('BULG', 'Bulgaria Air'),
        ('ENAI', 'Enter Air'),
        ('ADAI', 'Adria Airways'),
        ('AZUA', 'Azur Air'),
        ('ELLA', 'Ellinair'),
    )
    airline = models.CharField(
        max_length=4,
        choices=AIRLINE_CHOICES,
        default='',
    )
    flight_no = models.CharField(max_length=25)
    departure_date = models.DateField(default=datetime.date.today)
    overbooked = models.BooleanField(default=False)
