const mobile_search_box = document.querySelector('.mobile_oneroom_search_box');
const mobile_search_btn = document.querySelector('.mobile_oneroom_search_btn');
let mobile_currentInput = '';

mobile_search_box.addEventListener('keyup', e => {
    if (e.code === 13) {
        mobile_search_btn.click();
    }
})

mobile_search_btn.addEventListener('click', e => {
    let validInput = mobile_search_box.value.trim();
    // 입력 연타 방지
    if (mobile_currentInput === validInput && '' === validInput) {
        return;
    }
    searchRoom(validInput);
})

function searchRoom(validInput) {
    mobile_currentInput = validInput;
    const search_result = positions.filter(room => room.title.includes(mobile_currentInput));
    if (search_result.length === 0) {
        alert('검색 결과가 없습니다.');
        mobile_search_box.value = '';
        return;
    }
    mobileRemoveAllRoom();
    removeAllMarkers();
    search_result.map(room => {
        mobileRenderRoom(room);
        addMarker(room);
    })
}
