// 지도 컨테이너
const container = document.querySelector('.myMap');
const itemList = document.querySelector('.bottomArea > ul');

// 지도 중심 좌표 설정
const MNU_LATITUDE = 34.91124654247272;
const MNU_LONGITUDE = 126.43614580709644;

const options = {
    center: new kakao.maps.LatLng(MNU_LATITUDE, MNU_LONGITUDE),
    level: 5 // 지도의 레벨(확대, 축소 정도)
};

let map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴