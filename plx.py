from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount

base = 'https://x:32400'
token = 'token_str'

#account = MyPlexAccount.signin('username', 'password')
#plex = account.resource('servername').connect()  # returns a PlexServer
#print(plex)

# grab the base, token and store them

plex = PlexServer(base, token)

for section in plex.library.sections():
    if section.type == 'artist':
        music_section = section
        break

print(music_section)

artists = music_section.all()

def authenticate():
    # 1.) check for default server setting
    # 2.) check for .config/mmsh/servers/<default>
    # 3.) if token found, use to auth,
    #     else: prompt for username/pwd

