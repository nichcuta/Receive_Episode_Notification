from imdbpie import Imdb
import datetime


def receive_episodes(ep_no):
    try:
        global to_download
        imdb = Imdb()
        z = imdb.get_episodes(ep_no)
        for item in z:
            if item.release_date == yesterday:
                if item.season < 10:
                    season = "0" + str(item.season)
                else:
                    season = str(item.season)
                if item.episode < 10:
                    ep = "0" + str(item.episode)
                else:
                    ep = str(item.episode)
                new_item = item.series_name + ' s' + season + 'e' + ep + '\n'
                to_download = to_download + new_item
    except Exception as err5:
        err_msg5 = (str(err5), 'Error Origin: Receive Episodes')
        print(err_msg5)
        del err_msg5


try:
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    to_download = ""

    receive_episodes("tt1520211")   # Walking Dead
    receive_episodes("tt1405406")   # The Vampire Diaries
    receive_episodes("tt1632701")   # Suits
    receive_episodes("tt2741602")   # The Blacklist
    receive_episodes("tt3107288")   # The Flash
    receive_episodes("tt2632424")   # The Originals
    receive_episodes("tt3032476")   # Better Call Saul
    receive_episodes("tt3322312")   # Daredevil
    receive_episodes("tt4158110")   # Mr. Robot
    receive_episodes("tt4254242")   # The Magicians
    receive_episodes("tt2707408")   # Narcos
    receive_episodes("tt4230076")   # The Defenders
    receive_episodes("tt4928092")   # Prision Break
    receive_episodes("tt0944947")   # Game of Thrones

    if to_download != "":
        # send_proton_email("New downloded Episode(s)!", to_download)    # One can use the proton-mail script provided in another rep to make it sent an email once new EP's are out!
        print("New EP's! " + to_download)
    else:
        print("No New Episodes Today!")
    del to_download
except Exception as err6:
    err_msg6 = (str(err6), 'Error Origin: Receive Episodes Main')
    print(err_msg6)
    del err_msg6
