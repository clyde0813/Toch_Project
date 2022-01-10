let mobileKeyWords = new Array('iPhone', 'iPod', 'BlackBerry', 'Android', 'Windows CE', 'Windows CE;', 'LG', 'MOT', 'SAMSUNG', 'SonyEricsson', 'Mobile', 'Symbian', 'Opera Mobi', 'Opera Mini', 'IEmobile');
for (let word in mobileKeyWords) {
    if (!navigator) {
        alert("Your Browser doesn't support 'Navigator'");
    }
    if (navigator && navigator.userAgent.match(mobileKeyWords[word]) != null) {
        window.location.href = "https://m.toch.kr/oneroom";
        break;
    }
}
