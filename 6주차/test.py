from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image_path):
    """
    이미지 파일에서 exif 정보 추출
    """
    with Image.open(image_path) as image:
        exif_data = image._getexif()
        if exif_data:
            exif = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == 'GPSInfo':
                    gps_info = {}
                    for gps_tag_id in value:
                        gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                        gps_info[gps_tag] = value[gps_tag_id]
                    exif[tag] = gps_info
                else:
                    exif[tag] = value
            return exif

def get_decimal_from_dms(dms, ref):
    """
    GPS 정보에서 DMS(Degree, Minute, Second)를 decimal로 변환
    """
    d, m, s = dms
    decimal = float(d) + float(m)/60 + float(s)/3600
    if ref in ['S', 'W']:
        decimal *= -1
    return decimal

def get_coordinates(exif_data):
    """
    GPS 정보에서 위도와 경도 추출
    """
    if 'GPSInfo' in exif_data:
        gps_info = exif_data['GPSInfo']
        lat_dms = gps_info.get('GPSLatitude')
        lat_ref = gps_info.get('GPSLatitudeRef')
        lon_dms = gps_info.get('GPSLongitude')
        lon_ref = gps_info.get('GPSLongitudeRef')
        if lat_dms and lat_ref and lon_dms and lon_ref:
            lat = get_decimal_from_dms(lat_dms, lat_ref)
            lon = get_decimal_from_dms(lon_dms, lon_ref)
            return lat, lon
    return None

# 이미지 파일 경로 설정
image_path = "C:\\Users\\yang\\Documents\\test.jpg"

# exif 정보 추출
exif_data = get_exif_data(image_path)

# 위도와 경도 추출
coordinates = get_coordinates(exif_data)
if coordinates:
    print(f"위도: {coordinates[0]}, 경도: {coordinates[1]}")
else:
    print("GPS 정보를 찾을 수 없습니다.")
