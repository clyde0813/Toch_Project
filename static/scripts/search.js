const search_box = document.querySelector('.seachBox > input[type="search"]');
const search_btn = document.querySelector('.oneroom_search_btn');
let currentInput = '';

search_box.addEventListener('keyup', e => {
    if (e.code === 'Enter') {
        search_btn.click();
    }
})

search_btn.addEventListener('click', e => {
    let validInput = search_box.value.trim();
    // 입력 연타 방지
    if (currentInput === validInput && '' === validInput) {
        return;
    }
    searchRoom(validInput);
})

function searchRoom(validInput) {
    currentInput = validInput;
    const search_result = positions.filter(room => room.title.includes(currentInput));
    if (search_result.length === 0) {
        alert('검색 결과가 없습니다.');
        search_box.value = '';
        return;
    }
    removeAllRooms();
    removeAllMarkers();
    search_result.map(room => {
        renderRoom(room);
        addMarker(room);
    })
}
