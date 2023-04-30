import hashlib
import struct
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import folium



class AutoForensic:
    def hash(self):
        m = hashlib.md5() 
        m.update(b"1 ") #저장매체(USB,HD,핸드폰)
        m.digest()
        print(m.hexdigest())
    pass

    def findHash(self):
        print("특정 폴더에서 일치하는 해시값을 찾는다")
        pass


    def to_little(self,val):
        little_hex = bytearray.fromhex(val)
        little_hex.reverse()

        str_little = ''.join(format(x, '02x') for x in little_hex)

        return str_little


    def calc(self,i):
        print(i[0:2])
        print(i[8:10])
        print(int(self.to_little(i[16:24]),16))
        #print(self.to_little(i[24:32],16))        

    def mbr(self):
        #(512=446+64+2)
        #00/202100/0C/80C47C/00080000/00C0DA00
        #012345678910111213141516171819202122232425262728293031
        pTable=[
            '002021000C80C47C0008000000C0DA00',
            '0080C57C07FEFFFF00C8DA000008F800'      
        ]
        print("mbr을 분석합니다.")
        print(pTable,type(pTable))
        for i in pTable:
            self.calc(i)
        '''
        for i in pTable:
            print(self.calc(i))
        #print(pTable)
        mbr_path='mbr.bin'
        with open(mbr_path,'rb') as f:
            print(f.read())
        '''
        pass

    def vbr(self):
        print("vbr을 분석합니다.")
        pass

    def carver(self):
        chk=1
        print("파일을 카빙합니다.")
        if chk:
            self.gps()
        else :
            pass

    def gps(self):
        image_path = 'example3.jpg'
        print("gps를 추출합니다.")
        exif_data = self.get_exif_data(image_path)
        # 위도와 경도 추출
        coordinates = self.get_coordinates(exif_data)
        if coordinates:
            print(f"위도: {coordinates[0]}, 경도: {coordinates[1]}")
            center = [coordinates[0], coordinates[1]]
            m = folium.Map(location=center, zoom_start=17, width=750, height=500)
            folium.Marker(center,popup="팝업 문구",tooltip="툴팁 문구",icon=folium.Icon(color='red', icon='star')).add_to(m)
            m.save('index.html')
            
        else:
            print("GPS 정보를 찾을 수 없습니다.")

        # 추출된 EXIF 데이터 출력
        if exif_data:
            for key, value in exif_data.items():
                print(f'{key}: {value}')
        else:
            print('이미지 파일에 EXIF 데이터가 없습니다.')
            print(exif_data)

    def get_exif_data(self,image_path):
        """이미지 파일에서 EXIF 데이터 추출"""
        with Image.open(image_path) as image:
            exif_data = image._getexif()
            if exif_data:
                exif = {}
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == 'GPSInfo':
                        print("GPS추출")
                        gps_info = {}
                        for gps_tag_id in value:
                            gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                            gps_info[gps_tag] = value[gps_tag_id]
                            exif[tag] = gps_info
                    else:
                        exif[tag] = value
        return exif

    def get_decimal_from_dms(self,dms, ref):
        """
        GPS 정보에서 DMS(Degree, Minute, Second)를 decimal로 변환
        """
        d, m, s = dms
        decimal = float(d) + float(m)/60 + float(s)/3600
        if ref in ['S', 'W']:
            decimal *= -1
        return decimal

    def get_coordinates(self,exif_data):
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
                lat = self.get_decimal_from_dms(lat_dms, lat_ref)
                lon = self.get_decimal_from_dms(lon_dms, lon_ref)
                return lat, lon
        return None



def main():
    print("start program")
    AF = AutoForensic()
    #AF.hash()
    #AF.findHash()
    AF.mbr()
    #AF.vbr()
    AF.carver()
    #AF.gps()
    #두개의 파일을 읽고 해시값 비교하는 프로그램
    
if __name__ == "__main__":
    main()
