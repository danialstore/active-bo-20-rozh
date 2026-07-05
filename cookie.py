import requests

cookies = {
    'tt_chain_token': 't5CdWci3MS5GlnDpiR4LfA==',
    'tiktok_webapp_theme_source': 'auto',
    'tiktok_webapp_theme': 'dark',
    'delay_guest_mode_vid': '5',
    'guest_mode_flag': '1',
    'tt_csrf_token': 'i9qIVqFR-VZNnwVYuqboCPtAhWKzPdS22b5Y',
    'ttwid': '1%7CTouaF3wBJAjDJW73xKFyfd86_IYnbHUS3euKRQGYIzY%7C1783211427%7Cd67d5bc4276d1094d19f4be51cd48d1e99ad56f6193c2a10f467169dfa1b5ee3',
    'g_state': '{"i_l":0,"i_ll":1783211433347,"i_b":"Id2VdY6kbGfmtoMuOWBUA4d2msF5ELkZxbDF7686tnc","i_e":{"enable_itp_optimization":24},"i_et":1783211433347}',
    'msToken': 'NuIKozj7ugTSOYgqB8PJuUZNB_zWO3-3Hqhatb6vzeDFdirxK6pcZhAaN4PD-lAb1T_3158sTtuEhzOV8Raz3JQ3LxvHoMZlMnNTkDY88MNTHyMc_ImbPQSbytzBQYPYJlTPpdRT0euIFwZtqwvTObOX8EWsfet3R7Mw98Ndv0g=',
    'odin_tt': '74ac170cbdf628d1543cded9cea3580ffe5ef4a8dce8f54383c11befdf68adb6829fb6a5e371d23dcb5090c3f7c325c80a3f93545a3f7f833c53bdcc64aeae056d662381d0d05797dac8005948533847',
    'msToken': 'Zl9hVOEI9XfENEIvy7l2e6lQAxOXo3VNxu2BdpZrorCyXVDwUmxUUTHlKGDAwquO165C7WWsTEIsUEReIwkDxcGgre56_mbyw8v5I5LnJGW1cpptulNR5RLa-7uJJC9bCN-6BUR07ssB_IR5wtLkBQKJj5eqpZrpi0hshLgv0Zo=',
}

headers = {
    'authority': 'www.tiktok.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'tt_chain_token=t5CdWci3MS5GlnDpiR4LfA==; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; guest_mode_flag=1; tt_csrf_token=i9qIVqFR-VZNnwVYuqboCPtAhWKzPdS22b5Y; ttwid=1%7CTouaF3wBJAjDJW73xKFyfd86_IYnbHUS3euKRQGYIzY%7C1783211427%7Cd67d5bc4276d1094d19f4be51cd48d1e99ad56f6193c2a10f467169dfa1b5ee3; g_state={"i_l":0,"i_ll":1783211433347,"i_b":"Id2VdY6kbGfmtoMuOWBUA4d2msF5ELkZxbDF7686tnc","i_e":{"enable_itp_optimization":24},"i_et":1783211433347}; msToken=NuIKozj7ugTSOYgqB8PJuUZNB_zWO3-3Hqhatb6vzeDFdirxK6pcZhAaN4PD-lAb1T_3158sTtuEhzOV8Raz3JQ3LxvHoMZlMnNTkDY88MNTHyMc_ImbPQSbytzBQYPYJlTPpdRT0euIFwZtqwvTObOX8EWsfet3R7Mw98Ndv0g=; odin_tt=74ac170cbdf628d1543cded9cea3580ffe5ef4a8dce8f54383c11befdf68adb6829fb6a5e371d23dcb5090c3f7c325c80a3f93545a3f7f833c53bdcc64aeae056d662381d0d05797dac8005948533847; msToken=Zl9hVOEI9XfENEIvy7l2e6lQAxOXo3VNxu2BdpZrorCyXVDwUmxUUTHlKGDAwquO165C7WWsTEIsUEReIwkDxcGgre56_mbyw8v5I5LnJGW1cpptulNR5RLa-7uJJC9bCN-6BUR07ssB_IR5wtLkBQKJj5eqpZrpi0hshLgv0Zo=',
    'referer': 'https://www.tiktok.com/@shakakkl_1/video/7658670359285091602',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.tiktok.com/aweme/v2/aweme/feedback/?WebIdLastTime=1783207203&aid=1988&app_language=ar&app_name=tiktok_web&aweme_type=0&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv81&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&current_region=IQ&data_collection_enabled=true&device_id=7658816607170971144&device_platform=web_pc&focus_state=true&from_page=video&history_len=5&is_fullscreen=false&is_osa_report=false&is_osa_report_cg=false&is_page_visible=true&is_sub_only_video=0&lang=ar&logout_reporter_email=&nickname=%D8%B4%D9%83%D8%A7%D9%83%D9%8A%20%F0%9F%8E%A7%F0%9F%94%A5&object_id=7658670359285091602&object_owner_id=7601307318659286023&odinId=7658817749736702997&os=linux&owner_id=7601307318659286023&play_mode=browser_mode&priority_region=&reason=9005&referer=&region=IQ&report_type=video&screen_height=820&screen_width=360&target=7658670359285091602&tz_name=Asia%2FBaghdad&user_is_login=false&video_id=7658670359285091602&video_owner=%5Bobject%20Object%5D&webcast_language=ar&msToken=Zl9hVOEI9XfENEIvy7l2e6lQAxOXo3VNxu2BdpZrorCyXVDwUmxUUTHlKGDAwquO165C7WWsTEIsUEReIwkDxcGgre56_mbyw8v5I5LnJGW1cpptulNR5RLa-7uJJC9bCN-6BUR07ssB_IR5wtLkBQKJj5eqpZrpi0hshLgv0Zo=&X-Bogus=DFSzsIVuA3UANCWdClxmvSPR5imm&X-Gnarly=MxPMjLHwO9KLatihGBbfvLq9NW0giUsF9a3WWvGzrIycdV5nugfmWbCalPaef/WxrUf2mEbJVKsz8T7KQCygdLU1/YsBWjafAZ2UbgCJFVPUMkPfw/YTmbgFKZAJ7lovjm726WuE7j2rv08qtvQIMbVkHz-j104OCCQDM29HtbKaZ9d1o3MZUS9tfNydnOlIe4KSYzXRnvz/N67B/xcssv6ahxGRrtv4koriJ/4d//c06XJHZMtjULloC2eUITIjSIDb2n9RFLP0QHM6A6/10zL8N4I4JbhIDXopXtWgi8to0qoFW27CSJUTf7emHLQzue8ARFYBk7T0',
    cookies=cookies,
    headers=headers,
)
