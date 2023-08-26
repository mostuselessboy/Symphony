import random
from ytmusicapi import YTMusic
ytmusic = YTMusic()
import pickle

def load_cache(target, ID):
	target_file = f'{target}_dataset.json'
	file = open(target_file, 'rb')
	data = pickle.load(file)
	file.close()
	if ID in data:
		return data[ID]
	return None
def set_cache(target, ID, raw_data):
	target_file = f'{target}_dataset.json'
	file = open(target_file, 'rb')
	data = pickle.load(file)
	file.close()
	file = open(target_file, 'wb')
	data[ID] =raw_data
	pickle.dump(data, file)
	file.close()
	print("DATA UPLOADED TO CACHE MEMORY")



raw_data = {'description': 'ZAYN is a multi-platinum selling recording artist, producer, and philanthropist known for his skyscraping vocals and hybrid style of pop and R&B. He became the first UK Male Solo artist to simultaneously chart at #1 on the UK and US album charts in the first week of release for his record-breaking debut album Mind of Mine (2016). The album’s lead single, “Pillowtalk,” hit #1 in 68 countries around the world and has since been certified 5x platinum by the RIAA. The album was followed by his gold certified Icarus Falls (2018), and critically acclaimed Nobody is Listening (2021). \n \nThe UK native’s influence spans beyond just music into the fashion world, where ZAYN has collaborated on capsule collections with the likes of Giuseppe Zanotti and Versus Versace, and covered numerous fashion publications including Vogue, GQ, ELLE UK, Highsnobiety, PAPER, The FADER and more. ZAYN has garnered several accolades throughout his career including a Billboard Music Award, American Music Award, MTV VMA, two Brit Award nominations, and was named “Most Stylish Man” at the British GQ Men of the Year Awards.\n \nIn addition to his music ZAYN continues to be a voice for positive change most recently advocating for free school lunches for children living in poverty in the UK.\n \nZAYN is currently working on his highly anticipated fourth studio album.', 'views': '4,960,698,344 views', 'name': 'ZAYN', 'channelId': 'UC3PdiRW5dUA4V70ueeR1eHA', 'shuffleId': None, 'radioId': None, 'subscribers': '15.5M', 'subscribed': False, 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/x_OLwEjNh74QScfVbc3ejrbxjjG3WFe5CfVrO9KlIT_W2VvHpVC-orFzg-LF2kVYsBGK2YOA5JvUsVE=w540-h225-p-l90-rj', 'width': 540, 'height': 225}, {'url': 'https://lh3.googleusercontent.com/x_OLwEjNh74QScfVbc3ejrbxjjG3WFe5CfVrO9KlIT_W2VvHpVC-orFzg-LF2kVYsBGK2YOA5JvUsVE=w816-h340-p-l90-rj', 'width': 816, 'height': 340}, {'url': 'https://lh3.googleusercontent.com/x_OLwEjNh74QScfVbc3ejrbxjjG3WFe5CfVrO9KlIT_W2VvHpVC-orFzg-LF2kVYsBGK2YOA5JvUsVE=w1440-h600-p-l90-rj', 'width': 1440, 'height': 600}, {'url': 'https://lh3.googleusercontent.com/x_OLwEjNh74QScfVbc3ejrbxjjG3WFe5CfVrO9KlIT_W2VvHpVC-orFzg-LF2kVYsBGK2YOA5JvUsVE=w1920-h800-p-l90-rj', 'width': 1920, 'height': 800}, {'url': 'https://lh3.googleusercontent.com/x_OLwEjNh74QScfVbc3ejrbxjjG3WFe5CfVrO9KlIT_W2VvHpVC-orFzg-LF2kVYsBGK2YOA5JvUsVE=w2880-h1200-p-l90-rj', 'width': 2880, 'height': 1200}], 'songs': {'browseId': 'VLOLAK5uy_l0VQ-p-TR4N0rpnWeD6yVFtTJS8FBtEYY', 'results': [{'videoId': 'j-0kLu3O7qU', 'title': 'Dusk Till Dawn (Radio Edit) (feat. Sia)', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'album': {'name': 'Icarus Falls', 'id': 'MPREb_wrmB5yea69o'}, 'likeStatus': 'INDIFFERENT', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/AvqIJA_NYHB8sqmaP4PKAbfyODNe_trM4QXEY1TYpEASi2NWcK19LSiuoSYTORUR8-iHrj9vvdGwqIs=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/AvqIJA_NYHB8sqmaP4PKAbfyODNe_trM4QXEY1TYpEASi2NWcK19LSiuoSYTORUR8-iHrj9vvdGwqIs=w120-h120-l90-rj', 'width': 120, 'height': 120}], 'isAvailable': True, 'isExplicit': False, 'videoType': 'MUSIC_VIDEO_TYPE_ATV'}, {'videoId': 'J2dqEK7pdBQ', 'title': 'I Don’t Wanna Live Forever (Fifty Shades Darker)', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}, {'name': 'Taylor Swift', 'id': 'UCPC0L1d253x-KuMNwa05TpA'}], 'album': {'name': 'Fifty Shades Darker (Original Motion Picture Soundtrack)', 'id': 'MPREb_0hEQfqUtf1D'}, 'likeStatus': 'INDIFFERENT', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/yf-ILe_eg5gMCQOccrKP7dVmSGBHw2ZHpgIQ_cX5kSAWMjYdHQzn03gVvBS04pqrCbTTDzMTFPz-6Gta=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/yf-ILe_eg5gMCQOccrKP7dVmSGBHw2ZHpgIQ_cX5kSAWMjYdHQzn03gVvBS04pqrCbTTDzMTFPz-6Gta=w120-h120-l90-rj', 'width': 120, 'height': 120}], 'isAvailable': True, 'isExplicit': False, 'videoType': 'MUSIC_VIDEO_TYPE_ATV'}, {'videoId': 'fSKtPBRV1gE', 'title': 'PILLOWTALK', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'album': {'name': 'Mind Of Mine (Deluxe Edition)', 'id': 'MPREb_qMYFJBrkR7e'}, 'likeStatus': 'INDIFFERENT', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/eAf4vUXn6VXtIkVPmHEvO88PxBOMzVTlLMfT33-5wtIxcHtcQyRMhoTMk_UFyOLYRxu_7jEs1jrQWuY=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/eAf4vUXn6VXtIkVPmHEvO88PxBOMzVTlLMfT33-5wtIxcHtcQyRMhoTMk_UFyOLYRxu_7jEs1jrQWuY=w120-h120-l90-rj', 'width': 120, 'height': 120}], 'isAvailable': True, 'isExplicit': True, 'videoType': 'MUSIC_VIDEO_TYPE_ATV'}, {'videoId': 'zm0JkbbnExo', 'title': 'Love Like This', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'album': {'name': 'Love Like This', 'id': 'MPREb_9Ie3ank0bx3'}, 'likeStatus': 'INDIFFERENT', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/kYmV4EWLMckRHIzTH2MF3HiF8PVR3ZU7kc-BNL9qP3yS8dFS9HO12NWA_pit9JfKYcT4AhQC5v801S0=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/kYmV4EWLMckRHIzTH2MF3HiF8PVR3ZU7kc-BNL9qP3yS8dFS9HO12NWA_pit9JfKYcT4AhQC5v801S0=w120-h120-l90-rj', 'width': 120, 'height': 120}], 'isAvailable': True, 'isExplicit': False, 'videoType': 'MUSIC_VIDEO_TYPE_ATV'}, {'videoId': 'EqDK225zfwk', 'title': 'A Whole New World (End Title) (From "Aladdin")', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}, {'name': 'Zhavia Ward', 'id': 'UCHKXAipxSAksBqKHgJQbs9g'}], 'album': {'name': 'A Whole New World (End Title) (From "Aladdin")', 'id': 'MPREb_sEfyYhncpFy'}, 'likeStatus': 'INDIFFERENT', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/82oQjlr50o24sobE6cX8_rxm154dCvp9jO65VTa-w2tCkxVmgFclRY0rgGhtctPfIK_RpCbjb2uBcXI=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/82oQjlr50o24sobE6cX8_rxm154dCvp9jO65VTa-w2tCkxVmgFclRY0rgGhtctPfIK_RpCbjb2uBcXI=w120-h120-l90-rj', 'width': 120, 'height': 120}], 'isAvailable': True, 'isExplicit': False, 'videoType': 'MUSIC_VIDEO_TYPE_ATV'}]}, 'albums': {'browseId': None, 'results': [{'title': 'Nobody Is Listening', 'year': '2021', 'browseId': 'MPREb_yBfArTfD29k', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/OnCNTgET0C00Ng0sqZihWyHko_23sxIxl7VhVhGXn66Thyt66S5boRbp0_h-fduZVoL-DlRcFe_JKVEt=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/OnCNTgET0C00Ng0sqZihWyHko_23sxIxl7VhVhGXn66Thyt66S5boRbp0_h-fduZVoL-DlRcFe_JKVEt=w544-h544-l90-rj', 'width': 544, 'height': 544}], 'isExplicit': True}, {'title': 'Icarus Falls', 'year': '2018', 'browseId': 'MPREb_Wuq9d5xZV2j', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/lDiOUvDWRfVzrQD9q8lCYahgAnvo1pX9HZOrqRll2zbKQPXd84qE1i3Os6buade3GqSAPFzlcnMx3hNPjw=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/lDiOUvDWRfVzrQD9q8lCYahgAnvo1pX9HZOrqRll2zbKQPXd84qE1i3Os6buade3GqSAPFzlcnMx3hNPjw=w544-h544-l90-rj', 'width': 544, 'height': 544}], 'isExplicit': True}, {'title': 'Mind Of Mine (Deluxe Edition)', 'year': '2016', 'browseId': 'MPREb_qMYFJBrkR7e', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/eAf4vUXn6VXtIkVPmHEvO88PxBOMzVTlLMfT33-5wtIxcHtcQyRMhoTMk_UFyOLYRxu_7jEs1jrQWuY=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/eAf4vUXn6VXtIkVPmHEvO88PxBOMzVTlLMfT33-5wtIxcHtcQyRMhoTMk_UFyOLYRxu_7jEs1jrQWuY=w544-h544-l90-rj', 'width': 544, 'height': 544}], 'isExplicit': True}]}, 'singles': {'browseId': 'UCYR9erHSNBPjjNswR4FrMaw', 'results': [{'title': 'Love Like This', 'year': '2023', 'browseId': 'MPREb_9Ie3ank0bx3', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/kYmV4EWLMckRHIzTH2MF3HiF8PVR3ZU7kc-BNL9qP3yS8dFS9HO12NWA_pit9JfKYcT4AhQC5v801S0=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/kYmV4EWLMckRHIzTH2MF3HiF8PVR3ZU7kc-BNL9qP3yS8dFS9HO12NWA_pit9JfKYcT4AhQC5v801S0=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Angel', 'year': '2022', 'browseId': 'MPREb_2ZBvGZ8qVil', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/dviPqQcy_ael8AoWqPldRCGYtW25MOgneUuvtRFLQssmjE9WcVvnF8IaUuvKFHKkU_5p1eKQu60qtH6cTA=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/dviPqQcy_ael8AoWqPldRCGYtW25MOgneUuvtRFLQssmjE9WcVvnF8IaUuvKFHKkU_5p1eKQu60qtH6cTA=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'To Begin Again', 'year': '2021', 'browseId': 'MPREb_9MVzbmVng4L', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/zXxPMGg7cE-BgL3zLLerjQG-PTQqb_3-WNLxm3x52ba2MuUFQySa_tPArCb1qsfjxGwY8iNguoD4F_jo=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/zXxPMGg7cE-BgL3zLLerjQG-PTQqb_3-WNLxm3x52ba2MuUFQySa_tPArCb1qsfjxGwY8iNguoD4F_jo=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Vibez', 'year': '2021', 'browseId': 'MPREb_KqSY0oGxCqs', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/WlAk6WYi0E-HRiPQuUD-n_1hyO3NoCqnxZXIwH9vc8frhLHIPTxUimH7IeTK_YSK6K62y89E-3DUFEM=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/WlAk6WYi0E-HRiPQuUD-n_1hyO3NoCqnxZXIwH9vc8frhLHIPTxUimH7IeTK_YSK6K62y89E-3DUFEM=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Better', 'year': '2020', 'browseId': 'MPREb_x6iGgRWQa98', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/wP7WlEZbpUFGVABMyTv4Di4AdtcSq3LUNzOxDPtnnA-lOdXbTamqG5iNNfNa76N8F47xQVsNSe839WbdLg=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/wP7WlEZbpUFGVABMyTv4Di4AdtcSq3LUNzOxDPtnnA-lOdXbTamqG5iNNfNa76N8F47xQVsNSe839WbdLg=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Flames (The EP)', 'year': '2020', 'browseId': 'MPREb_L1GnA4QIS7N', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/Eu78qd5dsP6CctFvDSGeSVPC7NqUzlUrR-K103Cob9DJHard-8EKjaag9H2ulb9RqR87QBKgTJP64VOcBA=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/Eu78qd5dsP6CctFvDSGeSVPC7NqUzlUrR-K103Cob9DJHard-8EKjaag9H2ulb9RqR87QBKgTJP64VOcBA=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Flames (R3HAB & Skytech VIP Remix)', 'year': '2019', 'browseId': 'MPREb_XoUOmQ9BC42', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/PltfKdYHbH5Ka8IMLhrQ-pU7CTUvA2QJOmzvVBKF995-7Fm3KanXXomsz_msiSdjbBlEBq8MxnYXJtu9jw=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/PltfKdYHbH5Ka8IMLhrQ-pU7CTUvA2QJOmzvVBKF995-7Fm3KanXXomsz_msiSdjbBlEBq8MxnYXJtu9jw=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'A Whole New World (End Title) (From "Aladdin")', 'year': '2019', 'browseId': 'MPREb_sEfyYhncpFy', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/82oQjlr50o24sobE6cX8_rxm154dCvp9jO65VTa-w2tCkxVmgFclRY0rgGhtctPfIK_RpCbjb2uBcXI=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/82oQjlr50o24sobE6cX8_rxm154dCvp9jO65VTa-w2tCkxVmgFclRY0rgGhtctPfIK_RpCbjb2uBcXI=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Trampoline (Joel Corry Remix)', 'year': '2018', 'browseId': 'MPREb_gYOlZtRa4BH', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/xetPFS8HmpvezZ8SoJnn274CRoSdfLErdnEBu2UCX7N2r-kZa9aiudLc5r98F5tWwYHFY0ctu5Ky1RU=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/xetPFS8HmpvezZ8SoJnn274CRoSdfLErdnEBu2UCX7N2r-kZa9aiudLc5r98F5tWwYHFY0ctu5Ky1RU=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Trampoline', 'year': '2018', 'browseId': 'MPREb_gNSquZABhoX', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/6-fo0Gqk6ajRkzX6dUEpixL6IWG2B6pBgyDAc6_b44BLjcv3Zmkj5OmyDveMxf67tdndq6wLDZEWUYamNw=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/6-fo0Gqk6ajRkzX6dUEpixL6IWG2B6pBgyDAc6_b44BLjcv3Zmkj5OmyDveMxf67tdndq6wLDZEWUYamNw=w544-h544-l90-rj', 'width': 544, 'height': 544}]}], 'params': '6gPgAUdxVUJXcFlCQ3BNQkNpUjVkRjl3WVdkbFgzTnVZWEJ6YUc5MFgyMTFjMmxqWDNCaFoyVmZjbVZuYVc5dVlXd1NIMUY2Y1RkZk5raERObFZWVjAxSlYwVkxTa3d6Y1MxQ01HRnRhblp2UW1jYVNnQUFaVzRBQVVsT0FBRkpUZ0FCQUVaRmJYVnphV05mWkdWMFlXbHNYMkZ5ZEdsemRBQUJBVU1BQUFFQUFBRUJBRlZEV1ZJNVpYSklVMDVDVUdwcVRuTjNValJHY2sxaGR3QUI4dHF6cWdvR1FBSklBRkFV'}, 'videos': {'browseId': 'VLOLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'results': [{'title': 'Love Like This', 'videoId': 'hXi3bGdl4ao', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/hXi3bGdl4ao/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3n0q63p4zmiXYS0dJeNoPyfB6q6mQ', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/hXi3bGdl4ao/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3mU-_w9hW7pVeqd0Pjp97vGuAyGGQ', 'width': 800, 'height': 450}], 'views': '513K'}, {'title': 'Dusk Till Dawn (Official Video) (feat. Sia)', 'videoId': 'tt2k8PGm-TI', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/tt2k8PGm-TI/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3kWHMgtOThe-O1V88toWbxjtUtVhw', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/tt2k8PGm-TI/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3mKrb9HziJcPZwOnkx4Qt62GzVJtA', 'width': 800, 'height': 450}], 'views': '2B'}, {'title': 'I Don’t Wanna Live Forever (Fifty Shades Darker) (From "Fifty Shades Darker (Original Motion Picture Soundtrack)")', 'videoId': 'AY9blLYMKnI', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}, {'name': 'Taylor Swift', 'id': 'UCPC0L1d253x-KuMNwa05TpA'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/AY9blLYMKnI/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3mQoOJocGSpOP7dlAf0zfGZaEzhkw', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/AY9blLYMKnI/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3lgeQS25PTWwwV2sHuctIfvUB89IA', 'width': 800, 'height': 450}], 'views': '182M'}, {'title': 'PILLOWTALK', 'videoId': 'C_3d6GntKbk', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/C_3d6GntKbk/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3lELW5ymgbhCfdlIM0xrsCPZCXlvg', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/C_3d6GntKbk/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3lT1O5dUsfXvS8Vp9t9As_ft8WImA', 'width': 800, 'height': 450}], 'views': '1.1B'}, {'title': 'Let Me', 'videoId': 'J-dv_DcDD_A', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/J-dv_DcDD_A/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3nGLCIVL12EY9KuqU2ATAszs2FNLQ', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/J-dv_DcDD_A/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3mdRbB4bxB6g65q1wjfJQS8IOlwxA', 'width': 800, 'height': 450}], 'views': '209M'}, {'title': 'Entertainer', 'videoId': 'voG07pt-KYI', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/voG07pt-KYI/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3kxieUCf3UyVl3OJtcx1pWDmoFUBg', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/voG07pt-KYI/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3mQjY_rYlZ04ILatiLTrLUxjPkzMA', 'width': 800, 'height': 450}], 'views': '94M'}, {'title': 'LIKE I WOULD', 'videoId': 'pTaqcGz2O5o', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/pTaqcGz2O5o/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3mXFMKbb0UEjlSdoNdp7swX3Nx3qQ', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/pTaqcGz2O5o/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3lr5Jve768fhNeQaQPHTHbz6McVRQ', 'width': 800, 'height': 450}], 'views': '85M'}, {'title': 'Better', 'videoId': 'NAo38Q9c4xA', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/NAo38Q9c4xA/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3lfOAfmQ8TrsRLq2wzaPmwUnC1QiA', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/NAo38Q9c4xA/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3k4wz2sADeSivzTjzf6UzobADaRlg', 'width': 800, 'height': 450}], 'views': '44M'}, {'title': 'Vibez', 'videoId': 'VSpgaN3wuag', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/VSpgaN3wuag/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3ki1Bf5jvFBHaDfB3tabbRrh4jylw', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/VSpgaN3wuag/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3mGnWF9XDAr4C8ph31qtVFJFRjttg', 'width': 800, 'height': 450}], 'views': '41M'}, {'title': 'There You Are', 'videoId': 'eFsGA0GXB-8', 'artists': [{'name': 'ZAYN', 'id': 'UCYR9erHSNBPjjNswR4FrMaw'}], 'playlistId': 'OLAK5uy_k6HYsvrDkPhV8-HCTbQSbUt6AosuY7S3I', 'thumbnails': [{'url': 'https://i.ytimg.com/vi/eFsGA0GXB-8/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3l8MpAe9q6XkpW7V64hsnC4t_w-4g', 'width': 400, 'height': 225}, {'url': 'https://i.ytimg.com/vi/eFsGA0GXB-8/hq720.jpg?sqp=-oaymwEXCKAGEMIDIAQqCwjVARCqCBh4INgESFo&rs=AMzJL3n2Zvob0MLaXNbcB-ce5BbceGXNMg', 'width': 800, 'height': 450}], 'views': '19M'}]}, 'related': {'browseId': None, 'results': [{'title': 'Shawn Mendes', 'browseId': 'UC6ZjlLJhqP79nqGr3Ic6Adg', 'subscribers': '30M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/4EsDMeFPd5Ms9hW7MCYaJ1172CO08yEEJ8clrkpjdSUuZDR6fljAjLfQVo7Ut-j32bQqmCrZJpSmulM=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/4EsDMeFPd5Ms9hW7MCYaJ1172CO08yEEJ8clrkpjdSUuZDR6fljAjLfQVo7Ut-j32bQqmCrZJpSmulM=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Liam Payne', 'browseId': 'UCEcGHupZkoAPFXXQrC2W8rA', 'subscribers': '3.76M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/TsvzynOHJaqZtZIWPknYyR6c379FoTN-ikS4BrKRyP49eMUSc2mKKjrS4ZY3hWPAlV5ly8MxCWasymI=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/TsvzynOHJaqZtZIWPknYyR6c379FoTN-ikS4BrKRyP49eMUSc2mKKjrS4ZY3hWPAlV5ly8MxCWasymI=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Niall Horan', 'browseId': 'UCxm9sS8Dd2aRthr_O3rVLJQ', 'subscribers': '4.62M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/Q8m4YJu7QtmEpWZQUCRI596T7QnGSkmOwKOLRgIKNjfVBsrQKwokX-kYEaDbOwWmGcoV288Vav_JVw=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/Q8m4YJu7QtmEpWZQUCRI596T7QnGSkmOwKOLRgIKNjfVBsrQKwokX-kYEaDbOwWmGcoV288Vav_JVw=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Justin Bieber', 'browseId': 'UCGvj8kfUV5Q6lzECIrGY19g', 'subscribers': '71.8M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/iVttpMqOcjor_Rt64WqL0iB8YJ3At97IGNer6qzhYQ7ffoqzVL7pEmxJXmItcZ2Sj_aRT_dewAg1ORg=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/iVttpMqOcjor_Rt64WqL0iB8YJ3At97IGNer6qzhYQ7ffoqzVL7pEmxJXmItcZ2Sj_aRT_dewAg1ORg=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Camila Cabello', 'browseId': 'UCsZIVNwBqtPBX-41kO_rQzQ', 'subscribers': '16.3M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/l6PqT6Wwyjv6V2H2scGgD0tXMtD-UHN39SF9Ey_pKMtpfxvSoyo2QwZzCbjzbwJlJj9MH0AilgbXf_A=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/l6PqT6Wwyjv6V2H2scGgD0tXMtD-UHN39SF9Ey_pKMtpfxvSoyo2QwZzCbjzbwJlJj9MH0AilgbXf_A=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Khalid', 'browseId': 'UCnfeNQJ7TgUCPCBD0q5Zh-Q', 'subscribers': '9.41M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/a-/AD_cMMTE_oO14aOxctl1x2zXEphZ-xe1A3sfc0-Zu76x79mdtg=w226-h226-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/a-/AD_cMMTE_oO14aOxctl1x2zXEphZ-xe1A3sfc0-Zu76x79mdtg=w544-h544-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Nick Jonas', 'browseId': 'UCAD0nONt_CXY913TBm3jqIQ', 'subscribers': '3.94M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/V5ksj6uaibgp0G43YaBf0bkcoZXvQVSaVnNzLVnxDoW-8Qn31q4j6SGq_OdXPRZb39JLnsmkDmvJziBF=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/V5ksj6uaibgp0G43YaBf0bkcoZXvQVSaVnNzLVnxDoW-8Qn31q4j6SGq_OdXPRZb39JLnsmkDmvJziBF=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Julia Michaels', 'browseId': 'UC-bE9kenHs2wN-p96ESCFIg', 'subscribers': '1.77M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/bVcp00-VmU6hOCtvHLlwqo49DU55x4vAOsoATi-swu6fygZnWbbVPLlGK1tvvDpoadXkF8Cq8fn_VWI=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/bVcp00-VmU6hOCtvHLlwqo49DU55x4vAOsoATi-swu6fygZnWbbVPLlGK1tvvDpoadXkF8Cq8fn_VWI=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Bazzi', 'browseId': 'UCoBD_yd06t7kBn1wLGH7nzg', 'subscribers': '3.23M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/AAN8alR77fRcJjBJrhCKKAQsqdYAOy8jpvVnZU8aLhZ-zPq5DKq3jfijgOlirAvmQJVwAtF4ro8wdw=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/AAN8alR77fRcJjBJrhCKKAQsqdYAOy8jpvVnZU8aLhZ-zPq5DKq3jfijgOlirAvmQJVwAtF4ro8wdw=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}, {'title': 'Hailee Steinfeld', 'browseId': 'UCBNeAoPycNhoRuS01B9Kf5g', 'subscribers': '4.52M', 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/SQglPDFeiL9N2fKlNlkIM_OI1mMMyy2tgeP5iwcdFdqgG6NmdNLyaOmNRlM5N-OJ_ax4flVCpSBo9i32=w226-h226-p-l90-rj', 'width': 226, 'height': 226}, {'url': 'https://lh3.googleusercontent.com/SQglPDFeiL9N2fKlNlkIM_OI1mMMyy2tgeP5iwcdFdqgG6NmdNLyaOmNRlM5N-OJ_ax4flVCpSBo9i32=w544-h544-p-l90-rj', 'width': 544, 'height': 544}]}]}}
current_year = 2023
def get_quiz_data(raw_data, current_year):
	def album_count(data):
		option = []
		album_count = (len(data['albums']['results']))
		option.append(album_count)
		x = 0
		while x!=3:
			operation = ["+", "-"]
			random.shuffle(operation)
			if operation[0] == "+":
				rnd = album_count+random.randint(1,6)
				if rnd not in option:
					option.append(rnd)
					x=x+1
			if operation[0] == "-":
				rnd = album_count-random.randint(1,6)
				if rnd not in option and rnd>0:
					option.append(rnd)
					x=x+1
		answer = option[0]
		random.shuffle(option)            
		return(f"How many {data['name']}'s Albums are there?", list(map(str, option)),answer)

	data_set = [album_count(raw_data)]
	def album_year(data,current_year):
		albums= (data['albums']['results'])
		questions = []
		for album in albums:
			option = []
			album_year = int(album['year'])
			option.append(album_year)
			x = 0
			while x!=3:
				operation = ["+", "-"]
				random.shuffle(operation)
				if operation[0] == "+":
					rnd = album_year+random.randint(1,10)
					if rnd not in option and rnd<current_year:
						option.append(rnd)
						x=x+1
				if operation[0] == "-":
					rnd = album_year-random.randint(1,10)
					if rnd not in option:
						option.append(rnd)
						x=x+1
			answer = option[0]
			random.shuffle(option)   
			questions.append((f"In what year '{album['title']}' Album was released?", list(map(str, option)), answer))
		return questions
	data_set.extend(album_year(raw_data, current_year))
	def album_songs(data):
		albums= (data['albums']['results'])
		questions = []
		for x in range(5):
			album_dict = {}
			for album in albums:
				raw_data = load_cache('album', album['browseId'])
				if not raw_data:
					raw_data = ytmusic.get_album(album['browseId'])
					set_cache('album', album['browseId'], raw_data)
				songs = [x['title'] for x in (raw_data['tracks'])]
				album_dict[album['title']] = (songs)
			set1 = []
			for item in album_dict:
				list_album = album_dict[item]
				random.shuffle(list_album)
				set1.append((list_album[0] , item))
			for item in (set1):
				list_set1 = list((album_dict.keys()))
				list_set1.remove(item[1])
				random.shuffle(list_set1)
				list2_set1 = (album_dict[list_set1[0]])
				random.shuffle(list2_set1)
				list3_set1 = list2_set1[:3]
				list3_set1.insert( 0,item[0])
				option = (list3_set1)
				rnd = random.randint(0,1)
				answer = option[0]
				random.shuffle(option)   
				if rnd ==1:
					questions.append((f"Which of the song is not from '{list_set1[0]}' Album?", list(map(str, option)),answer))
				else:
					questions.append((f"Which of the song is from '{item[1]}' Album?", list(map(str, option)),answer))

		return questions
	data_set.extend(album_songs(raw_data))
	random.shuffle(data_set)
	return(data_set)
