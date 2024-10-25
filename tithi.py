

from skyfield.api import load, Topos
from datetime import datetime, timedelta

tithi_names = [
        "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", 
        "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
        "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima/Amavasya"
    ]
def calculate_tithi(year,month,day):

    date = datetime(year,month,day) 
    # Load the JPL ephemeris DE421 (covers 1900-2050).
    planets = load('de421.bsp')
    earth, moon, sun = planets['earth'], planets['moon'], planets['sun']
    
    # Define the date and time (UTC)
    ts = load.timescale()
    t = ts.utc(date.year, date.month, date.day, 0, 0, 0)
    
    # Calculate the ecliptic longitude of Moon and Sun
    astrometric_moon = earth.at(t).observe(moon).apparent()
    astrometric_sun = earth.at(t).observe(sun).apparent()
    
    moon_longitude = astrometric_moon.ecliptic_latlon()[1].degrees
    sun_longitude = astrometric_sun.ecliptic_latlon()[1].degrees
    
    # Calculate the angular difference
    angular_difference = (moon_longitude - sun_longitude) % 360
    
    # Calculate the Tithi number
    tithi_index = int(angular_difference // 12) + 1  # 1 to 30

    # Determine Paksha (Shukla or Krishna)
    paksha = "Shukla Paksha" if tithi_index <= 15 else "Krishna Paksha"
    tithi_number = tithi_index if tithi_index <= 15 else tithi_index - 15


    tithi_name = tithi_names[tithi_number - 1]  # Adjusted for 0-based index

    return f"{tithi_name} ({paksha})"




