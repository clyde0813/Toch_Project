const info_area = document.querySelector('.infoArea');
const oneroom_detail_modal_container = document.querySelector('.oneroom_detail_modal_container');
const modal_close_btn = document.querySelector('.modal_close_btn');

const copy_modal = document.querySelector('.copy_modal');

info_area.addEventListener('click', e => {
    if (e.target.className === 'contact_btn') {
        oneroom_detail_modal_container.classList.remove('none');
    } else if (e.target.className === 'copy_contact_btn') {
        copyContact();
    } else if (e.target.className === 'oneroom_detail_share_btn') {
        console.log('공유');
    }
})

modal_close_btn.addEventListener('click', () => {
    oneroom_detail_modal_container.classList.add('none');
});

function copyContact() {
    const contact = document.querySelector('.modal_body').textContent;
    let textArea = document.createElement("textarea");
    document.body.appendChild(textArea);
    textArea.value = contact;
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    copy_modal.classList.add('copy_message');
    setTimeout(() => {
        copy_modal.classList.remove('copy_message');
    }, 1250);
}