const container = document.querySelector('.myMap');
const itemList = document.querySelector('.itemList');

let MARKER_WIDTH = 33, // 기본, 클릭 마커의 너비
    MARKER_HEIGHT = 36, // 기본, 클릭 마커의 높이
    OFFSET_X = 12, // 기본, 클릭 마커의 기준 X좌표
    OFFSET_Y = MARKER_HEIGHT, // 기본, 클릭 마커의 기준 Y좌표
    OVER_MARKER_WIDTH = 40, // 오버 마커의 너비
    OVER_MARKER_HEIGHT = 42, // 오버 마커의 높이
    OVER_OFFSET_X = 13, // 오버 마커의 기준 X좌표
    OVER_OFFSET_Y = OVER_MARKER_HEIGHT, // 오버 마커의 기준 Y좌표
    SPRITE_MARKER_URL = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markers_sprites2.png', // 스프라이트 마커 이미지 URL
    SPRITE_WIDTH = 126, // 스프라이트 이미지 너비
    SPRITE_HEIGHT = 146, // 스프라이트 이미지 높이
    SPRITE_GAP = 10; // 스프라이트 이미지에서 마커간 간격

let markerSize = new kakao.maps.Size(MARKER_WIDTH, MARKER_HEIGHT), // 기본, 클릭 마커의 크기
    markerOffset = new kakao.maps.Point(OFFSET_X, OFFSET_Y), // 기본, 클릭 마커의 기준좌표
    overMarkerSize = new kakao.maps.Size(OVER_MARKER_WIDTH, OVER_MARKER_HEIGHT), // 오버 마커의 크기
    overMarkerOffset = new kakao.maps.Point(OVER_OFFSET_X, OVER_OFFSET_Y), // 오버 마커의 기준 좌표
    spriteImageSize = new kakao.maps.Size(SPRITE_WIDTH, SPRITE_HEIGHT); // 스프라이트 이미지의 크기

// 클릭된 마커를 담을 변수
let selectedMarker = null;

// 마커를 표시할 위치와 해당 정보를 담은 객체 배열
let positions = [
    { %
if data_list %}
{%
    for data in data_list %}
{
    title: '{{ data.title }}',
        // price: '월세 200/35',
        // type: '원룸',
        // space: '7평',
        latlng
:
    new kakao.maps.LatLng(34.91124654247272, 126.43614580709644), // 원룸 좌표

}
,
]
;

const options = {
    center: new kakao.maps.LatLng(34.91124654247272, 126.43614580709644), // 지도의 중심 좌표
    level: 3 // 지도의 레벨(확대, 축소 정도)
};

const map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴

for (let i = 0, len = positions.length; i < len; i++) {
    let gapX = (MARKER_WIDTH + SPRITE_GAP), // 스프라이트 이미지에서 마커로 사용할 이미지 X좌표 간격 값
        originY = (MARKER_HEIGHT + SPRITE_GAP) * i, // 스프라이트 이미지에서 기본, 클릭 마커로 사용할 Y좌표 값
        overOriginY = (OVER_MARKER_HEIGHT + SPRITE_GAP) * i, // 스프라이트 이미지에서 오버 마커로 사용할 Y좌표 값
        normalOrigin = new kakao.maps.Point(0, originY), // 스프라이트 이미지에서 기본 마커로 사용할 영역의 좌상단 좌표
        clickOrigin = new kakao.maps.Point(gapX, originY), // 스프라이트 이미지에서 마우스오버 마커로 사용할 영역의 좌상단 좌표
        overOrigin = new kakao.maps.Point(gapX * 2, overOriginY); // 스프라이트 이미지에서 클릭 마커로 사용할 영역의 좌상단 좌표

    let info = {
        title: positions[i].title,
        price: positions[i].price,
        type: positions[i].type,
        space: positions[i].space
    }

    // 마커를 생성하고 지도위에 표시합니다
    addMarker(positions[i].latlng, normalOrigin, overOrigin, clickOrigin, info);

    // 아이템 모두 표시
    showAllItems(info);
}

// 마커를 생성하고 지도 위에 표시하고, 마커에 mouseover, mouseout, click 이벤트를 등록하는 함수입니다
function addMarker(position, normalOrigin, overOrigin, clickOrigin, info) {

    // 기본 마커이미지, 오버 마커이미지, 클릭 마커이미지를 생성합니다
    var normalImage = createMarkerImage(markerSize, markerOffset, normalOrigin),
        overImage = createMarkerImage(overMarkerSize, overMarkerOffset, overOrigin),
        clickImage = createMarkerImage(markerSize, markerOffset, clickOrigin);

    // 마커를 생성하고 이미지는 기본 마커 이미지를 사용합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: position,
        image: normalImage,
    });

    // 마커 객체에 마커아이디와 마커의 기본 이미지를 추가합니다
    marker.normalImage = normalImage;

    // 마커에 click 이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function () {
        // 클릭된 마커가 없고, click 마커가 클릭된 마커가 아니면
        // 마커의 이미지를 클릭 이미지로 변경합니다
        if (!selectedMarker || selectedMarker !== marker) {
            setListItem(info);
        }

        // 클릭된 마커를 현재 클릭된 마커 객체로 설정합니다
        selectedMarker = marker;
    });
}

function setListItem(info) {
    // 기존 item 들을 삭제합니다.
    while (itemList.firstChild) {
        itemList.removeChild(itemList.firstChild);
    }

    const roomInfo =
        `
        <a href="#">
            <li>
                <div style="margin-right:30px"><img width="80px" height="80ox" src="https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markers_sprites2.png" alt="This is a preview image of the room."></div>
                <div>
                    <p>
                        <h3>${info.price}</h3>
                        <span>${info.type}</span>
                        <span>${info.space}</span>
                    </p>
                </div>
            </li>
        </a>
    `
    itemList.innerHTML = roomInfo;
}

// MakrerImage 객체를 생성하여 반환하는 함수입니다
function createMarkerImage(markerSize, offset, spriteOrigin) {
    let markerImage = new kakao.maps.MarkerImage(
        SPRITE_MARKER_URL, // 스프라이트 마커 이미지 URL
        markerSize, // 마커의 크기
        {
            offset: offset, // 마커 이미지에서의 기준 좌표
            spriteOrigin: spriteOrigin, // 스트라이프 이미지 중 사용할 영역의 좌상단 좌표
            spriteSize: spriteImageSize // 스프라이트 이미지의 크기
        }
    );

    return markerImage;
}

// 아이템 전부 표시
function showAllItems(info) {
    // 기존 item 들을 삭제합니다.
    const item = document.createElement('li');
    itemList.appendChild(item);

    const roomInfo =
        `
        <a href="#">
            <li>
                <div style="margin-right:30px"><img width="80px" height="80ox" src="https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markers_sprites2.png" alt="This is a preview image of the room."></div>
                <div>
                    <p>
                        <h3>${info.price}</h3>
                        <span>${info.type}</span>
                        <span>${info.space}</span>
                    </p>
                </div>
            </li>
        </a>
    `
    item.innerHTML = roomInfo;
}


