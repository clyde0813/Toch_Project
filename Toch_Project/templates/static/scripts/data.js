let positions = [];
{% if data %}
    {% for i in data %}
        positions.push({
            id: {{ i.id }},
            title: '{{ i.title }}',
            rent_type: '{{ i.rent_type }}',
            rent_amount: '{{ i.rent_amount }}',
            deposit: '{{ i.deposit }}',
            latlng: new kakao.maps.LatLng({{ i.latitude }}, {{ i.longitude }}), // 원룸 좌표
            main_img: '{{ i.file_set.first.file.url }}',
            floor_num: '{{ i.floor_num }}',
            common_area: '{{ i.common_area }}',
            address: '{{ i.address }}',
            manage_amount: '{{ i.manage_amount }}'
        })
    {% endfor %}
{% endif %}