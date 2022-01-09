const kakao_map = document.querySelector('.kakao_map');

 // 지도 중심 좌표 설정
const MNU_LATITUDE = 34.91124654247272;
const MNU_LONGITUDE = 126.43614580709644;

const options = {
    center: new kakao.maps.LatLng(MNU_LATITUDE, MNU_LONGITUDE),
    level: 4 // 지도의 레벨(확대, 축소 정도)
};

let map = new kakao.maps.Map(kakao_map, options); //지도 생성 및 객체 리턴

console.log(map);