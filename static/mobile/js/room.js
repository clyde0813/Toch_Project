function mobileRenderRoom(info, ul=oneroom_list_ul) {
  const roomInfo = mobileRoomTemplate(info);
  ul.insertAdjacentHTML('beforeend', roomInfo);
}

function mobileRenderAllRoom() {
  mobileRemoveAllRoom();
  positions.map(room => mobileRenderRoom(room));
}

function mobileRoomTemplate(info) {
  return (
    `
      <li class="oneRoomList">
        <a href="#">
          <div
            class="imgBox"
            style="background-image: url(${info.main_img})"
          >
            월세 이미지
          </div>
          <div class="textArea">
            <strong>
              <small> ${info.title} </small>
              보증금 ${info.deposit}만원 / 월세 ${info.rent_amount}만원
            </strong>
            <p>
              남은 방 : ${info.remain}
              면적 : ${(info.dedicated_area ? info.dedicated_area : '준비중')}평
            </p>
            <p>${info.address}</p>
            <div>
              <span>${(info.hashtag1 ? info.hashtag1 : '준비중')}</span>
              <span>${(info.hashtag2 ? info.hashtag2 : '준비중')}</span>
              <span>${(info.hashtag3 ? info.hashtag3 : '준비중')}</span>
            </div>
          </div>
        </a>
      </li>
    `
    );
}

function mobileRemoveAllRoom(ul=oneroom_list_ul) {
  while(ul.firstChild) {
    ul.removeChild(ul.firstChild);
  }
}

