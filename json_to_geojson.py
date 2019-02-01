# Geojson is a common format used on the internet for plotting geo-cordinates
import json

with open( 'data.json') as f:
    data = json.load( f )


cords = []
for k in data.keys():
    #print data[k]
    lat = float(data[k]["latitude"]) +\
          float( data[k]["latitude_minutes"] )/60. +\
          float( data[k]["latitude_seconds"] )/3600.
    long = float(data[k]["longitude"]) +\
        float( data[k]["longitude_minutes"] )/60. +\
        float( data[k]["longitude_seconds"] )/3600.
    print '---'
    print long,',', lat
    #cords.append( [round(long,6), round(lat,6) ] )

    lat1 = round( float(data[k]['lat'])/100., 6 )
    lon1 = round( float(data[k]['lon'])/100., 6 )
    print lon1, lat1
    cords.append( [ lon1, lat1 ] )

out = {}
out["type"] = "MultiPoint"
out["coordinates"] = cords
with open( 'data.geojson', 'w') as f:
    json.dump( out, f );
