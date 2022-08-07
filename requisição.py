# pip install --upgrade google-api-python-client

from googleapiclient.discovery import build

apiKey="AIzaSyC9EpW0P-o9tuOu94AA46FuThpCFXtHy44"        # Minha API KEY.
youtube = build('youtube', 'v3', developerKey=apiKey)   # Construindo a API do Youtube.
canal = "UCopVMAEcdblYjF1-4Z7rcvw"                      # Url do Canal.

estatisticas = []
estatisticas = youtube.channels().list(part="statistics", id=canal).execute()     # Pegando as estatisticas do canal.

quantidade_inscrito = estatisticas['items'][0]['statistics']['subscriberCount']   # Pegando somente a quantidade de inscritos.

print(f'{quantidade_inscrito} subscribers')


# Agora o banco de dados!
#pip install pyodbc.

import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-6APO6LU;Database=Hitbell;Trusted_Connection=yes') # conexão com banco de dados

cursor = conn.cursor();

# Extração de dados da tabela canal:

nomeCanal = []
nomeCanal = youtube.channels().list(part="snippet", id=canal).execute()


idC = canal
videoCount = estatisticas['items'][0]['statistics']['videoCount'] 
subscriberCount = quantidade_inscrito
titleC = nomeCanal['items'][0]['snippet']['title']

inserirCanal = f"""INSERT INTO CHANNEL(ID, TITLE, SUBSCRIBERCOUNT, VIDEOCOUNT)
                    VALUES
                        ('{idC}', '{titleC}', {subscriberCount}, {videoCount})"""
cursor.execute(inserirCanal)
cursor.commit()


#Extração de dados da tabela video:

playlist = []
playlist = youtube.channels().list(part="contentDetails", id=canal).execute()
namePlaylist = playlist['items'][0]['contentDetails']['relatedPlaylists']['uploads']

idChannel = idC
nextPage = None

while True:
    playlist = youtube.playlistItems().list(part="snippet", playlistId= namePlaylist, maxResults=1, pageToken = nextPage).execute()
    
    nextPage = playlist.get('nextPageToken')

    if nextPage is None:
        break;

    
    idVideo = playlist['items'][0]['snippet']['resourceId']['videoId']
    title = playlist['items'][0]['snippet']['title']
    print(idVideo)

    video = []
    video = youtube.videos().list(part="statistics", id=idVideo).execute()
    viewCount = video['items'][0]['statistics']['viewCount']
    try:
        likeCount = video['items'][0]['statistics']['likeCount']
    except:
        likeCount = 0
    
    contentDetails = []
    contentDetails = youtube.videos().list(part='contentDetails', id=idVideo).execute()
    duration = contentDetails['items'][0]['contentDetails']['duration']
    dimension = contentDetails['items'][0]['contentDetails']['definition']

    inserirVideos = f"""INSERT INTO VIDEOS(IDVIDEO, IDCHANNEL, TITLE, VIEWCOUNT, LIKECOUNT, DURATION, DIMENSION)
                    VALUES 
                        ('{idVideo}', '{idChannel}', '{title}', {viewCount}, {likeCount}, '{duration}', '{dimension}')"""
    cursor.execute(inserirVideos)
    cursor.commit();
