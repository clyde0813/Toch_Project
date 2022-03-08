insert into Toch.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
values  (1, 'pbkdf2_sha256$260000$ocPkMdmbapeR3l7tkIbNWC$FCNemuyYarG3yXgEN08//ske8EgF93nxffg+5Gu1Wyc=', '2021-12-13 06:38:49.827623', 1, '테스트하는 개굴이', '', '', 'admin@admin.com', 1, 1, '2021-09-23 08:46:27.080835'),
        (2, 'pbkdf2_sha256$260000$OhehWnRMCIZemc2z4Oe3Sr$3jPnhWODvYSabOe8qPGy+3fqHCvWTPXKFDrPCJrBmto=', '2021-12-22 07:15:13.290406', 1, '테스트하는 호랑이', '', '박정현', '', 1, 1, '2021-11-20 12:34:28.914422'),
        (3, 'pbkdf2_sha256$260000$8xIpBnANXGirrG9p8FnkBu$WkhOnW8nWaMzM4qItBfXPuy+udgi+Qu/VgN+C01UQwA=', null, 1, '테스트하는 토끼', '', '', '', 1, 1, '2021-11-20 12:34:40.509194'),
        (6, 'pbkdf2_sha256$260000$PBFhqMPQgqwoYnDgw0BFK1$3PDIdqg/nGPvw2daxEjXZvY0jeYasmWNkyHQVKW2SW4=', '2021-11-24 01:21:36.259202', 0, '테스트하는 멍뭉이
', '', '박정현', 'test1234@gmail.com', 0, 1, '2021-11-21 10:47:28.073109'),
        (7, 'pbkdf2_sha256$260000$mOKGByIYgfjxKeVF4CZpe6$ToN6PR29r6x+j75k6MQ8MnNsTeJZXTOpjVcfGq859AY=', '2021-11-30 00:35:24.578134', 0, '테스트하는 고양이
', '', '토치', 'kakao@mokpo.ac.kr', 0, 1, '2021-11-23 19:26:41.821753'),
        (8, 'pbkdf2_sha256$260000$abuszMqBCoHUfOryV838cR$zeFYBOd1AxKWUBzCZUeqW0G7277C6QYIzPtgXXKt5Oc=', '2022-01-06 11:37:18.924470', 0, 'truth2357', '', '윤영숙', 'truth2357@naver.com', 0, 1, '2022-01-06 11:36:53.434689');