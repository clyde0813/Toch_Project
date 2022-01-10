
// 마커 생성, 지도 위에 표시
function addMarker(info) {
    let content = document.createElement('div');
    content.classList.add('custom_overlay');
    content.setAttribute('id', info.id);
    content.textContent = (info.remain !== 'None' ? info.remain : '비공개');
    content.onclick = (e) => handleMarkerClick(e, info);

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

function handleMarkerClick(e, info) {
    if(e.target.id === single_list_flag) {
        console.log('같은거 클릭됫을때');
        single_list_container.classList.remove('showing');
        list_btn.classList.remove('none');
        map_btn.classList.remove('none');
        single_list_flag = '';
        return;
    }
    if(single_list_flag === '') {
        console.log('플래그가 비어있는 경우');
        single_list_container.classList.add('showing');
        list_btn.classList.add('none');
        map_btn.classList.add('none');
    }
    mobileRemoveAllRoom(single_list_container)
    mobileRenderRoom(info, single_list_container);
    single_list_flag = e.target.id;
}