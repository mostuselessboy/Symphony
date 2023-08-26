from flask import Flask, render_template, request, redirect, url_for, session,make_response,after_this_request
import firebase_admin
from werkzeug.utils import secure_filename
from firebase_admin import credentials, auth, firestore,storage

import requests 
import random
import os
from pytube import YouTube
import threading
from ytmusicapi import YTMusic
ytmusic = YTMusic()
import base64
import random
from DataSetCreator import get_quiz_data
def set_headers(response):
    return response


app = Flask(__name__, template_folder='site', static_folder='assets')
cred = credentials.Certificate("serviceaccountkey.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'musick-2945d.appspot.com'})
app.secret_key = 'mostuselessboyismostusefulboy' 
db = firestore.client()
bucket = storage.bucket()

@app.route('/home')
def home_page():
    dark_mode = request.args.get('darkmode')
    if dark_mode == 'true':
        print("YES DARK MODE😭😋😋")
    artists = [{'name': 'Taylor Swift', 'id': 'UCPC0L1d253x-KuMNwa05TpA', 'img': 'https://lh3.googleusercontent.com/U1cI80giSCUuNYx3zkRPt_AWytN1qFMlQoL5F7kTZeFzfIMmfHJYLJchX3BxeDLglE9MeVYp4OlN5Xc=w2880-h1200-p-l90-rj'}, {'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw', 'img': 'https://lh3.googleusercontent.com/x_OLwEjNh74QScfVbc3ejrbxjjG3WFe5CfVrO9KlIT_W2VvHpVC-orFzg-LF2kVYsBGK2YOA5JvUsVE=w2880-h1200-p-l90-rj', 'bio': 'ZAYN is a multi-platinum selling recording artist, producer, and philanthropist known for his skyscraping vocals and hybrid style of pop and R&B. He became the first UK Male Solo artist to simultaneously chart at #1 on the UK and US album charts in the first week of release for his record-breaking debut album Mind of Mine (2016). The album’s lead single, “Pillowtalk,” hit #1 in 68 countries around the world and has since been certified 5x platinum by the RIAA. The album was followed by his gold certified Icarus Falls (2018), and critically acclaimed Nobody is Listening (2021). \n \nThe UK native’s influence spans beyond just music into the fashion world, where ZAYN has collaborated on capsule collections with the likes of Giuseppe Zanotti and Versus Versace, and covered numerous fashion publications including Vogue, GQ, ELLE UK, Highsnobiety, PAPER, The FADER and more. ZAYN has garnered several accolades throughout his career including a Billboard Music Award, American Music Award, MTV VMA, two Brit Award nominations, and was named “Most Stylish Man” at the British GQ Men of the Year Awards.\n \nIn addition to his music ZAYN continues to be a voice for positive change most recently advocating for free school lunches for children living in poverty in the UK.\n \nZAYN is currently working on his highly anticipated fourth studio album.'}, {'name': 'Justin Bieber', 'id': 'UCGvj8kfUV5Q6lzECIrGY19g', 'img': 'https://lh3.googleusercontent.com/iVttpMqOcjor_Rt64WqL0iB8YJ3At97IGNer6qzhYQ7ffoqzVL7pEmxJXmItcZ2Sj_aRT_dewAg1ORg=w2880-h1200-p-l90-rj'}, {'name': 'Katy Perry', 'id': 'UC_7s69e1mDS3lgcTMJEPjCg', 'img': 'https://lh3.googleusercontent.com/eMgihOYKQahtK-vzW1QVALPM7LolBy7yC5NshcOgSwjXotdudRavwmwiSAZmtLfGrvKu2Y3JvGCseXA=w2880-h1200-p-l90-rj'}, {'name': 'Ariana Grande', 'id': 'UC0076UMUgEng8HORUw_MYHA', 'img': 'https://lh3.googleusercontent.com/DU6Kpr5TYKcW6QHvMnsJau5_8QSuix8LCLtf5UEaziZZdXw8SxvcxJ9YWmVIQuzhg2R-MVHYgjdGCQ=w2880-h1200-p-l90-rj'}, {'name': 'Maroon 5', 'id': 'UCdFe4KkWwZ_twpo-UECR-Nw', 'img': 'https://lh3.googleusercontent.com/7jndWy5UJwFJKueBCrizeFWOFwxKUOZZjRMIcPyRlv1X18tY9aJpkuSz_PpamnHVjbYV6s_oER8oi4g=w2880-h1200-p-l90-rj'}, {'name': 'Beyoncé', 'id': 'UCoPQ_TWm8JZ5nJv4a5BzSWA', 'img': 'https://lh3.googleusercontent.com/GAR8Y4xuTIBIrOr0GPSPdhPc-aRvUCOXwiC0O75cKSP7uRoHFvb20K2ZwpaZwxp2IcSoXGBiAgjit-BC=w2880-h1200-p-l90-rj'}, {'name': 'The Weeknd', 'id': 'UClYV6hHlupm_S_ObS1W-DYw', 'img': 'https://lh3.googleusercontent.com/U-SAmNOu4TynE818gLCfKsuHZ0U5YNEtO9mrjSI9WCCKERs98LzrCal5kajBBTQNwdcisoB2Bn-pHp4=w2880-h1200-p-l90-rj'}, {'name': 'Dolly Parton', 'id': 'UCXJscayh5BT8m2ZVFQSdeVw', 'img': 'https://lh3.googleusercontent.com/ZvZFUBod49phwJaA1BDBZZwTNW17-ZQGJRc1TecLbfM41FNhtC6UGFeEDuyxYHrvHJtIj5npLe3R4QRx=w2880-h1200-p-l90-rj'},  {'name': 'Florence + the Machine', 'id': 'UCkmCGbrGa7yNrRl_NHrOaTw', 'img': 'https://lh3.googleusercontent.com/Mrc6nBGklCHoToVgoBkPELexyPylNAVhhyiKFYTOr3DMLpr7BN3Wu4VEmfBnSSnpTgfOk0Lc-RYeUfQ=w2880-h1200-p-l90-rj'}, {'name': 'Drake', 'id': 'UCU6cE7pdJPc6DU2jSrKEsdQ', 'img': 'https://lh3.googleusercontent.com/MxNjcRJ-uK4Xvx7u90IhEFLQM8x9LIGTA9VCKHq5U4Wn2jOgiWaMtg-qz329SIzqnCyhdCCB3MpdAGs=w2880-h1200-p-l90-rj'}, {'name': 'Nicki Minaj', 'id': 'UCTTcTeAszDGxALRSMkJH9FQ', 'img': 'https://lh3.googleusercontent.com/dxazpVxrrUIWVdh49h3-GBhkgI5Wl2ALR5lI1AEldaVbUtz5TN4HfmL_ssUddy2ctEKcSPzNGeFOl-c=w2880-h1200-p-l90-rj'}, {'name': 'Cardi B', 'id': 'UCoIp9Cj1l7k63B90hFg38Zw', 'img': 'https://lh3.googleusercontent.com/EI0DGHwUprlB2Xc4XL0oKDgG_Dv2ejS5F8GaVIDV8w3Zehz14TGLqoTQwP7Am2buVJVJo9oJ1o8Szw=w2880-h1200-p-l90-rj'}]
    DATA_genres ={'Pop': [{'name': 'Adele', 'id': 'UCRw0x9_EfawqmgDI2IgQLLg', 'img': 'https://lh3.googleusercontent.com/mFjMekiL9JJDrJOSTpAvu264z4DDmYS6pdy51ZCLr98kA256rvxSrIIuNv12kMj8RJW2vtTq1ECDhA=w2880-h1200-p-l90-rj'}, {'name': 'Ed Sheeran', 'id': 'UClmXPfaYhXOYsNn_QUyheWQ', 'img': 'https://lh3.googleusercontent.com/jQoBIAS6JjFGpcqQY1M_Mh3AasOvFENCdVRxkgax1a0K6qiq7AgE3MbJ6Jtt-Jndcarvoawmrg66KTny=w2880-h1200-p-l90-rj'}, {'name': 'Justin Bieber', 'id': 'UCGvj8kfUV5Q6lzECIrGY19g', 'img': 'https://lh3.googleusercontent.com/iVttpMqOcjor_Rt64WqL0iB8YJ3At97IGNer6qzhYQ7ffoqzVL7pEmxJXmItcZ2Sj_aRT_dewAg1ORg=w2880-h1200-p-l90-rj'}, {'name': 'Katy Perry', 'id': 'UC_7s69e1mDS3lgcTMJEPjCg', 'img': 'https://lh3.googleusercontent.com/eMgihOYKQahtK-vzW1QVALPM7LolBy7yC5NshcOgSwjXotdudRavwmwiSAZmtLfGrvKu2Y3JvGCseXA=w2880-h1200-p-l90-rj'}, {'name': 'Rihanna', 'id': 'UCvWtix2TtWGe9kffqnwdaMw', 'img': 'https://lh3.googleusercontent.com/6EZ6nHUoi96zJ9ijYyDrBfSZ_1pY64QQqJUqyWKA-Uy9Gzoio7gFTReBruJJRCjjuQQyHES7pIQchTkT=w2880-h1200-p-l90-rj'}, {'name': 'Bruno Mars', 'id': 'UCZn4r7heNOPY-C43YIywnVA', 'img': 'https://lh3.googleusercontent.com/u5G4lXyNl69C1M298f2yMu610s5oSW98TAAVkze5Gek8B5qMDeJ2dFko0x3cXOaoJVA1339aOaOq3uTM=w2880-h1200-p-l90-rj'}, {'name': 'Ariana Grande', 'id': 'UC0076UMUgEng8HORUw_MYHA', 'img': 'https://lh3.googleusercontent.com/DU6Kpr5TYKcW6QHvMnsJau5_8QSuix8LCLtf5UEaziZZdXw8SxvcxJ9YWmVIQuzhg2R-MVHYgjdGCQ=w2880-h1200-p-l90-rj'}, {'name': 'Maroon 5', 'id': 'UCdFe4KkWwZ_twpo-UECR-Nw', 'img': 'https://lh3.googleusercontent.com/7jndWy5UJwFJKueBCrizeFWOFwxKUOZZjRMIcPyRlv1X18tY9aJpkuSz_PpamnHVjbYV6s_oER8oi4g=w2880-h1200-p-l90-rj'}, {'name': 'Shawn Mendes', 'id': 'UC6ZjlLJhqP79nqGr3Ic6Adg', 'img': 'https://lh3.googleusercontent.com/4EsDMeFPd5Ms9hW7MCYaJ1172CO08yEEJ8clrkpjdSUuZDR6fljAjLfQVo7Ut-j32bQqmCrZJpSmulM=w2880-h1200-p-l90-rj'}], 'Rock': [{'name': 'The Beatles', 'id': 'UC2XdaAVUannpujzv32jcouQ', 'img': 'https://lh3.googleusercontent.com/z8KZsHNKS-O1qYVyKlSErT_RLMSMwVht89USvSdFAd0EoRlBOppi9DOdRkv609Ye_tfq_Wp8WwhVJbw=w2880-h1200-p-l90-rj'}, {'name': 'Queen', 'id': 'UCEPMVbUzImPl4p8k4LkGevA', 'img': 'https://lh3.googleusercontent.com/_Qx50zW4-diO8SuAKhaccaNLyTvObgE-TQv1jYS4M9Kma6llb3s-IHpBBvuZAkPh88lHvXTQGaWS7aE=w2880-h1200-p-l90-rj'}, {'name': 'Led Zeppelin', 'id': 'UCYtap7ujIPaxTS2iCDoMi3g', 'img': 'https://lh3.googleusercontent.com/MYtL09ZzsVQy2gBcWceZ04StzvKmNxJ6jfrzT8KrtwXFcwEXanVOzCGUWztuLg4A1zmWQYUu04vvOSw=w2880-h1200-p-l90-rj'}, {'name': 'The Rolling Stones', 'id': 'UCNYhhkQqeFLUc-YEDcLpSYQ', 'img': 'https://lh3.googleusercontent.com/VayRnJfZC6MAdZZEkGa_O8Zegu9qoyhlwcYA73fFqRAr5C8no_DLdMqGY3LXtdDQFX91V4GMWrtnjmk=w2880-h1200-p-l90-rj'}, {'name': 'Coldplay', 'id': 'UCIaFw5VBEK8qaW6nRpx_qnw', 'img': 'https://lh3.googleusercontent.com/IOKuXtp8PCQ_Fc-vaRKm3sKIXBxFV51gZheLTH5br-YGnWHFQf_Jywcuk7wbprYRoEbQyS_XZY6-nMJX=w2880-h1200-p-l90-rj'}, {'name': 'U2', 'id': 'UCqIQRxCUGi7hyJisyzv9zYQ', 'img': 'https://lh3.googleusercontent.com/AkQ_0Er0h2xS90d0_CrEoFfiW7AjaSoTAJ6SdAJmFdzaKRJh4jywzPWi6cAewGrpP2AywIGGfXUWkBo=w2880-h1200-p-l90-rj'}, {'name': 'Nirvana', 'id': 'UCrPe3hLA51968GwxHSZ1llw', 'img': 'https://lh3.googleusercontent.com/yoFwkvvbmM3u7q0VM_HpjCnsaViQx3gWuycm5OsdmRqWBHL4LyIpNQ5kemdcoW7zrGETTutR_5c_xk8=w2880-h1200-p-l90-rj'}, {'name': 'Pink Floyd', 'id': 'UCO6LS_5W7vqG9mALDNzSFug', 'img': 'https://lh3.googleusercontent.com/I3NonRbCqhwhHAoWaTtXmUNtTUKALOUM3fRYYucCzhtA3VAkPov5k_EKNtS44n2ExEXSPKJf32xgJQ=w2880-h1200-p-l90-rj'}, {'name': 'AC/DC', 'id': 'UCVm4YdI3hobkwsHTTOMVJKg', 'img': 'https://lh3.googleusercontent.com/IlNp_o9GKakp7qtaDAKaDxpW29qtP8sjqQXPcBQ9uAdOUU3AnJdB85xLRiYIGT3FlCmobm6oiMQX4GU=w2880-h1200-p-l90-rj'}, {'name': 'Radiohead', 'id': 'UCr_iyUANcn9OX_yy9piYoLw', 'img': 'https://lh3.googleusercontent.com/o_9BDAQZy2-R-BzR-MO91rvly39MRjxV_qUbdzYdvyOPu9V2CPix9nRXroTMvy4f99zdLhKePFHQEYA=w2880-h1200-p-l90-rj'}], 'Hip-Hop': [{'name': 'Eminem', 'id': 'UCedvOgsKFzcK3hA5taf3KoQ', 'img': 'https://lh3.googleusercontent.com/P-rYd_7rYsYjsHg9LwlI-66FpHn3dCSSuoFof_cCf08LWFEfZe4h94-pKnEXvut926ouTf6QU6849Q=w2880-h1200-p-l90-rj'}, {'name': 'Kendrick Lamar', 'id': 'UCprAFmT0C6O4X0ToEXpeFTQ', 'img': 'https://lh3.googleusercontent.com/hMjzHmIuTV0XPlvRSjl3wMR6NP-uF-fqF6kkandkFX-hEVp6d3tw-FQG9_smAq0tFwNBT6QLQR-Hkwge=w2880-h1200-p-l90-rj'}, {'name': 'Drake', 'id': 'UCU6cE7pdJPc6DU2jSrKEsdQ', 'img': 'https://lh3.googleusercontent.com/MxNjcRJ-uK4Xvx7u90IhEFLQM8x9LIGTA9VCKHq5U4Wn2jOgiWaMtg-qz329SIzqnCyhdCCB3MpdAGs=w2880-h1200-p-l90-rj'}, {'name': 'JAY Z', 'id': 'UCbJG1HvzgzaMe_15xfiUyWw', 'img': 'https://lh3.googleusercontent.com/YcGJemFC30LtMjWCOMXUgjHhVknIUlxtgh6yBkEl1NA8ZHhih7VE4UrFqFqvwGPraXBr_EDvfbQ0ZkVi=w2880-h1200-p-l90-rj'}, {'name': 'Kanye West', 'id': 'UCRY5dYsbIN5TylSbd7gVnZg', 'img': 'https://lh3.googleusercontent.com/IFlc3sf6sHV3TAZ_5vhyHQiKb9D4AdSlDkiTSgsRiicnzLASXwVr1n22EEg6Vtd2XBlyJslm8xlYiA=w2880-h1200-p-l90-rj'}, {'name': 'Nicki Minaj', 'id': 'UCTTcTeAszDGxALRSMkJH9FQ', 'img': 'https://lh3.googleusercontent.com/dxazpVxrrUIWVdh49h3-GBhkgI5Wl2ALR5lI1AEldaVbUtz5TN4HfmL_ssUddy2ctEKcSPzNGeFOl-c=w2880-h1200-p-l90-rj'}, {'name': 'Cardi B', 'id': 'UCoIp9Cj1l7k63B90hFg38Zw', 'img': 'https://lh3.googleusercontent.com/EI0DGHwUprlB2Xc4XL0oKDgG_Dv2ejS5F8GaVIDV8w3Zehz14TGLqoTQwP7Am2buVJVJo9oJ1o8Szw=w2880-h1200-p-l90-rj'}, {'name': 'Lil Wayne', 'id': 'UC4IAZ3dowcXyvVYBx4hucSQ', 'img': 'https://lh3.googleusercontent.com/tpZlhvzqH9HPsXKBygEOKEWfw-KkU5zltB0kBazorZvUg_fvviQvcb3IG8DJfAW8tEVoqYu-8FhAQW0=w2880-h1200-p-l90-rj'}, {'name': 'Snoop Dogg', 'id': 'UC7xz_YipuZtypOuVALNzeog', 'img': 'https://lh3.googleusercontent.com/eWz33ayRvinYr30kQSi3aKeRedhY3_6-dNnOWUMNkaFlpB5DnljCB9fuPLjmN4_4dnhxyfLaw9HR7Mk=w2880-h1200-p-l90-rj'}, {'name': 'Travis Scott', 'id': 'UCf_gP4AMRSgAfyzbkeS9k4g', 'img': 'https://lh3.googleusercontent.com/r9k_FpAswxhQnl_cudiaT2ocWFccR6SzEFXgZ9a12iR5eDPSILlIL2EQewyQ-yYSt1JFyH1pqnoBXxs=w2880-h1200-p-l90-rj'}], 'R&B (Rhythm and Blues)': [{'name': 'Beyoncé', 'id': 'UCoPQ_TWm8JZ5nJv4a5BzSWA', 'img': 'https://lh3.googleusercontent.com/GAR8Y4xuTIBIrOr0GPSPdhPc-aRvUCOXwiC0O75cKSP7uRoHFvb20K2ZwpaZwxp2IcSoXGBiAgjit-BC=w2880-h1200-p-l90-rj'}, {'name': 'Rihanna', 'id': 'UCvWtix2TtWGe9kffqnwdaMw', 'img': 'https://lh3.googleusercontent.com/6EZ6nHUoi96zJ9ijYyDrBfSZ_1pY64QQqJUqyWKA-Uy9Gzoio7gFTReBruJJRCjjuQQyHES7pIQchTkT=w2880-h1200-p-l90-rj'}, {'name': 'Chris Brown', 'id': 'UCMXDyVR2tclKWhbqNforSyA', 'img': 'https://lh3.googleusercontent.com/BWoZ2a1rLr0GwAQOMDv_wSiAVOIfojPVy1dk6g_5slxviqSFL5YZ-oiuk5lqDmxzZUGmCCusH5gNGgY=w2880-h1200-p-l90-rj'}, {'name': 'Usher', 'id': 'UCILuIcqzJMtkxCmftNVjNBQ', 'img': 'https://lh3.googleusercontent.com/mWYMY57GRNGro1dGyxfyxwB19HWzqI4LEdaiFRL_RHVcTdnl4Gj840UD-B-_JqE5BVBI54xiPdNBGw=w2880-h1200-p-l90-rj'}, {'name': 'Alicia Keys', 'id': 'UCvaP3izVIy3fieneHVV6Drw', 'img': 'https://lh3.googleusercontent.com/SK-iFcersg-ptS5IKuvoslOLOIVBFyUrkQsw9rZiBe01tD6_jP6dXNmUVJckdJwk1jidZz2QEd_YWGD9=w2880-h1200-p-l90-rj'}, {'name': 'Mariah Carey', 'id': 'UCKRnq8aBOCanYlffje7HyvA', 'img': 'https://lh3.googleusercontent.com/zQwYb_8FK0DndP_rrm-y9GW133AYS7shlNgLCsH6gwu8cp6iRhScqviVAE9LO6Qg74WvaLnDKTkiRlM=w2880-h1200-p-l90-rj'}, {'name': 'The Weeknd', 'id': 'UClYV6hHlupm_S_ObS1W-DYw', 'img': 'https://lh3.googleusercontent.com/U-SAmNOu4TynE818gLCfKsuHZ0U5YNEtO9mrjSI9WCCKERs98LzrCal5kajBBTQNwdcisoB2Bn-pHp4=w2880-h1200-p-l90-rj'}, {'name': 'R. Kelly', 'id': 'UCNRcoQxfabvUAULNbIy7qPg', 'img': 'https://lh3.googleusercontent.com/w3tItUtf6Out8tULlStsZgxsBw1rJFpozutybicpQYquf9zVYKasjVWuGcseVELjmq_byFZ2grZppg=w2880-h1200-p-l90-rj'}, {'name': 'Frank Ocean', 'id': 'UCETYiBLjt2v-pcKSgf8pe6g', 'img': 'https://lh3.googleusercontent.com/_bQ5G33KuYf-AIsMAQfOlzLjYxKV08KQsVd6II9NVU-uaGgtJ6S-Zxgo34cq2OKgaX_C4FjNqftzxckD=w2880-h1200-p-l90-rj'}, {'name': 'John Legend', 'id': 'UC7wYAi5loaBGEbOQz7VBF2w', 'img': 'https://lh3.googleusercontent.com/iLVMCf1aIKtGwqi_FL7CRnSMWvD4mwaiJKZpjbc8KXLk6tQgpcvBl20F_jerbkHTNrkfT1ERzBai-g=w2880-h1200-p-l90-rj'}], 'Electronic': [{'name': 'Calvin Harris', 'id': 'UCZ0Aezmtk-S2l8A9Ln-2lKw', 'img': 'https://lh3.googleusercontent.com/8nNzlKW_I90sd-oiJoDpu54BaI2f4YF281SOTonEALOreg6xH4jtoQwR7duCPG7UJzhtOfRj9g=w2880-h1200-p-l90-rj'}, {'name': 'David Guetta', 'id': 'UCh-4c1ZoBPNP1C8c-7iVvUQ', 'img': 'https://lh3.googleusercontent.com/Nm_nq9JlS9WNx94meVL8AUgW-n7LzliJDYvWLrR-2ubFWQED1YQJKTv1AEV0s1gKiA3QKdY7lgimbFY=w2880-h1200-p-l90-rj'}, {'name': 'Avicii', 'id': 'UCuACQmW04T3v9Mz_1_suFYw', 'img': 'https://lh3.googleusercontent.com/TH3IXs5FL0GWk4BWPylXomZ_tUFV3sQQz8IaK1Hhw4sTTbFkCQlUXwAErsMvnoqjRxR5L1nXrsinYg=w2880-h1200-p-l90-rj'}, {'name': 'The Chainsmokers', 'id': 'UCQgUHOPJJrmzCjExg-ISupA', 'img': 'https://lh3.googleusercontent.com/gn1DZAeAiUs5vWpVaCLj9uFD5R75oTGkyqS8Otk_uVG5TIQB57foeLVac-DzoXIcXrLDmR8q9s6J5X4=w2880-h1200-p-l90-rj'}, {'name': 'Marshmello', 'id': 'UCrxpwXq8wCTskOQq5d_KoqQ', 'img': 'https://lh3.googleusercontent.com/FgXNumEMez1nb_08prkNDaGnKChcoTsxfe3dLBQ1bZoDFQ4X1pBnoTbZLeP28dWKkWYxOerVnamKag=w2880-h1200-p-l90-rj'}, {'name': 'Skrillex', 'id': 'UCibXKvuw5PoJVmyZJ4qhDIw', 'img': 'https://lh3.googleusercontent.com/KjyBsa4qngDl-OzeZdW25Kn0l7a3y2-iynPBpTZa5ECbIa_1xqiBWqV9AWcj-CR6mg0At0Kt-qnKIw=w2880-h1200-p-l90-rj'}, {'name': 'deadmau5', 'id': 'UCL44WZGVf-BU5N0ymCXrpBg', 'img': 'https://lh3.googleusercontent.com/Q7lfhLhSevtbi2_w7gEsrfI-zETEQVQndm5EE52VPAyztDSrEqIJ6Eb8cwTLbkIGpUuUq938MA=w2880-h1200-p-l90-rj'}, {'name': 'Zedd', 'id': 'UCGVGIqHPzwLhZg8KQNVaRbA', 'img': 'https://lh3.googleusercontent.com/GrjgqbE58IACC7-SZ-9miFgvtobauDqnOd5Dw9Z-kKXMwPkCio2PTen59hFadf0h8inUifhgbf5cPKY=w2880-h1200-p-l90-rj'}, {'name': 'Tiësto', 'id': 'UC8VSaPhuiHkjobAgNpRqLIA', 'img': 'https://lh3.googleusercontent.com/ix4H5SsMVKo9icIGURXBr0kO4Bt4F5HI29m1B9ubMk2tJ34GLn8nNWx6fpiHl5ABmdRCyfAlKYyWF7o=w2880-h1200-p-l90-rj'}, {'name': 'Martin Garrix', 'id': 'UCqJnSdHjKtfsrHi9aI-9d3g', 'img': 'https://lh3.googleusercontent.com/AH3ND2NEx2st2gddk-QC6qLH_rVnMs7vGhgB-ecC1KHgxtFjZEhOJvbFupxuNXtWPGVu0IlRAwF-hg=w2880-h1200-p-l90-rj'}], 'Jazz': [{'name': 'Louis Armstrong', 'id': 'UCCDaSui4C9VFMpeRlKEOHDA', 'img': 'https://lh3.googleusercontent.com/rToj7b3aISFXIeby5ahIIrrEJcALLL3PMe6YerNNq-67WxTmX3VlKpBAS2BUnV8efjEXbJ0B1kw72Vg=w2880-h1200-p-l90-rj'}, {'name': 'Miles Davis', 'id': 'UCIev2PktTH5mI-QlGmbUkiw', 'img': 'https://lh3.googleusercontent.com/RgU9lxCfVPGtTHV9ipuqFqk8BfW0F166wKLBkmdGKQX7M_a9ti7FsGGOyZA0lj3rvaOLxtBPRQYYUts=w2880-h1200-p-l90-rj'}, {'name': 'John Coltrane', 'id': 'UCH4T2kv7rr9qnuP0DOXLxMA', 'img': 'https://lh3.googleusercontent.com/0Bvhu4NNaOZq_KFArKyQmITvm0B6hEyq5PB2LfxEG0h7KgypRM_FChDqjh2LJIN0m2NHQv-mCk5YH8Q=w2880-h1200-p-l90-rj'}, {'name': 'Duke Ellington', 'id': 'UCvwUPRgFawNNBdQg497gHJw', 'img': 'https://lh3.googleusercontent.com/dPLmwAhF4SsMxyJNCA1wroHc_kSB9Pn01E7CcNT9s4GZfe5PRU6L3OVz801gSFqPvGwzJiCPNvA3y8cM=w2880-h1200-p-l90-rj'}, {'name': 'Ella Fitzgerald', 'id': 'UCuMHq8jMRZXpUxSGLBuCa9g', 'img': 'https://lh3.googleusercontent.com/irTyj56_7yAzo_U3gUwEfWAr-xdISV8fXgUOaKsTZetNi2iuzVejN5K8zufuicF96muuQeyyjRAP4oA=w2880-h1200-p-l90-rj'}, {'name': 'Billie Holiday', 'id': 'UCW-raws5Iq2xLADkLcEoVaA', 'img': 'https://lh3.googleusercontent.com/LXibYBjO8IdWgjon5J-hKgDuVSx4QbEl0g38nb4lNZKr4uFzN8rg0U1D1ARCynpj6N91PfOPI5syuUlK=w2880-h1200-p-l90-rj'}, {'name': 'Charlie Parker', 'id': 'UCPFmyRluI7yvEdbHCrecUng', 'img': 'https://lh3.googleusercontent.com/i0vMawtRNm4hTPzHSYn04CGLtf1zUgwsjkb3Hylc870EbBPcDqN-4WefDhDWWtxSlXodfif9LRMfiA0=w2880-h1200-p-l90-rj'}, {'name': 'Thelonious Monk', 'id': 'UCyCL_gVNVoWZTjkw-KnuIDg', 'img': 'https://lh3.googleusercontent.com/3obpMZCAAsH6qoUPF3UizhgqOQGgSX78QSCxQU8Qob_kWuOZa3AZjvAQhDullQ0AE3om8iS7vexiPQ=w2880-h1200-p-l90-rj'}, {'name': 'Chick Corea', 'id': 'UC7Syqiz3THx07IfHPlgroRA', 'img': 'https://lh3.googleusercontent.com/sovIN0R1CP5h11wKQk3tMkJI-4mjP8DsBYpEHbqBjYp9Lldhi0R_MeK7NRZXhzO0HZvZy2ecqzKvLqs=w2880-h1200-p-l90-rj'}, {'name': 'Herbie Hancock', 'id': 'UCq_O_14tCKbx9U9uUT_LEPA', 'img': 'https://lh3.googleusercontent.com/QgghX-OlklKQWat21PdPf7bLOmSMLQLabJjxXeao61ZJZ-7G-UPSgi1EtEJi0jH577smHMmb-ar1HsA=w2880-h1200-p-l90-rj'}], 'Country': [{'name': 'Johnny Cash', 'id': 'UCiGs21G3KeE2tpbbMPzn9Qg', 'img': 'https://lh3.googleusercontent.com/FesnODpLPJbk5taHyuGG8NgGYlSYgaU8H2YJMR1OIu8Y4635Zkdcs9aGSITi2gNcsyXFYosoBQkuQNgw=w2880-h1200-p-l90-rj'}, {'name': 'Dolly Parton', 'id': 'UCXJscayh5BT8m2ZVFQSdeVw', 'img': 'https://lh3.googleusercontent.com/ZvZFUBod49phwJaA1BDBZZwTNW17-ZQGJRc1TecLbfM41FNhtC6UGFeEDuyxYHrvHJtIj5npLe3R4QRx=w2880-h1200-p-l90-rj'}, {'name': 'Brooks & Dunn', 'id': 'UCJSmF69f8mMuu_kQJbYZzXQ', 'img': 'https://lh3.googleusercontent.com/8Skmg_5qjhur4xQ0gr9HRYYx0RWQsGtUNMdCNkSjJTASDN-k_2Ys8yjFFi9vR7sSnvvqyGV_rZHPmdNc=w2880-h1200-p-l90-rj'}, {'name': 'Shania Twain', 'id': 'UC3H5SQg6oJnxeolvQk6ABWA', 'img': 'https://lh3.googleusercontent.com/w4SqapZPurQwgzTH1-8ZpyQf6TtoejkBVumKvAKjiSr5K_PhaQgxSYzlwpuucTDLFBAZ9Ve-HbrZ8Ho=w2880-h1200-p-l90-rj'}, {'name': 'Kenny Chesney', 'id': 'UCx-U-6-fMEm6yuxm5tUA7zg', 'img': 'https://lh3.googleusercontent.com/yrU4V8_8wk8b4eWbMZ9Icpaetn-KvTnWVpo3gIjoRDYE5J40tEqP_H_EpVbF85ZIG6yQmCWbbdnBgQ=w2880-h1200-p-l90-rj'}, {'name': 'Keith Urban', 'id': 'UC9yy7XoW6jmzZd0lD2yiEOQ', 'img': 'https://lh3.googleusercontent.com/VzLZqXWtmANAy66BaV4IaBK7iZkt8hiJU1PadibEhdk8bGIk5PX7Pt0-kk9_rDSoGtCa10Utqw2T65o=w2880-h1200-p-l90-rj'}, {'name': 'Tim McGraw', 'id': 'UC9UQ96xNXcV6DUiBlJRTvjA', 'img': 'https://lh3.googleusercontent.com/tmAzuxfdBcUhPfCSzZmtNSpCAJbZC0VZhIf_jDm3C4udw5JcMZ3glMVQiJo1ocUhiiRxSB-mzvAwuXkK=w2880-h1200-p-l90-rj'}, {'name': 'Taylor Swift', 'id': 'UCPC0L1d253x-KuMNwa05TpA', 'img': 'https://lh3.googleusercontent.com/U1cI80giSCUuNYx3zkRPt_AWytN1qFMlQoL5F7kTZeFzfIMmfHJYLJchX3BxeDLglE9MeVYp4OlN5Xc=w2880-h1200-p-l90-rj'}, {'name': 'Luke Bryan', 'id': 'UCNxZqWO9mhIqniH6W8Vcp7Q', 'img': 'https://lh3.googleusercontent.com/I1i6G8fkt1ptkqcqqfBXZUBEXaY7PZpRiT0UIjinHLUrOIayO2ec1fwaOdJLYvT5AQi6h-75MVPc5A=w2880-h1200-p-l90-rj'}, {'name': 'Carrie Underwood', 'id': 'UCOKZ9VMYXV5HlyLMOuoiKlA', 'img': 'https://lh3.googleusercontent.com/3v7lzgYAGlTp5QfI4mDt6CdnF-2VS6fXCNvtufO2wrNq0m1WRIpDov2cq9JXitUUnt1MRPUCG3h-1A=w2880-h1200-p-l90-rj'}], 'Reggae': [{'name': 'Bob Marley', 'id': 'UCBfv87kvVXyNi88URZ1zvCA', 'img': 'https://lh3.googleusercontent.com/1za5mxkA6wc2983TI3GbBVJSc2QaEpr0RWB4HakR-q0edqdlYKFhG2KdE1XBE_xww4t1sdwFvxw=w2880-h1200-p-l90-rj'}, {'name': 'Peter Tosh', 'id': 'UCFLzDxCkznTBfJkRBgJ_hwA', 'img': 'https://lh3.googleusercontent.com/2BddM9d-1n4WnGm66sX6WcNsZ_6Mghk2ESBSrTD8OnSLOPbN8GufawjIsuu_6hfmNdcZdwbmfj7vFbQ=w2880-h1200-p-l90-rj'}, {'name': 'Jimmy Cliff', 'id': 'UCFAsFFXKy4vpvdXbnZAEyOg', 'img': 'https://lh3.googleusercontent.com/Qx8nabrLby2QJdvmaCgMxPZwwkBwz6k4pVdU8Rkholi3lb-1iHUulgWn7AYpPRqCkWGjI87aT8suVw=w2880-h1200-p-l90-rj'}, {'name': 'Damian Marley', 'id': 'UCu1as47vTAurke8pciuGcMw', 'img': 'https://lh3.googleusercontent.com/U2uiFEfF5ilIcuKgh4xkr7DvAYHX61zMPtHAxTJHjanHePB3nq-fg-R0howm3KGUXZPM7FdVDunycPI=w2880-h1200-p-l90-rj'}, {'name': 'Sean Paul', 'id': 'UCnCNNA05VZcH8wVJYtC-6ew', 'img': 'https://lh3.googleusercontent.com/Z4stcdG5DZu-MBapbHCg6XcPJgbOSFVZTyOS4MHcJnemtzMupvHgeCr7sLr0zT6ME2_L67brgNA90QQl=w2880-h1200-p-l90-rj'}, {'name': 'Toots Hibbert', 'id': 'UCrHs1rY0pGwmKaj1bIdGnGQ', 'img': 'https://lh3.googleusercontent.com/N1a9fyGCjeOcIe77pEqqFp7pOjwIut0RCjBkYRWYIA742ty1vyIT8145xcioydbYwU8ZOVRrWK2VYJzC=w2880-h1200-p-l90-rj'}, {'name': 'Ziggy Marley', 'id': 'UCsMjZkTMjcYtG0s5yxXzgUA', 'img': 'https://lh3.googleusercontent.com/-Z5LpHxPAZD-vsRrOubjzm6rqAtABQhCsOgKP05dGMcyGTkvJSqHHMZc7ZMzsyHXrZ6CRf-mkdz2JBY=w2880-h1200-p-l90-rj'}, {'name': 'Bunny Wailer', 'id': 'UCbOFji5tmPE9lx8YDjoU_eg', 'img': 'https://lh3.googleusercontent.com/F5bsYJTYE7x9TShnCxmyPNt97JRo_rAn-mg7WlRoqWpYYOHA-hgVA1HM9HZ-QmAkhEyf6nF1SC38JEM=w2880-h1200-p-l90-rj'}, {'name': 'Shaggy', 'id': 'UCUqmn42LCN5JJ6-0lQl0vPg', 'img': 'https://lh3.googleusercontent.com/EMrf00d1nIfuwakv6PQSHxDM0kRvYoV9yahhZMmxQgE8PdS5fNKQ9uACHfCw4Zk_aRcQiV1yQMFrbgU=w2880-h1200-p-l90-rj'}, {'name': 'Steel Pulse', 'id': 'UCQm5FW2a60NQmsClcbDnygA', 'img': 'https://lh3.googleusercontent.com/adVIg5HA2hk4-mWoHUj6Z7TKKQ4OxGNrLOzsuE9JPFcLtxToabXAbxxsrcsEWaPRsO5Kw01BlwYfLcQ=w2880-h1200-p-l90-rj'}], 'Classical': [{'name': 'Ludwig van Beethoven', 'id': 'UCnsAooIr-Dsr8zJOCSadQcA', 'img': 'https://lh3.googleusercontent.com/mIAE8wKX56JqCULD5ryJEk6J9BHu8G_XQKqffyZU4OgDFBWVtb0zwLsbO5CG5MaKlMLgW59JrGrduQ=w2880-h1200-p-l90-rj'}, {'name': 'Wolfgang Amadeus Mozart', 'id': 'UCmeFxYk5BSbJGWN9OgTAIhw', 'img': 'https://lh3.googleusercontent.com/pZyWzrMGGncmh-PudR2HH7IN9rcQZFKq3mSryoUXmVY1hyyoSrmlieHaDCnqSdRpWSmJjNgvLT5wtIA=w2880-h1200-p-l90-rj'}, {'name': 'Johann Sebastian Bach', 'id': 'UCFtSXTlIMFFkyJbHO3V5b7A', 'img': 'https://lh3.googleusercontent.com/C5hLBPYdwgyQEKjwZXfOM-0MCgn619Ja_WgljDeIO-fjNHi-SsYzGr_c5piG46OaRj_ROZqhuCYhucmf=w2880-h1200-p-l90-rj'}, {'name': 'Pyotr Ilyich Tchaikovsky', 'id': 'UC6UJm5ElaATOPzXxNkuLDJg', 'img': 'https://lh3.googleusercontent.com/bEZEdZEhUBzRT52SK4kSYfcPkHobDfG18zAWSFWGy2WKrWLIxnQEaiSEehV-R_ezUkpYpvH3a7D37P0=w2880-h1200-p-l90-rj'}, {'name': 'Franz Schubert', 'id': 'UC7l3IFSPxafcH_GTj1VWTeg', 'img': 'https://lh3.googleusercontent.com/tvnVfyMJ0kuUSaeSHdhfXVRsAtcEHDVe99U62rtGdWJ2zjS9Axlq26S1gQruH0HxrSkjNnZXQbGxB3I=w2880-h1200-p-l90-rj'}, {'name': 'Claude Debussy', 'id': 'UCDBe28OI2PycHdECfoaIWtA', 'img': 'https://lh3.googleusercontent.com/GtlibpMRuI_NuSzSy_N-KGKXgr4OZg4TnVaX7VeGn5suKliSWH41BNZ34MGqQ9-FEarQCYLGwQtqhvE=w2880-h1200-p-l90-rj'}, {'name': 'Vivaldi', 'id': 'UCGU4MTUOmtNe40qxaZx1lFg', 'img': 'https://lh3.googleusercontent.com/a-/AD_cMMTXiGi-YcWKeZ_CezRYXvgex-MvSkrQ_5nmwXSojQZUpQ=w2880-h1200-p-l90-rj'}, {'name': 'Gustav Mahler', 'id': 'UC4JndR9Jg60dqinZE45umxw', 'img': 'https://lh3.googleusercontent.com/6kkhqnR14GbWrxng762sdmmw7tzoe9ypuTcNBPhDmHjpcgH3yYJg2MXuHOVzcGC07E8ytWAyrkHt-Q=w2880-h1200-p-l90-rj'}, {'name': 'Richard Wagner', 'id': 'UCqRT-aGYojd-in6xTOT2-OQ', 'img': 'https://lh3.googleusercontent.com/bLQPgJRMwMSfV5i_Y3n4FOtR1mGIxnKlbA9HTNpfp5YRfDtWCtjzWWKfKaZMh6s-RmY7t9N2V4gl-9I=w2880-h1200-p-l90-rj'}, {'name': 'Igor Stravinsky', 'id': 'UCELh0PB52k1uiZP91LKW9VA', 'img': 'https://lh3.googleusercontent.com/08C76ZGLaVJU2BAgsM0p17al-fzXXYlhwtCnFeIcV1Y1TkByIERr_AwTItpZvIMLHEcmi2GEcITeI7G5=w2880-h1200-p-l90-rj'}], 'Blues': [{'name': 'B.B. King', 'id': 'UCqKrqzF3eX7R17m_MIMte4w', 'img': 'https://lh3.googleusercontent.com/a-/AD_cMMQhuJyOYdUqJyoaBZkvrOCKn1bW33lprruBI3DD9G01HA=w2880-h1200-p-l90-rj'}, {'name': 'Muddy Waters', 'id': 'UCZ5YpKcmxGptLgRRW8ujxHA', 'img': 'https://lh3.googleusercontent.com/vuJYW7X5Ivt8UVpsi5nsSAQfS-Vd7uwIhirujeb4QDmjr0qhuKvs4V4VN3XDCp7HE9pdqWedw0Z6i0Q=w2880-h1200-p-l90-rj'}, {'name': 'Robert Johnson', 'id': 'UCjcp3ChO5oUZyx3f0FnGVUA', 'img': 'https://lh3.googleusercontent.com/GAOZGStdcSgA9vikzDrb_siKYcR1_8m465HviM2bK1aU_00AqhjZcnlxFn9Bw59g3DZdtK2GUdNvZmKb=w2880-h1200-p-l90-rj'}, {'name': 'John Lee Hooker', 'id': 'UCcWk0Z6iOwjUeycdoh7mIMQ', 'img': 'https://lh3.googleusercontent.com/yQKhWUEZULd8exxM7RLmKJOjj-eg_RfDvGq2KOtKHKdNDeozuHWSA9r1tUpOxXfjQvHo02UiJAJ1a1Gg=w2880-h1200-p-l90-rj'}, {'name': "Howlin' Wolf", 'id': 'UCq7KYdlYIAjlt2NbSEZD7bg', 'img': 'https://lh3.googleusercontent.com/ROSqrj42rMqni3FL4rvk8XyyWtpUYN7mjZdXRVbkO3sjMNZxb3tAzyRspj6PKR_SBod2Wx5Hfv2jaA=w2880-h1200-p-l90-rj'}, {'name': 'Stevie Ray Vaughan', 'id': 'UCG47N6MrGcPaJpVRgBoAVAQ', 'img': 'https://lh3.googleusercontent.com/pnD7uq4760qNecPTM8SD-m8sl8ukPlGhJcH-BaKYbbQs6ElDPLwx6TYx2ziJhk6wYwMIXUxbSpJeWw=w2880-h1200-p-l90-rj'}, {'name': 'Etta James', 'id': 'UCieyolnCbsWzyEt6wsd7lgQ', 'img': 'https://lh3.googleusercontent.com/SCifxn2sFqVKZzbWtNk0O_jJgAmU5c04xpbVcSlaVEDkSfOvxGMsH5WzIMKALVLXL5H-QpKg6VD9KKQ1=w2880-h1200-p-l90-rj'}, {'name': 'Albert King', 'id': 'UC9XFvJIqt0duVgnlvkXBeKA', 'img': 'https://lh3.googleusercontent.com/Ayy2HaHhIDSrHNZDLO9Awy6VJb-_vAL5H-aR5favHCChEjvQvl_eSrBzDXxegudFKvUBs0UdIrDLGw=w2880-h1200-p-l90-rj'}, {'name': 'Taj Mahal', 'id': 'UCylg6tzCZVAJrq5z4i1bgpg', 'img': 'https://lh3.googleusercontent.com/iQeNUUR-PndnucTRSbf0rx1BEJxxcVs31w_xnwEkOrKwYogCj88vmJ03KW5XNe4whhWQKgTe-TZfwH4=w2880-h1200-p-l90-rj'}, {'name': 'Bonnie Raitt', 'id': 'UCt3dWNI94rZKmfzuwZyD5Fw', 'img': 'https://lh3.googleusercontent.com/yvV2cSw6nj-iCx3vUsZQgBU_gmD1_Mj2bALRZpbbykJD3IwF9EX8yRWs6n2xMzjRGdDKLvGdgUkpEoU=w2880-h1200-p-l90-rj'}], 'Folk': [{'name': 'Bob Dylan', 'id': 'UCBqkojCXby4zGkWX86FEY7Q', 'img': 'https://lh3.googleusercontent.com/tn1ajpYJaL0uVyUIgegB0qw4f6ZhWb8YiHGoIZCTPHPrzFv1aq_vz_vzxzwoA9bgMK98WlzwPYco5A=w2880-h1200-p-l90-rj'}, {'name': 'Joni Mitchell', 'id': 'UCvlAqrv-_NlUzyFFhhep7PQ', 'img': 'https://lh3.googleusercontent.com/6qX-LRW3AWaak5qVSskq4UhshvD3iUI4aS3d-ZMKTx3_fRnm7e3AFSafFhOB2XJ4zfXcBkONrz_0GcQ=w2880-h1200-p-l90-rj'}, {'name': 'Simon & Garfunkel', 'id': 'UCOovQ5kcvRFGh4ix6Q1SsKA', 'img': 'https://lh3.googleusercontent.com/MbRUu1Wu6GllMptKKl0Z0ppWWL8UWMgSnJ72lrAyVSbJe_--lKU3zO1BIVj09ml0hAVlIN9Ch7CXbkRu=w2880-h1200-p-l90-rj'}, {'name': 'Joan Baez', 'id': 'UCS1qmMQEO8KBurXzQCjlbrA', 'img': 'https://lh3.googleusercontent.com/bPQ2NzXwzx__gQN-40YToParQyxhafE6_elDG1ZVo7t_sJrYcdAB-89ka3pCPDVNL1YjyGYE5xSzFEc=w2880-h1200-p-l90-rj'}, {'name': 'Woody Guthrie', 'id': 'UCgbCJIqwRQbo8xuVWvQFqYg', 'img': 'https://lh3.googleusercontent.com/179hWI_oy8GdaH3oxJVio0Rf40HdL03iBp8VlBtnKulsBzKkvSE2gT59g91IZ8b2wAMIP_xtjst8JRw=w2880-h1200-p-l90-rj'}, {'name': 'Pete Seeger', 'id': 'UC6J7zes7i6Fr2GmwkadEq-w', 'img': 'https://lh3.googleusercontent.com/UWDsR7hzUQtvdZ0I-q9Y0HCvDAcdkoBqH6VHZGI_bohjn-xoYaBDJvl_ec8kJlwD3Mjj2uGRBEU2cQ=w2880-h1200-p-l90-rj'}, {'name': 'James Taylor', 'id': 'UCZJikx4babgeliqeRPnE9rA', 'img': 'https://lh3.googleusercontent.com/-S4qhrWVSjYWAU9Fxw3ugn-WgvfE-WD_29WYp-mm3mO-UqtwZ6Jce-Gzo7AxYcCSdEku79235duhK3kQ=w2880-h1200-p-l90-rj'}, {'name': 'Neil Young', 'id': 'UC6JhadLTf6g6f-ZdeEaAqBQ', 'img': 'https://lh3.googleusercontent.com/S3_EIKQJVSyY9G0joYX6vRogAAURwT6TujCfl8CR7bZxSFB40dSU47nsjUSA2FdMjZqX04ybSXbbmt8=w2880-h1200-p-l90-rj'}, {'name': 'Yusuf / Cat Stevens', 'id': 'UCpzTj29sgB9oSPIuFqy1ShQ', 'img': 'https://lh3.googleusercontent.com/Mh7pacPOmsiPOMuWmhby2c7firVBGMXVlc3wc_2gJlZPS75LXdBgX048nd1HozwTjt76CEDobt5jegI=w2880-h1200-p-l90-rj'}, {'name': 'Tracy Chapman', 'id': 'UCndrh03uIKb9SUR7-znGZ9w', 'img': 'https://lh3.googleusercontent.com/KzA9PHXjq437N0DCbyqLX-BE_e5GRz0l3Xd9RwYq2L-8fFy9buH92JZze5MX-QZ_E1_70iA6WcwdtWw=w2880-h1200-p-l90-rj'}], 'Metal': [{'name': 'Metallica', 'id': 'UCGexNm_Kw4rdQjLxmpb2EKw', 'img': 'https://lh3.googleusercontent.com/KnByTUXJkfrqlDoS4LXhyRFZALhxmHOfBtI9FLHtb1g5OB5msMdHXHcISvwtQGNtzwXKqjDmIw=w2880-h1200-p-l90-rj'}, {'name': 'Iron Maiden', 'id': 'UC0zbzp6x7zR8u0LhanNWFyw', 'img': 'https://lh3.googleusercontent.com/nhiZLMxjoxcIOcjrMr_Es_0ARMq0iCMkcfMivwQZrF5UL0kJwUthJIAH6dnQstu3MbmyyPGX5RazQ9E=w2880-h1200-p-l90-rj'}, {'name': 'Black Sabbath', 'id': 'UCLCELUuoHbkUxZ9EMHTYebg', 'img': 'https://lh3.googleusercontent.com/DvpOh4gP93F7IvpgquneYfSK9pwaHDZ4NptCpDAiakAapVTbN81nDok6VYI-68HmxSSQGBGYzYNhhA=w2880-h1200-p-l90-rj'}, {'name': 'Slayer', 'id': 'UC9S7S6SFgBenThCZC6qbMoQ', 'img': 'https://lh3.googleusercontent.com/DyDMTj0hXBloVrrLHgWYgo-ydul0_8uYPg6gVj4guLKhRF616Kgm3L8_pohHlVx0urk8ODEZBsOgJayS=w2880-h1200-p-l90-rj'}, {'name': 'Megadeth', 'id': 'UCW5bkwocGGoeJjHTJZIEAOw', 'img': 'https://lh3.googleusercontent.com/Lc6P8m_OjADjwtwbphEmQP5J_fZ_VsGFKSl9lpLpIB5IPlBcgDAyG5Of9RFuH5dFePVbu7CRRwKV2eja=w2880-h1200-p-l90-rj'}, {'name': 'Judas Priest', 'id': 'UCy6-RHgm74I8CCCvMu4NPJQ', 'img': 'https://lh3.googleusercontent.com/qDNmw6VJxeaeczjQSJEonI973462Fd1-OR3DrISJcdtcXgLgS_hSnWL72fKpQ7WNbCNh5TNzIb6U-Og=w2880-h1200-p-l90-rj'}, {'name': 'Pantera', 'id': 'UCZOWwQaVFO8QxRVVIJBTEZQ', 'img': 'https://lh3.googleusercontent.com/s75jxKcUOPBam-pZijM44PGNsR00eteduxQaV6XEqaMdVaVD_uWK92Czqb-EEPQSc7e8uHp6Az2FUJw=w2880-h1200-p-l90-rj'}, {'name': 'Motörhead', 'id': 'UC29TwdZt2GUC-AqbhFs_uSA', 'img': 'https://lh3.googleusercontent.com/6cta3CAsJUPqqFj5iPIi-LhAjFXYmhNi_-1KgBcVbSRbJbgOm165tcFRSjpMwpq7tW6v2NAg2-f8JAM=w2880-h1200-p-l90-rj'}, {'name': 'TOOL', 'id': 'UCW6FSIkA04g7pBvMXlnaKqg', 'img': 'https://lh3.googleusercontent.com/c0zfXl5j2_Xzm72W9QnstAyo-JhH_iQDlsl_FyJ9FKPbXRebcvu2y-dlVocK9iFfi25LS8Ceq5k9_as=w2880-h1200-p-l90-rj'}, {'name': 'Korn', 'id': 'UCdSgOgQ0WtelXBMKF3tDsqg', 'img': 'https://lh3.googleusercontent.com/stTENs_iguH8neg1sIkSoUW4cFtuEDZvRZaTtljOmghycUXsts2rvmHkH0f3FUNGNSfm2UvnbkBP1w=w2880-h1200-p-l90-rj'}], 'Punk': [{'name': 'Ramones', 'id': 'UCXYTNaRC13Mc0muUaYDrT9g', 'img': 'https://lh3.googleusercontent.com/LfiZwoc7CMYj3AXm5mVM8oM60bt-hTN4yoDQyXE9dftDLptREDFaqbulqrr4KEYF8aIoKHbBp_s8Kg=w2880-h1200-p-l90-rj'}, {'name': 'Sex Pistols', 'id': 'UClN6gQsL6wKtLzo1S_-ui2w', 'img': 'https://lh3.googleusercontent.com/ZitucVjCPPOLcwMb28irTmmcdCroAkbSzFwPYg0m4CRbZNQI7sW-peCSPhMf2n62c-Y1RHHXUtV4kH8=w2880-h1200-p-l90-rj'}, {'name': 'The Clash', 'id': 'UCf-a_3DiA07vhQmoEaczDhw', 'img': 'https://lh3.googleusercontent.com/pv41w-O3Bx7SMSu3nPMupxGMKWOqQt5kdvRMFw-S_-SvolnTXopnC74cVz1hzzf75eCoM-xTCFTPUH63=w2880-h1200-p-l90-rj'}, {'name': 'Green Day', 'id': 'UC4JNeITH4P7G51C1hJoG6vQ', 'img': 'https://lh3.googleusercontent.com/HSa3KQdjGlvXFB-He8HKuZ4Zj3AT3qmjQ1kbRsR7ZNGuxqOUnF1UoEdPAvQPEGXk8PA4Flf3G1DXpQSI=w2880-h1200-p-l90-rj'}, {'name': 'blink-182', 'id': 'UCo23ROZAe-BZYHpzBu9630Q', 'img': 'https://lh3.googleusercontent.com/P1xw4CuyE9zhuNwtmPSI_TCECDTp59MQDOhrKe0KfJy7XyCfqikxwTkOT4b2Wy8v4O4iEgeL250yCI8=w2880-h1200-p-l90-rj'}, {'name': 'Dead Kennedys', 'id': 'UCnGbZT2OHo8Kc0MoVpDi9cQ', 'img': 'https://lh3.googleusercontent.com/JCbeDxIkuqs4mV_Y554XhRW6TY_gwSlV5MO5eLdsDhYa_75f_x7l6zJ9cHxU0m3is7yvvfhMjuISrw=w2880-h1200-p-l90-rj'}, {'name': 'The Offspring', 'id': 'UCQVUXQu8RpxhihAMla6ke5A', 'img': 'https://lh3.googleusercontent.com/okgpbT5PycswKWM6mlJrOnv-PHw_tQ8hSxMbOCQ4kHR7_p7tJD598JWlu4WE-QozGDVoW06IKErZQA=w2880-h1200-p-l90-rj'}, {'name': 'NOFX', 'id': 'UC5-MatmZOvX-ORzhTuO0ZiQ', 'img': 'https://lh3.googleusercontent.com/PkmSz8QKFxc9hzfB3YE-bermajs9LKctxmQLZMnxbmSX9AL5AwcGUEFuyM8hr9iotpjQpmIUuJuoF7M=w2880-h1200-p-l90-rj'}, {'name': 'The Misfits', 'id': 'UCUAa1fv7JsIFuBUWtH0ZaOA', 'img': 'https://lh3.googleusercontent.com/MQmGUSYrzdcgGus92CLtSZYbZ_8K1y1v44VpsYtCE2_FXrTEk0-atUtv5wMI_mh9KJNsKxPa_mbDqYE=w2880-h1200-p-l90-rj'}, {'name': 'Rancid', 'id': 'UC5UyvYJVUtezUGNJ4c29GbA', 'img': 'https://lh3.googleusercontent.com/9nQ2RCbf7X5T0DhpuG3TPfc0uYGN-xSAxxD95ZeCkpYZ-I-VXvy4o0EuYEX_YbvNhqWaUvD11xLmV-s=w2880-h1200-p-l90-rj'}], 'Dance': [{'name': 'Daft Punk', 'id': 'UCRr1xG_2WIDs18a6cIiCxeA', 'img': 'https://lh3.googleusercontent.com/qLhu6Py_4_xoBsoubKQsXlhOQGqU9YU1ZRAbFusF0LlrPkXbbpu7bEh-k_ZtE4JwLgubvucAQqcK1hRk=w2880-h1200-p-l90-rj'}, {'name': 'Justice', 'id': 'UCcJLC91v0A0iD-CMUWdZkig', 'img': 'https://lh3.googleusercontent.com/X3qK9BY_u4OgfXkOW8WliYoDi_PkGEg6Od4FakGjqlO0KvowhTcY_oZSozF4pUKUYkN1bmHsq-JpXg=w2880-h1200-p-l90-rj'}, {'name': 'The Chemical Brothers', 'id': 'UCyPCkwR4gcQNybC2XzMNFTA', 'img': 'https://lh3.googleusercontent.com/akuE1pMYmBawbe2yzxKX2JvNVAaauXb4kjPoyfg4s-VOisvh2CQxhPGXsf3i07O5X0tK_BQ1WVKhv2A=w2880-h1200-p-l90-rj'}, {'name': 'Fatboy Slim', 'id': 'UCNekatqy_ys1SX8NfjpwixA', 'img': 'https://lh3.googleusercontent.com/G9IAV_qvA-o3eZ0wJgV98CuhG9s3o15YAAFQuRiuTRBvlEYVHwVtpHcLHSJvewUzxNCXb_ry_HcK-FkQ=w2880-h1200-p-l90-rj'}, {'name': 'Underworld', 'id': 'UCahiOREGlmLx7vi-35NbdBg', 'img': 'https://lh3.googleusercontent.com/3WY1IoKFAOc41mj7AYkZo4BE7HS0qlgYegmMHMF48a_vS8MIRcnUZFLPBFsUs9aBwx6MTnvh4inePcQ=w2880-h1200-p-l90-rj'}, {'name': 'Basement Jaxx', 'id': 'UCAfJ3OKeayzTdq3tFyIrDHg', 'img': 'https://lh3.googleusercontent.com/9KiP244395AKCvOVPebOTYNwqBOg4BBZZOH7X2Yxiazw6jDp0GsIRJk0E8R8BFBbOLxPf0oJEJlHWLs=w2880-h1200-p-l90-rj'}, {'name': 'Paul Oakenfold', 'id': 'UClQvWIsyq8zH_xlIgr7UJcg', 'img': 'https://lh3.googleusercontent.com/U-Qxpd4HTEP9xflM-JxBJjZdNQ3bEDC69bd-MOvxieUbMaEnjcmfss-lQPFgzySDZVOfqpJB2ONlAQ=w2880-h1200-p-l90-rj'}, {'name': 'Armin van Buuren', 'id': 'UCAeLFBCQS7FvI8PvBrWvSBg', 'img': 'https://lh3.googleusercontent.com/Oke8ahYFvhmsB-cbT0rIK-yvXc5FqKYY_ZgxnysgSr8-JwC1Ywgidkd1M7HM4nm4mxmfU1wxH3PFWLK8=w2880-h1200-p-l90-rj'}, {'name': 'Carl Cox', 'id': 'UC_2ZGM1YP91QYRKhHVANZTQ', 'img': 'https://lh3.googleusercontent.com/EF7-vTbUNFmBloI9BSavV7Ylk6zqWocLG1Hhq3gl1dZ06s3cYv8EDNfyUHRKVpxXaFH1DmyUGeP77A=w2880-h1200-p-l90-rj'}, {'name': 'Tiësto', 'id': 'UC8VSaPhuiHkjobAgNpRqLIA', 'img': 'https://lh3.googleusercontent.com/ix4H5SsMVKo9icIGURXBr0kO4Bt4F5HI29m1B9ubMk2tJ34GLn8nNWx6fpiHl5ABmdRCyfAlKYyWF7o=w2880-h1200-p-l90-rj'}], 'Alternative': [{'name': 'Radiohead', 'id': 'UCr_iyUANcn9OX_yy9piYoLw', 'img': 'https://lh3.googleusercontent.com/o_9BDAQZy2-R-BzR-MO91rvly39MRjxV_qUbdzYdvyOPu9V2CPix9nRXroTMvy4f99zdLhKePFHQEYA=w2880-h1200-p-l90-rj'}, {'name': 'Nirvana', 'id': 'UCrPe3hLA51968GwxHSZ1llw', 'img': 'https://lh3.googleusercontent.com/yoFwkvvbmM3u7q0VM_HpjCnsaViQx3gWuycm5OsdmRqWBHL4LyIpNQ5kemdcoW7zrGETTutR_5c_xk8=w2880-h1200-p-l90-rj'}, {'name': 'Pearl Jam', 'id': 'UCI1tnOMUhNh2QiHTpMrPDbw', 'img': 'https://lh3.googleusercontent.com/btX91X6V9ZMo6c59bk5PeJqQFp2dKAHKMEV0tnOKybdp_agkj-UwpQt6DGYpNeuz-6bBlrl0nTAi4w=w2880-h1200-p-l90-rj'}, {'name': 'The Smashing Pumpkins', 'id': 'UCZM3bF24BS-qDMe0OigpeZw', 'img': 'https://lh3.googleusercontent.com/Qtxhx-v5a5C_jnINqxEujeNGnkbJ3pPu7ie5Me0EMA9XOaE0vWheGe-I1bwyjzgY7hhHG6qPvzT4FKs=w2880-h1200-p-l90-rj'}, {'name': 'The Cure', 'id': 'UCKuG9-MGolUuWbEcoz5qijw', 'img': 'https://lh3.googleusercontent.com/zgxx9xJI-x-brHQKRONelnaAEklEkq4pShEJ5Eq19yhWxOwfuiyoR_YpzcPZ_ckimGO2syALRh5MWvQ=w2880-h1200-p-l90-rj'}, {'name': 'Jeff Beck', 'id': 'UCDPMz5gHZt_TgS8JX7lS71w', 'img': 'https://lh3.googleusercontent.com/7aOs75d3x--cD6uXcGFfLAWXtXAoCUie5E1py51DKYa5_kTox2mrKITZIrIAWO5zkSqb7a10xY4MRsaA=w2880-h1200-p-l90-rj'}, {'name': 'R.E.M.', 'id': 'UCZQMYjqm_j5mBVTfPcCy3FA', 'img': 'https://lh3.googleusercontent.com/aosgWu09nIxHcg8yJ88yFCPeas3gz8OlDjdXBfWlFiH9Uo5NZEM5f6dDqrKunNva8RVF6POUyHt22GU=w2880-h1200-p-l90-rj'}, {'name': 'Nine Inch Nails', 'id': 'UC8txE2ZyN2Sh8XxH5OkHLSw', 'img': 'https://lh3.googleusercontent.com/Z7oKqV22vlbB-rp5X9sdGIf9dGLzzyxxIJ3OQPu5QxpyaLc0MQQzGDHV7MRXLa882uY_OnTmteryuBQ=w2880-h1200-p-l90-rj'}, {'name': 'Blur', 'id': 'UCI3EFb2lvZyBMykNd64JDhg', 'img': 'https://lh3.googleusercontent.com/B0mCtQOdMRlQMxp1DoIuisVPwIyFexGPbMK5tHuiNC_IAr9AkOdRR83vdHFQdG5E8ZnH62gfw1jTwpGU=w2880-h1200-p-l90-rj'}, {'name': 'Arcade Fire', 'id': 'UCXvAK640Ko85SLbI-zA0ZCg', 'img': 'https://lh3.googleusercontent.com/TiAcP19PlmxR3iIAQmSBwvIUE6i5SloddubTQBs2c1raALYpr7L6WaExvToQvvNMLkGZBVTEnEWqF-A=w2880-h1200-p-l90-rj'}], 'Soul': [{'name': 'Aretha Franklin', 'id': 'UCW02f_MjH8n1uMZhSds4mQQ', 'img': 'https://lh3.googleusercontent.com/HX3H9VxY4LuUR04Ey0-B8JO1RpuvH5-0P9sXDVzHt5KEwmDq10Hc0rtDhc92rQmYFQzoSepDSkcylg=w2880-h1200-p-l90-rj'}, {'name': 'James Brown', 'id': 'UCLSKiNGc_qBWJJ-m5y3jDEw', 'img': 'https://lh3.googleusercontent.com/NHOCpekLQdxPifmG2D5dtiJmrjstBvsqACwzWaEJIAhKYXhV3Zgo3I6rEt7agN603EJArlpf_x6ej9c=w2880-h1200-p-l90-rj'}, {'name': 'Stevie Wonder', 'id': 'UCR83RRXHzXrEQbu_ZQmPMSg', 'img': 'https://lh3.googleusercontent.com/a-/AD_cMMRuZ_RhCreWcuDAOjRkwJOSVrSZsXsxvT8pYKljyFcJ_w=w2880-h1200-p-l90-rj'}, {'name': 'Ray Charles', 'id': 'UClapQBGYNOoLYmCct6e3B5Q', 'img': 'https://lh3.googleusercontent.com/BcwP9rh6oifdO1XQnN1zg-332EgN3IAtn1vCtja-1V5FRmmzx02c21qtLxCGcXB9SQje2REhiWjOfA=w2880-h1200-p-l90-rj'}, {'name': 'Otis Redding', 'id': 'UCqgDLm2XV81s2IdoF4Skgbg', 'img': 'https://lh3.googleusercontent.com/hdMcvxdqtTRf-oc3C9XAcdDG0dPvLjhndNoLx3XVEy_C4yiSBkVi37jCiBjomD_VFTvbBfkUCXrGBfwi=w2880-h1200-p-l90-rj'}, {'name': 'Al Green', 'id': 'UC7tb2Of68kIlrtj2qUnJtbQ', 'img': 'https://lh3.googleusercontent.com/rdu8DGCHxXnqrE9CKl3z5kbTfzIMLlSJInqmu2kYlW-G92ejg5ZGPctDlLPfnvinRYmB3e50M2fF6iL9=w2880-h1200-p-l90-rj'}, {'name': 'Tina Turner', 'id': 'UC3XcDooUnwiaiTPlICV6-ig', 'img': 'https://lh3.googleusercontent.com/AofpLcuYv0t0pfSrwGyVxJQp7rtyj_H3y1jF9jYtop04xf7LXW-vEoa26Rc0maoPt8aiPWrAkMpw1r8=w2880-h1200-p-l90-rj'}, {'name': 'Marvin Gaye', 'id': 'UCpMMYJB5GJAYSJr3QpxnHEg', 'img': 'https://lh3.googleusercontent.com/esyKhWghWBdhtZIfkgIrG8vY7DhGFNDZbwSvmGWhjDqH_F9AvoRDAC-MyMIAgldMHliQpYNm-CGcwfg=w2880-h1200-p-l90-rj'}, {'name': 'Sam Cooke', 'id': 'UCYW9vMurwIpx1l0bb8gyK7g', 'img': 'https://lh3.googleusercontent.com/OWkKtFCC-PBSUiQasPitq3xGwI79RmGM2EILkNtgH4gFkjXDoG8-Zw39lSfNm1rA9rQ9VZd_zvE-=w2880-h1200-p-l90-rj'}, {'name': 'Amy Winehouse', 'id': 'UCMRsEwcN5cXdvqNP-UBup_A', 'img': 'https://lh3.googleusercontent.com/iH214983e5hbimMZEjbjPq4bo0_OAJxTGY9DveVjxYtiIAgZu_lzJggPM2dPbeblpoLQsNiw9LsAL8A=w2880-h1200-p-l90-rj'}], 'Funk': [{'name': 'James Brown', 'id': 'UCLSKiNGc_qBWJJ-m5y3jDEw', 'img': 'https://lh3.googleusercontent.com/NHOCpekLQdxPifmG2D5dtiJmrjstBvsqACwzWaEJIAhKYXhV3Zgo3I6rEt7agN603EJArlpf_x6ej9c=w2880-h1200-p-l90-rj'}, {'name': 'Prince', 'id': 'UCPIZb3A7k6zLefVNtaAmvGg', 'img': 'https://lh3.googleusercontent.com/VCwDeUl4U1UdEpXsYnkvYsqH9KVsWINZwSIgaipN7TEpiF4vwJ_QJ9khQUJlQ4qFETlgXZ0MMa1--Ek=w2880-h1200-p-l90-rj'}, {'name': 'Parliament', 'id': 'UCcmsXjBIjEbFMRHhtdnFnqQ', 'img': 'https://lh3.googleusercontent.com/XqbVS1ap7Dmw5Pd2_nCTJcqHUG8Q7-i1SyCjedb48ObXdC5DO6mLDETL5pMqDBVDPn0iiaqIT8oCio8B=w2880-h1200-p-l90-rj'}, {'name': 'Stevie Wonder', 'id': 'UCR83RRXHzXrEQbu_ZQmPMSg', 'img': 'https://lh3.googleusercontent.com/a-/AD_cMMRuZ_RhCreWcuDAOjRkwJOSVrSZsXsxvT8pYKljyFcJ_w=w2880-h1200-p-l90-rj'}, {'name': 'Earth, Wind & Fire', 'id': 'UCdyqvgHHq9NEEfV20lO61jQ', 'img': 'https://lh3.googleusercontent.com/wqJ-pGtVA7e16RB4DYctqvk7HtNgjtvlcYeiG25eP1CzujkWCOfwbvMwof2O3drckdUKNhxVKWSnHnES=w2880-h1200-p-l90-rj'}, {'name': 'Sly and the Family Stone', 'id': 'UCgwJnBJfprQYGX3OPQrTvqw', 'img': 'https://lh3.googleusercontent.com/1_PK7ZNgQBPduCFBjKe-YujiCj0YY-37QYraXi9-9rCrwvgbFj48dj7Xxf9qNMdPGfJaa7GstG_qrveZ=w2880-h1200-p-l90-rj'}, {'name': 'Chic', 'id': 'UCpQUvuZiddKoVsKCq0086Eg', 'img': 'https://lh3.googleusercontent.com/uSCETcOgY8ir7z-0mgP_Bc3tNZg21GwHsZUko7GnxbV1N3fr95vISXq504HBJTl5xOnRY0m6n4Ip874=w2880-h1200-p-l90-rj'}, {'name': 'Kool & The Gang', 'id': 'UC44z3Xy2dA0dM3ql1hgrwCw', 'img': 'https://lh3.googleusercontent.com/c60xfi4yjefQlskWIq14b21vVo4s3TMOTJLWhCvMLcyO5uMi1QpFYq1jh45DyHpDRkpCGHOQvNbyf7I=w2880-h1200-p-l90-rj'}, {'name': 'Tower Of Power', 'id': 'UCkSrbTm2YvkMiVopasi5yHg', 'img': 'https://lh3.googleusercontent.com/Yl3n6OuR8IOm63RiyDbuh8rZdZXu30sh_qXCgKtCcrR_2bUXUnjm8TtQPx25uia5tqgXd0ziU7tsY1U=w2880-h1200-p-l90-rj'}, {'name': 'The Meters', 'id': 'UCwye34yhtCbWGQsrFS4oMNw', 'img': 'https://lh3.googleusercontent.com/ex-hf8FXJ4r1o64bEt_48AmDT-DBcpryXAFe1Ox-YONEMvtMui8nU-NSjUfaepyRGcWslsb4JBARSmrO=w2880-h1200-p-l90-rj'}], 'Indie': [{'name': 'Arctic Monkeys', 'id': 'UC8Yu1_yfN5qPh601Y4btsYw', 'img': 'https://lh3.googleusercontent.com/kbPRnnOmWPXIb35ygxKvXt2a_745AVUkAUeFMqOUxbKx8T_I0f1JUfK3G43-_xUldK16-KrU2cj43i0=w2880-h1200-p-l90-rj'}, {'name': 'The Strokes', 'id': 'UC8N13xhRG78YQK7Ppc4Ytrg', 'img': 'https://lh3.googleusercontent.com/QdxnTbXnfk-f0uP-7x9q2uYEkwNDLvDsEd7ViMBxB1jEIudgCUkxI7YGnZlL_IPdVRlgbOa1Mc4r6w=w2880-h1200-p-l90-rj'}, {'name': 'Vampire Weekend', 'id': 'UCWy-MPuAh_GH8YwXxtq3gcA', 'img': 'https://lh3.googleusercontent.com/G6i3GQh6D9Tvs6DXKsHcFwyt9ARfMuvmJEPd2mOUHO5C7WleJ_H_C6IBUnAXjEvMod7GEpWtxWFxrwr3=w2880-h1200-p-l90-rj'}, {'name': 'Tame Impala', 'id': 'UCGz-eguN8tcic5kUG4s1ZgA', 'img': 'https://lh3.googleusercontent.com/onR0ZnuFE6PwBeNwMiaTQHtz5vIbEIV8GJwDj8nEmOHuOvUj0efwFdAtXpfCOnpm-4GBl1IMgmtUNw=w2880-h1200-p-l90-rj'}, {'name': 'Florence + the Machine', 'id': 'UCkmCGbrGa7yNrRl_NHrOaTw', 'img': 'https://lh3.googleusercontent.com/Mrc6nBGklCHoToVgoBkPELexyPylNAVhhyiKFYTOr3DMLpr7BN3Wu4VEmfBnSSnpTgfOk0Lc-RYeUfQ=w2880-h1200-p-l90-rj'}, {'name': 'The Black Keys', 'id': 'UCchwuI134MUX4GSZqYLpYGA', 'img': 'https://lh3.googleusercontent.com/cFZdshYBDq6VPi3PnYlI1-fCDX1bjpAZdp72oJ7ei7Mat148giuYm69_eUCGlu4mLWLDimiu_tvKEw=w2880-h1200-p-l90-rj'}, {'name': 'The National', 'id': 'UC1bWXfKY5YoBduVCcSP8SGQ', 'img': 'https://lh3.googleusercontent.com/sHwv51eVKu9z7srQDK5-IqF0BNDtIjlSdX0PnOLOY5uaKo9i5GyZP7Y_A1I4ABRqGMd9wkrmB7kZ1sBx=w2880-h1200-p-l90-rj'}, {'name': 'Arcade Fire', 'id': 'UCXvAK640Ko85SLbI-zA0ZCg', 'img': 'https://lh3.googleusercontent.com/TiAcP19PlmxR3iIAQmSBwvIUE6i5SloddubTQBs2c1raALYpr7L6WaExvToQvvNMLkGZBVTEnEWqF-A=w2880-h1200-p-l90-rj'}, {'name': 'Death Cab for Cutie', 'id': 'UCQyYgbGkyvK3v3X1XzGDQ2Q', 'img': 'https://lh3.googleusercontent.com/yoMKWON2xhuOOzw9zCo83167GdGrwieaGxhGdFKXu-xGaTx0DCllkeLAkuDw8kglBSFDjKvM7_rsQE4=w2880-h1200-p-l90-rj'}, {'name': 'Mumford & Sons', 'id': 'UCJ3Q_kExh0ZZMMT05o0FXzA', 'img': 'https://lh3.googleusercontent.com/OQrSIGgnw4PO31fGCQB4nZpFfLjjM3DDhuOB58IbYebiQcMKC1WIWI600goDXX29WbOKM3S31MshXas=w2880-h1200-p-l90-rj'}], 'Rap': [{'name': 'Eminem', 'id': 'UCedvOgsKFzcK3hA5taf3KoQ', 'img': 'https://lh3.googleusercontent.com/P-rYd_7rYsYjsHg9LwlI-66FpHn3dCSSuoFof_cCf08LWFEfZe4h94-pKnEXvut926ouTf6QU6849Q=w2880-h1200-p-l90-rj'}, {'name': 'Kendrick Lamar', 'id': 'UCprAFmT0C6O4X0ToEXpeFTQ', 'img': 'https://lh3.googleusercontent.com/hMjzHmIuTV0XPlvRSjl3wMR6NP-uF-fqF6kkandkFX-hEVp6d3tw-FQG9_smAq0tFwNBT6QLQR-Hkwge=w2880-h1200-p-l90-rj'}, {'name': 'Drake', 'id': 'UCU6cE7pdJPc6DU2jSrKEsdQ', 'img': 'https://lh3.googleusercontent.com/MxNjcRJ-uK4Xvx7u90IhEFLQM8x9LIGTA9VCKHq5U4Wn2jOgiWaMtg-qz329SIzqnCyhdCCB3MpdAGs=w2880-h1200-p-l90-rj'}, {'name': 'JAY Z', 'id': 'UCbJG1HvzgzaMe_15xfiUyWw', 'img': 'https://lh3.googleusercontent.com/YcGJemFC30LtMjWCOMXUgjHhVknIUlxtgh6yBkEl1NA8ZHhih7VE4UrFqFqvwGPraXBr_EDvfbQ0ZkVi=w2880-h1200-p-l90-rj'}, {'name': 'Kanye West', 'id': 'UCRY5dYsbIN5TylSbd7gVnZg', 'img': 'https://lh3.googleusercontent.com/IFlc3sf6sHV3TAZ_5vhyHQiKb9D4AdSlDkiTSgsRiicnzLASXwVr1n22EEg6Vtd2XBlyJslm8xlYiA=w2880-h1200-p-l90-rj'}, {'name': 'Nicki Minaj', 'id': 'UCTTcTeAszDGxALRSMkJH9FQ', 'img': 'https://lh3.googleusercontent.com/dxazpVxrrUIWVdh49h3-GBhkgI5Wl2ALR5lI1AEldaVbUtz5TN4HfmL_ssUddy2ctEKcSPzNGeFOl-c=w2880-h1200-p-l90-rj'}, {'name': 'Cardi B', 'id': 'UCoIp9Cj1l7k63B90hFg38Zw', 'img': 'https://lh3.googleusercontent.com/EI0DGHwUprlB2Xc4XL0oKDgG_Dv2ejS5F8GaVIDV8w3Zehz14TGLqoTQwP7Am2buVJVJo9oJ1o8Szw=w2880-h1200-p-l90-rj'}, {'name': 'Lil Wayne', 'id': 'UC4IAZ3dowcXyvVYBx4hucSQ', 'img': 'https://lh3.googleusercontent.com/tpZlhvzqH9HPsXKBygEOKEWfw-KkU5zltB0kBazorZvUg_fvviQvcb3IG8DJfAW8tEVoqYu-8FhAQW0=w2880-h1200-p-l90-rj'}, {'name': 'Snoop Dogg', 'id': 'UC7xz_YipuZtypOuVALNzeog', 'img': 'https://lh3.googleusercontent.com/eWz33ayRvinYr30kQSi3aKeRedhY3_6-dNnOWUMNkaFlpB5DnljCB9fuPLjmN4_4dnhxyfLaw9HR7Mk=w2880-h1200-p-l90-rj'}, {'name': 'Travis Scott', 'id': 'UCf_gP4AMRSgAfyzbkeS9k4g', 'img': 'https://lh3.googleusercontent.com/r9k_FpAswxhQnl_cudiaT2ocWFccR6SzEFXgZ9a12iR5eDPSILlIL2EQewyQ-yYSt1JFyH1pqnoBXxs=w2880-h1200-p-l90-rj'}], 'EDM (Electronic Dance Music)': [{'name': 'Calvin Harris', 'id': 'UCZ0Aezmtk-S2l8A9Ln-2lKw', 'img': 'https://lh3.googleusercontent.com/8nNzlKW_I90sd-oiJoDpu54BaI2f4YF281SOTonEALOreg6xH4jtoQwR7duCPG7UJzhtOfRj9g=w2880-h1200-p-l90-rj'}, {'name': 'David Guetta', 'id': 'UCh-4c1ZoBPNP1C8c-7iVvUQ', 'img': 'https://lh3.googleusercontent.com/Nm_nq9JlS9WNx94meVL8AUgW-n7LzliJDYvWLrR-2ubFWQED1YQJKTv1AEV0s1gKiA3QKdY7lgimbFY=w2880-h1200-p-l90-rj'}, {'name': 'Avicii', 'id': 'UCuACQmW04T3v9Mz_1_suFYw', 'img': 'https://lh3.googleusercontent.com/TH3IXs5FL0GWk4BWPylXomZ_tUFV3sQQz8IaK1Hhw4sTTbFkCQlUXwAErsMvnoqjRxR5L1nXrsinYg=w2880-h1200-p-l90-rj'}, {'name': 'The Chainsmokers', 'id': 'UCQgUHOPJJrmzCjExg-ISupA', 'img': 'https://lh3.googleusercontent.com/gn1DZAeAiUs5vWpVaCLj9uFD5R75oTGkyqS8Otk_uVG5TIQB57foeLVac-DzoXIcXrLDmR8q9s6J5X4=w2880-h1200-p-l90-rj'}, {'name': 'Marshmello', 'id': 'UCrxpwXq8wCTskOQq5d_KoqQ', 'img': 'https://lh3.googleusercontent.com/FgXNumEMez1nb_08prkNDaGnKChcoTsxfe3dLBQ1bZoDFQ4X1pBnoTbZLeP28dWKkWYxOerVnamKag=w2880-h1200-p-l90-rj'}, {'name': 'Skrillex', 'id': 'UCibXKvuw5PoJVmyZJ4qhDIw', 'img': 'https://lh3.googleusercontent.com/KjyBsa4qngDl-OzeZdW25Kn0l7a3y2-iynPBpTZa5ECbIa_1xqiBWqV9AWcj-CR6mg0At0Kt-qnKIw=w2880-h1200-p-l90-rj'}, {'name': 'deadmau5', 'id': 'UCL44WZGVf-BU5N0ymCXrpBg', 'img': 'https://lh3.googleusercontent.com/Q7lfhLhSevtbi2_w7gEsrfI-zETEQVQndm5EE52VPAyztDSrEqIJ6Eb8cwTLbkIGpUuUq938MA=w2880-h1200-p-l90-rj'}, {'name': 'Zedd', 'id': 'UCGVGIqHPzwLhZg8KQNVaRbA', 'img': 'https://lh3.googleusercontent.com/GrjgqbE58IACC7-SZ-9miFgvtobauDqnOd5Dw9Z-kKXMwPkCio2PTen59hFadf0h8inUifhgbf5cPKY=w2880-h1200-p-l90-rj'}, {'name': 'Tiësto', 'id': 'UC8VSaPhuiHkjobAgNpRqLIA', 'img': 'https://lh3.googleusercontent.com/ix4H5SsMVKo9icIGURXBr0kO4Bt4F5HI29m1B9ubMk2tJ34GLn8nNWx6fpiHl5ABmdRCyfAlKYyWF7o=w2880-h1200-p-l90-rj'}, {'name': 'Martin Garrix', 'id': 'UCqJnSdHjKtfsrHi9aI-9d3g', 'img': 'https://lh3.googleusercontent.com/AH3ND2NEx2st2gddk-QC6qLH_rVnMs7vGhgB-ecC1KHgxtFjZEhOJvbFupxuNXtWPGVu0IlRAwF-hg=w2880-h1200-p-l90-rj'}]}
    random.shuffle(artists)
    response = make_response(render_template('home.html',artists=artists,genres=DATA_genres))
    return set_headers(response)

@app.route('/')
def player_page():
    response = make_response(render_template('main.html'))
    return set_headers(response)

@app.route('/edit_profile')
def edit_profilee():
    user_id = session['user']
    user_ref = db.collection('users').document(user_id)
    user_data = user_ref.get().to_dict()
    if 'userpfp_base64' in user_data:
        user_data['userpfp_data_url'] = f"data:image/jpeg;base64,{user_data['userpfp_base64']}"

    response = make_response(render_template('edit_profile.html', data=user_data))
    return set_headers(response)

@app.route('/firebase')
def firebase():
    try:
        return redirect(url_for('profile_page'))

    except Exception:
        response = make_response(render_template('firebase.html'))
        return set_headers(response)
@app.route('/api/v2/update_profile', methods=['POST'])
@app.route('/api/v2/update_profile', methods=['POST'])
def update_profile():
    if 'user' not in session:
        return "User not authenticated", 401
    
    user_id = session['user']
    username = request.form.get('username')
    userbio = request.form.get('userbio')
    userpronoun = request.form.get('userpronoun')

    try:
        userpfp = request.files['userpfp']
    except KeyError:
        userpfp = None
    
    user_data = {
        'username': username,
        'userbio': userbio,
        'userpronoun': userpronoun,
    }

    if userpfp:
        userpfp_base64 = base64.b64encode(userpfp.read()).decode('utf-8')
        user_data['userpfp_base64'] = userpfp_base64

        
    user_ref = db.collection('users').document(user_id)
    user_ref.set(user_data, merge=True)

    return "successful"


@app.route('/profile')
def profile_page():
    try:
        user_id = session['user']
        user_ref = db.collection('users').document(user_id)
        user_data = user_ref.get().to_dict()
        if user_data['userpfp_base64']!=None:
            user_data['userpfp_data_url'] = f"data:image/jpeg;base64,{user_data['userpfp_base64']}"
        else:
            user_data['userpfp_data_url'] ='blabla'
        return render_template('profile.html', data=user_data)
    except Exception as E:
        print(E)
        response = make_response(render_template('firebase.html'))
        return set_headers(response)


@app.route('/api/v2/logout')
def logout():
    session.clear()
    print('done')
    return "done"
@app.route('/api/v2/like_song', methods=['POST'])
def like_song():
    user_id = session['user']
    request_data = request.get_json()
    songid = request_data['songid']
    img = request_data['img']
    title = request_data['title']
    artist = request_data['artist']
    liked_songs_ref = db.collection('users').document(user_id).collection('likedSongs')
    query = liked_songs_ref.where('song_id', '==', songid)
    liked_song_docs = query.get()
    if liked_song_docs:
        for liked_song_doc in liked_song_docs:
            liked_song_doc.reference.delete()
        response_text = "UNLIKED"
    else:
        liked_songs_ref.add({
            'song_id': songid,
            'img':img,
            'title':title,
            'artist':artist,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
        response_text = "LIKED"
    
    return {"text": response_text}

@app.route('/api/v2//signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.create_user(email=email, password=password)
        user = auth.get_user_by_email(email)
        session['user'] = user.uid
        user_data = {'username': "default_username123",'userbio': "Hey there i'm new to this app",'userpronoun': "Not Set","userpfp_base64":""}

        user_ref = db.collection('users').document(session['user'])
        user_ref.set(user_data, merge=True)
        return redirect(url_for('home_page'))
    except Exception as e:
        return str(e)
@app.route('/api/v2/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.get_user_by_email(email)
        session['user'] = user.uid
        return redirect(url_for('home_page'))
    except Exception as e:
        return str(e)

@app.route('/artist/<artistid>')
def artist_page(artistid):
    raw_data = ytmusic.get_artist(artistid)
    ARTIST_data = {'streams':raw_data['views'],"related":raw_data['related'],"albums":raw_data['albums'],"videos":raw_data['videos'],"songs":raw_data['songs'], "id":raw_data['channelId'],'bio':raw_data['description'], 'name':raw_data['name'],'img':raw_data['thumbnails'][0]['url'].split("=w")[0] +"=w2880-h1200-p-l90-rj"}
    response = make_response(render_template('artist.html', data=ARTIST_data))
    return set_headers(response)

@app.route('/album/<albumid>')
def album_page(albumid):
    album_data = ytmusic.get_album(albumid)
    user_id = session['user']
    liked_songs_ref = db.collection('users').document(user_id).collection('likedSongs')
    liked_songs = liked_songs_ref.stream()
    liked_song_ids = [song.get('song_id') for song in liked_songs]
    for song in album_data['tracks']:
        song['variable'] = song['videoId'].replace("-","__hyphen__")
        if song['videoId'] in liked_song_ids:
            song['liked'] = True
        else:
            song['liked'] = False
    
    response = make_response(render_template('album.html', data=album_data))
    return set_headers(response)
@app.route('/liked')        
def playlist_page():
    try:
        user_id = session['user']
        print("yoyoyo")
        liked_songs_ref = db.collection('users').document(user_id).collection('likedSongs')
        liked_songs = liked_songs_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).get()
        print("yoyoyo")
        songs_list = []
        for song in liked_songs:
            song_data = song.to_dict()
            song_data['liked'] =True
            song_data['variable'] = song_data['song_id'].replace("-","__hyphen__")
            songs_list.append(song_data)

        response = make_response(render_template('playlist.html', data=songs_list,length_data=len(songs_list)))
        return set_headers(response)
    except Exception:
        response = make_response(render_template('firebase.html'))
        return set_headers(response)




@app.route('/quiz/<quiz_id>')
def quiz_page(quiz_id):
    print(quiz_id)
    raw_data = ytmusic.get_artist(quiz_id)
    DATA_artist = {'name':raw_data['name'],'id':quiz_id,'img':raw_data['thumbnails'][0]['url'].split("=w")[0] +"=w2880-h1200-p-l90-rj", "bio":raw_data['description']}
    dataset = get_quiz_data(raw_data, 2023)
    response = make_response(render_template('game.html',dataset=dataset,DATA_artist=DATA_artist))
    return set_headers(response)



@app.route('/api/music/<artist_id>')
def get_music(artist_id):
    raw_data = ytmusic.get_artist(artist_id)
    song_data = (raw_data['songs']['results'])
    def get_audio_data(song_data):
        audio_data=[]
        def audio_url(video_id,title, img):
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream_url = audio_stream.url
            audio_data.append((title,audio_stream_url, img))
        threads = []
        for x in song_data:
            video_id = x['videoId']
            t = threading.Thread(target=audio_url, args=(video_id,x['title'],x['thumbnails'][0]['url'].split("=w")[0] +"=w1200-h1200-p-l90-rj"))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        return(audio_data)
    return(get_audio_data(song_data))


@app.route('/api/mp3/<song_id>')
def get_mp3url(song_id):
    video_url = f"https://www.youtube.com/watch?v={song_id}"
    yt = YouTube(video_url)
    watch_data = ytmusic.get_watch_playlist(song_id)
    try:
        lyrics = ytmusic.get_lyrics(watch_data['lyrics'])['lyrics'].split('\n')
    except Exception:
        lyrics = ['Woah ;) You Caught Us', "Lyrics of this song will be added soon!"]
    audio_stream = yt.streams.get_highest_resolution()
    audio_stream_url = audio_stream.url
    print(audio_stream_url)
    return ({"url":audio_stream_url,'lyrics':lyrics})

@app.route('/api/search/<query>')
def search_artist(query):
    data = ytmusic.search(query)
    print("\n\n\n\n\n", data)
    return data

@app.route('/api/karoake/<song_id>')
def get_karoake(song_id):
    watch_data = song_id.split("||")
    def get_karoake(song_name, artist_name):
        from youtubesearchpython import VideosSearch
        videosSearch = VideosSearch(f'singkingkaraoke {song_name} {artist_name}', limit = 1)
        data = (videosSearch.result())['result'][0]
        if data['channel']['name'] == "Sing King":
            title = (data['title'])
            if song_name.lower() in title.lower() or artist_name.lower() in title.lower(): 
                video_url = f"https://www.youtube.com/watch?v={data['id']}"
                yt = YouTube(video_url)
                audio_stream = yt.streams.get_highest_resolution()
                audio_stream_url = audio_stream.url
                return audio_stream_url
            else:
                print("not available")
    data = get_karoake(song_name=watch_data[0],artist_name=watch_data[1])
    print(data)
    return data


app.run(host="0.0.0.0", port=2011, debug=True)