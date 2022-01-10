// 마커 생성, 지도 위에 표시
function addMarker(info) {
    let content = document.createElement('div');
    content.classList.add('custom_overlay');
    content.textContent = (info.remain ? info.remain : '비공개');
    content.onclick = () => {
        if(!list_container.className.includes('showing')) {
            list_container.classList.add('showing');
            list_btn.classList.add('none');
            map_btn.classList.remove('none');
        }
        mobileRemoveAllRoom();
        mobileRenderRoom(info);
    }
    let marker = new kakao.maps.CustomOverlay({
        position: info.latlng,
        content: content
    });

    current_markers.push(marker);
    markers.push(marker)
    marker.setMap(map);
}

function addAllMarkers() {
    positions.map(room => addMarker(room));
}

function removeAllMarkers() {
    current_markers.map(marker => marker.setMap(null));
}