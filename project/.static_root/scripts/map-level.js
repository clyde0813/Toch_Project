// 지도가 확대 또는 축소되면 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
function handleMapLevel(map) {
    kakao.maps.event.addListener(map, 'zoom_changed', function () {
        // 지도의 현재 레벨을 얻어옵니다
        var level = map.getLevel();

        var message = '현재 지도 레벨은 ' + level + ' 입니다';
        var resultDiv = document.getElementById('result');
    });
}
