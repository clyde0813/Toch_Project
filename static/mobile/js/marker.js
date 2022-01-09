// 마커 생성, 지도 위에 표시
function addMarker(info) {
    let content = document.createElement('div');
    content.classList.add('custom_overlay');
    content.textContent = 10;
    content.onclick = () => {
        console.log('CLICKED');
    }

    // 커스텀 오버레이를 생성합니다
    let marker = new kakao.maps.CustomOverlay({
        position: info.latlng,
        content: content
    });

    current_markers.push(marker);
    markers.push(marker)
    // 마커가 지도 위에 표시되도록 설정합니다.
    marker.setMap(map);
}

function removeAllMarkers() {
    current_markers.map(marker => marker.setMap(null));
}