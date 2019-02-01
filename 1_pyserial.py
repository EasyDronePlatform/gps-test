import serial
import pynmea2
import collections
def signal_handle( sig, frame ):
    # Save JSON
    import json
    with open( '/home/mpkuse/try/gps_nmea/data.json', 'w' ) as outfile:
            json.dump( ARY, outfile )
    exit(0)

ser = serial.Serial( '/dev/ttyUSB0', 4800 )
ARY =  collections.OrderedDict() # To save the data for reference
import signal
signal.signal( signal.SIGINT, signal_handle )
while True:
    print '\n---'

    # Get data from the device
    line = ser.readline()
    print "raw data:", line

    # Parse the data
    try:
        msg = pynmea2.parse( line )
        #print 'status=', msg.status,
        print 'lat=', msg.lat,
        print 'lon=', msg.lon,
        #print '#sats=', msg.num_sats,
        print 'datetime=', msg.datetime
        #ARY.append( (msg.datetime,msg.latitude, msg.latitude_minutes, msg.latitude_seconds, msg.longitude, msg.longitude_minutes, msg.longitude_seconds) )
        Q = {}
        Q[ 'latitude' ] = float(msg.latitude)
        Q[ 'latitude_minutes' ] = float(msg.latitude_minutes)
        Q[ 'latitude_seconds' ] = float(msg.latitude_seconds)
        Q[ 'longitude' ] = float(msg.longitude)
        Q[ 'longitude_minutes' ] = float(msg.longitude_minutes)
        Q[ 'longitude_seconds' ] = float(msg.longitude_seconds)
        Q[ 'lat'] = float(msg.lat)
        Q['lon'] = float(msg.lon)
        ARY[ msg.datetime.__str__() ] = Q
    except:
        continue
