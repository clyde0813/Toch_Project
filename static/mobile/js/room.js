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
              보증금 ${info.deposit !== "None" ? info.deposit : "비공개"} / 월세 ${info.rent_amount !== "None" ? info.rent_amount : "비공개"}
            </strong>
            <p>
              남은 방 : ${info.remain !== "None" ? info.remain : "비공개"} /
              면적 : ${info.dedicated_area !== "None" ? info.dedicated_area+"평" : "비공개"}
            </p>
            <p>${info.address}</p>
            <div>
              <span>${(info.hashtag1 !== "None" ? info.hashtag1 : "준비중")}</span>
              <span>${(info.hashtag2 !== "None" ? info.hashtag2 : "준비중")}</span>
              <span>${(info.hashtag3 !== "None" ? info.hashtag3 : "준비중")}</span>
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

