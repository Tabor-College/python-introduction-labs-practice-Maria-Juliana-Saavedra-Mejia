## Spotify Basic

class Song :
    total_songs = 0 # STATIC VARIABLE

    def __init__ ( self , song_id , title , artist , duration ) :
        self . __song_id = song_id
        self . __title = title
        self . __artist = artist
        self . __duration = duration
        self . __play_count = 0

        Song . total_songs += 1

    def get_title ( self ) :
        return self . __title
    
    def get_artist ( self ) :
        return self . __artist
    
    def set_duration ( self , new_duration ) :
        if new_duration > 0:
            self . __duration = new_duration
            return True
        print ( " Duration must be positive ! " )
        return False
    
    def __increment_plays ( self ) :
        self . __play_count += 1

    def play ( self ) :
        self . __increment_plays ()
        print(f" Playing : { self . __title } ( Plays : { self . __play_count })" )

    @staticmethod

    def get_total_songs () :
        return Song . total_songs
    
class Playlist:
    def __init__(self, name, creator):
        self.__name = name
        self.__creator = creator
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print ( f" { song . get_title () } added to { self . __name } " )

    def display(self):
        print(f"\nPlaylist: {self.__name}")
        for i , song in enumerate ( self . songs , 1) :
            print(f"{i}. {song.get_title()} - {song.get_artist()}")

class User :
    total_users = 0

    def __init__ ( self , username , email , balance ) :
        self . __username = username
        self . __email = email
        self . __balance = balance
        self . __playlists = []

        User . total_users += 1

    def pay_for_premium ( self , cost ) :
        if cost <= self . __balance :
            self . __balance -= cost
            print ( " Premium activated ! " )
            return True
        print ( " Insufficient balance ! " )
        return False
    
    def create_playlist ( self , name ) :
        playlist = Playlist ( name , self . __username )
        self . __playlists . append ( playlist )
        return playlist
    
    @staticmethod
    def get_total_users () :
        return User.total_users
    
# Create Song objects
song1 = Song (101 , " Blinding Lights " , " The Weeknd " , 200)
song2 = Song (102 , " Shape of You " , " Ed Sheeran " , 234)

print ( " Total Songs : " , Song . get_total_songs () )

# Play a song
song1 . play ()
song1 . play ()

# Create User
user1 = User ( " Amar " , " amar@spotify . com " , 500)

# Create Playlist
favorites = user1 . create_playlist ( " My Favorites " )

# Add Song objects to Playlist
favorites . add_song ( song1 )
favorites . add_song ( song2 )

# Display Playlist
favorites . display ()

# Pay for premium
user1 . pay_for_premium (200)

## Spotify Advanced 

def playback_logger(func):
    """Decorator: Adds logging arround playback"""
    def wrapper(self):
        print(".          Logging Playback......")
        result = func(self)
        print("Playback complete \n")
    return wrapper

class Song:
    total_songs = 0

    def __init__(self, song_id , title , artist , duration):
        self.__song_id = song_id
        self.__title = title
        self.__artist = artist 
        self.__duration = duration
        self.__play_count = 0
        Song.total_songs +=1

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def __increment_plays(self):
        self.__play_count += 1
    
    @playback_logger
    def play(self):
        self.__increment_plays()
        print(f"Playing: {self.__title} ({self.__play_count})")

class Playlist:
    def __init__(self, name):
        self.__name = name 
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.songs):
            raise StopIteration
        song = self.songs[self.index]
        self.index += 1
        return song
    
    def play_song(self):
        """ GENERATOR : Yields songs one at a time """
        for song in self.songs:
            yield song

    def play_all(self, player):
        """
        DUCK TYPING :
        Any object with a play () method works
        """
        for song in self:
            player.play(song)
    

def playback_limiter(max_plays):
        """
        CLOSURE :
        Remembers play count across calls
        """
        count = 0

        def limiter(song):
            nonlocal count
            if count < max_plays:
                song.play()
                count += 1
            else:
                print("Playback limit reached")
        return limiter

class SimplePlayer: 
    def play ( self , song ) :
        song.play()

class LimitedPlayer:
    def __init__(self, limiter):
        self.limiter = limiter
    
    def play(self, song):
        self.limiter(song)

# Songs
s1 = Song (101 , " Blinding Lights " , " The Weeknd " , 200)
s2 = Song (102 , " Shape of You " , " Ed Sheeran " , 234)

# Playlist
favorites = Playlist ( " My Favorites " )
favorites . add_song ( s1 )
favorites . add_song ( s2 )

# Closure
limit_1 = playback_limiter (1)

# Players
normal_player = SimplePlayer ()
limited_player = LimitedPlayer ( limit_1 )

# Duck typing in action
favorites . play_all ( normal_player )
favorites . play_all ( limited_player )     
        

    