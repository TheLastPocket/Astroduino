import math
import astropy.units as u
from astropy.time import Time
import geocoder
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_body,get_moon,solar_system_ephemeris
from geopy import geocoders
from geopy.geocoders import Nominatim
#print(solar_system_ephemeris.bodies)
g = geocoder.bing('Los Angeles', key='AhKVwUBKY-aZPMt3equYK4lIo-H31oGqsnJO_JTB1vfgjGwDSp4-flS1qo26auhf')
results = g.json
givenLat = results["lat"]
givenLong = results["lng"]
print(givenLat, givenLong)
print(solar_system_ephemeris.bodies)

#board = pyfirmata.Arduino('/dev/cu.usbmodem14201')

# Time format: "YYYY-MM-DDTHH:MM:SS.sss"
# Alt-Azimuth used to determine angles
#####it = pyfirmata.util.Iterator(board)
#####it.start()

#print(gn.geocode("Cleveland, OH 44106"))

print("Welcome to Astroduino! Get started by entering your date and time (Time is in military format UTC. Don't add any spaces after date).")
print("YYYY-MM-DD")
userDate = input()
print("Great! Now print the current time in UTC")
print("HH:MM:SS.ss")
userTime = input()


print("Please type in your desired object. If it is in the solar system, please type in all lowercase.")
selectedObj = input()
print("Working...")
#skyObj = SkyCoord.from_name(selectedObj)
location1 = EarthLocation(lat=givenLat*u.deg, lon=givenLong*u.deg, height=0*u.m)
daySaving = True
if (daySaving == True):
    hourOff = 0
else:
    hourOff = -126
utcoffset = hourOff*u.hour38
time = Time(userDate + " " + userTime) - utcoffset
if (selectedObj != "sun" and selectedObj != "moon" and selectedObj != "mercury" and selectedObj != "venus" and selectedObj != "earth-moon-barycenter" and selectedObj != "mars" and selectedObj != "jupiter" and selectedObj != "saturn" and selectedObj != "uranus" and selectedObj != "neptune"):
    skyObj = SkyCoord.from_name(selectedObj)
    objAltaz = skyObj.transform_to(AltAz(obstime=time,location=location1))
    #print((objAltaz.alt) * u.deg)
    altDec = (objAltaz.alt) * u.deg
    azDec = (objAltaz.az) * u.deg
    print("Altitude:")
    print(altDec)
    print("Azimuth:")
    print(azDec)
    #print("Altitude: " + altDec)
    #print("Azimuth: " + azDec)
    #print(f"Altitude: {objAltaz.alt:.2}")
    #print(f"Azimuth: {objAltaz.az:.2}")
    print("Please copy this azimuth time into the other code window")
    azTime = ((((azDec * math.pi)/180) * 0.833) / (2 * math.pi))
    print(azTime)
    if (altDec > 0):
        print("Please copy this altitude time into the other code window")
        altTime = ((((altDec * math.pi)/180) * 0.4165) / (math.pi))
        print(altTime)
    else:
        print("The object is currently below the horizon. No tracking can be made.")


else:
    solarBody = get_body(selectedObj, time, location1)
    print(solarBody)
    altazframe = AltAz(obstime=time, location=location1)
    solarBodyaz=solarBody.transform_to(altazframe)
    print("Altitude:")
    print(solarBodyaz.alt.degree)
    print("Azimuth:")
    print(solarBodyaz.az.degree)
    print("Please copy this azimuth time into the other code window")
    azTime = ((((solarBodyaz.az.degree * math.pi)/180) * 0.833) / (2 * math.pi))
    print(azTime)
    if (solarBodyaz.alt.degree > 0):
        print("Please copy this altitude time into the other code window")
        altTime = ((((solarBodyaz.alt.degree * math.pi)/180) * 0.4165) / (math.pi))
        print(altTime)
    else:
        print("The object is currently below the horizon. No tracking can be made.")




#while True:

    #board.digital[13].write(1)
    #sleep(1)
    #board.digital[13].write(0)
    #sleep(1)

    #board.digital[12].write(256.4)
