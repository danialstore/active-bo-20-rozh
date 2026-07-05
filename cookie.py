import requests

cookies = {
    'tt_chain_token': 't5CdWci3MS5GlnDpiR4LfA==',
    'tiktok_webapp_theme_source': 'auto',
    'tiktok_webapp_theme': 'dark',
    'delay_guest_mode_vid': '5',
    'guest_mode_flag': '1',
    'tt_csrf_token': 'tGpQiFI0-Z9Yxl1hSqidrQGfnh792E4dyaCU',
    'ttwid': '1%7CTouaF3wBJAjDJW73xKFyfd86_IYnbHUS3euKRQGYIzY%7C1783210260%7C3cfc42131f7f050e931517dce0f2010a62e3710231b0f24b8b1e74a7db92e438',
    'msToken': '4C70lp57rWg_cA1pMiNHDv7K2ho5VCbNtcC1AYWZABYJZs7d1qQ_I_SwXYkhTrS9fTiTBoFBFNjRB3PJVR0vcgOkMWBCV42rM2Ldwzm313HBs4G3Oe_Jplf44GrcKkZbCHE7IUN57Xwh4AhGS3RkPmFDLp_qUQwV5EiSuzuN3Tg=',
    'msToken': '4C70lp57rWg_cA1pMiNHDv7K2ho5VCbNtcC1AYWZABYJZs7d1qQ_I_SwXYkhTrS9fTiTBoFBFNjRB3PJVR0vcgOkMWBCV42rM2Ldwzm313HBs4G3Oe_Jplf44GrcKkZbCHE7IUN57Xwh4AhGS3RkPmFDLp_qUQwV5EiSuzuN3Tg=',
    'g_state': '{"i_l":0,"i_ll":1783210267712,"i_b":"Id2VdY6kbGfmtoMuOWBUA4d2msF5ELkZxbDF7686tnc","i_e":{"enable_itp_optimization":24},"i_et":1783210267712}',
}

headers = {
    'authority': 'www.tiktok.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'tt_chain_token=t5CdWci3MS5GlnDpiR4LfA==; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; guest_mode_flag=1; tt_csrf_token=tGpQiFI0-Z9Yxl1hSqidrQGfnh792E4dyaCU; ttwid=1%7CTouaF3wBJAjDJW73xKFyfd86_IYnbHUS3euKRQGYIzY%7C1783210260%7C3cfc42131f7f050e931517dce0f2010a62e3710231b0f24b8b1e74a7db92e438; msToken=4C70lp57rWg_cA1pMiNHDv7K2ho5VCbNtcC1AYWZABYJZs7d1qQ_I_SwXYkhTrS9fTiTBoFBFNjRB3PJVR0vcgOkMWBCV42rM2Ldwzm313HBs4G3Oe_Jplf44GrcKkZbCHE7IUN57Xwh4AhGS3RkPmFDLp_qUQwV5EiSuzuN3Tg=; msToken=4C70lp57rWg_cA1pMiNHDv7K2ho5VCbNtcC1AYWZABYJZs7d1qQ_I_SwXYkhTrS9fTiTBoFBFNjRB3PJVR0vcgOkMWBCV42rM2Ldwzm313HBs4G3Oe_Jplf44GrcKkZbCHE7IUN57Xwh4AhGS3RkPmFDLp_qUQwV5EiSuzuN3Tg=; g_state={"i_l":0,"i_ll":1783210267712,"i_b":"Id2VdY6kbGfmtoMuOWBUA4d2msF5ELkZxbDF7686tnc","i_e":{"enable_itp_optimization":24},"i_et":1783210267712}',
    'referer': 'https://www.tiktok.com/ar/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.tiktok.com/node/report/reasons?WebIdLastTime=1783207203&aid=1988&api_version=3&app_language=ar&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv81&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&data_collection_enabled=true&device_id=7658816607170971144&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=3&is_fullscreen=false&is_page_visible=true&lang=ar&object_id=7641984471389981970&odinId=7658817749736702997&os=linux&priority_region=&referer=&region=IQ&report_type=video&screen_height=820&screen_width=360&tz_name=Asia%2FBaghdad&user_is_login=false&webcast_language=ar&msToken=4C70lp57rWg_cA1pMiNHDv7K2ho5VCbNtcC1AYWZABYJZs7d1qQ_I_SwXYkhTrS9fTiTBoFBFNjRB3PJVR0vcgOkMWBCV42rM2Ldwzm313HBs4G3Oe_Jplf44GrcKkZbCHE7IUN57Xwh4AhGS3RkPmFDLp_qUQwV5EiSuzuN3Tg=&X-Bogus=DFSzsIVu8yUANCWdClxbwSPR5im3&X-Gnarly=MPjY6EPVNL7sAa739Z6kGsj0aS43uOfNv6I7/haV7vY1qEJTOP2b1l1Pov9N1rwg1ov0O6dYOg1-w--nIcLLD6Q5AIixmFC/p66IL3yPiFeEyxnzigOMJBtRY8jnqt9QOzIzR1B627iYliwqAoAMH/3mqc54J4O9SAOjao7FO5mbqQK/9md03PFdvagythCpj88FkmqFkGbGXJTBcmGmcmKYJiX/F9v6rbiXI9/NB7jKRrwxP/NRIv08SIW/PMtLcT55XxQYv8jOFi5Q1NL/tGQOs7wBwBjU5MZbxbCrPLlFgZobiGvaIFmX9D67mn/CGIJd9EwDDn74',
    cookies=cookies,
    headers=headers,
)
