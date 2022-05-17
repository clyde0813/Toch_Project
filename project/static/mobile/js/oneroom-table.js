const oneroom_table_btn = document.querySelector('.oneroom_table_btn');
const oneroom_table_container = document.querySelector('.oneroom_table_container');

oneroom_table_btn.addEventListener('click', () => {
    oneroom_table_container.classList.toggle('none');
})

