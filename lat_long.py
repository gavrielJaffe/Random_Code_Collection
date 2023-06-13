import math

diflat = -0.00066286966871111111111111111111111111
diflon = -0.0003868060578  
c_sa = 6378137.000000
c_sb = 6356752.314245


def UTMtoWGS84(utmX, utmY, utmZone):
    def Check_valid_zone(utmZone):
        # implementation of Check_valid_zone function
        pass

    def Check_Valid_Bounds(utmX, utmY):
        # implementation of Check_Valid_Bounds function
        pass
    
    Check_valid_zone(utmZone)
    Check_Valid_Bounds(utmX, utmY)
    utmZone  ="1C"
    isNorthHemisphere = utmZone[-1] >= 'N'
    zone = 36  # int(utmZone[:-1])
    e2 = math.sqrt((math.pow(c_sa,2) - math.pow(c_sb,2))) / c_sb
    e2cuadrada = math.pow(e2,2)
    c = math.pow(c_sa,2) / c_sb
    x = utmX - 500000
    # y = utmY if isNorthHemisphere else utmY - 10000000 
    y = utmY - 10000000


    s = ((zone * 6.0) - 183.0)
    lat = y / (c_sa * 0.9996)
    v = (c / math.sqrt(1 + (e2cuadrada * math.pow(math.cos(lat), 2)))) * 0.9996
    a = x / v
    a1 = math.sin(2 * lat)
    a2 = a1 * math.pow((math.cos(lat)), 2)
    j2 = lat + (a1 / 2.0)
    j4 = ((3 * j2) + a2) / 4.0
    j6 = ((5 * j4) + math.pow(a2 * (math.cos(lat)), 2)) / 3.0
    alfa = (3.0 / 4.0) * e2cuadrada
    beta = (5.0 / 3.0) * math.pow(alfa, 2)
    gama = (35.0 / 27.0) * math.pow(alfa, 3)
    bm = 0.9996 * c * (lat - alfa * j2 + beta * j4 - gama * j6)
    b = (y - bm) / v
    epsi = ((e2cuadrada * math.pow(a, 2)) / 2.0) * math.pow((math.cos(lat)), 2)
    eps = a * (1 - (epsi / 3.0))
    nab = (b * (1 - epsi)) + lat
    senoheps = (math.exp(eps) - math.exp(-eps)) / 2.0
    delt  = math.atan(senoheps/(math.cos(nab)))
    tao = math.atan(math.cos(delt) * math.tan(nab))

    diflat = -0.00066286966871111111111111111111111111
    diflon = -0.0003868060578

    longitude = ((delt * (180.0 / math.pi)) + s) + diflon
    latitude = ((lat + (1 + e2cuadrada * math.pow(math.cos(lat), 2) - (3.0 / 2.0) * e2cuadrada * math.sin(lat) * math.cos(lat) * (tao - lat)) * (tao - lat)) * (180.0 / math.pi)) + diflat

    return (latitude, longitude)






def main():
    lat1 = 31.84773061844485
    lon1 = 34.68503878875027

    lat2 = 31.847699286584252
    lon2 = 34.685039459302516

    # latitude, longitude  = UTMtoWGS84(lon1, lat1)
    # latitude, longitude  = UTMtoWGS84(utmX, utmY, utmZone)
    latitude, longitude  = UTMtoWGS84(2.4096,2.4096, 31)
    print('latitude', latitude)
    print('longitude',longitude)
    
    
    # print('distance', distance)




if __name__ == '__main__':
    main()
