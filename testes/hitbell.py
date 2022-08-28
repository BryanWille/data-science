from googleapiclient.discovery import build
import pyodbc

class Canal:
    playlist = []
    statistics = []
    channelname = []

    #Construtor
    def __init__(self, apiYoutubeKey, id_canal):
        apiKey = apiYoutubeKey

        self.youtube = build('youtube', 'v3', developerKey=apiKey)
        self.canal = id_canal
        self.statistics = self.youtube.channels().list(part="statistics", id=self.canal).execute()  # estatisticas do canal
        self.channelName = self.youtube.channels().list(part="snippet", id=self.canal).execute()    # todas informações do canal
        self.playlist = self.youtube.channels().list(part="contentDetails", id=self.canal).execute() # detalhes de conteúdo do canal.

        self.subCount = self.subCount()
        self.channelInformations()
        self.dbConnection()
        self.insertChannelDb(self.canal, self.titleC, self.subCount, self.videoCount)
        self.generateAllVideos()

        print(f'{self.subCount} subscribers!');                          

    #Retornar a quantidade de inscritos.
    def subCount(self):
        return self.statistics['items'][0]['statistics']['subscriberCount']

    #Gerar atributos com a informação do canal
    def channelInformations(self):
        self.idC = self.canal
        self.titleC = self.channelName['items'][0]['snippet']['title']
        self.videoCount = self.statistics['items'][0]['statistics']['videoCount'] 
        self.subscriberCount = self.subCount
    

    # Vai gerar os vídeos e colocar eles na tabela videos.
    def generateAllVideos(self):

        #Todo canal tem uma playlist com todos os seus vídeos, então forço para pegar essa playlist.
        namePlaylist = self.playlist['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        idChannel = self.idC
        nextPage = None

        # Enquanto houver videos continue pegando os dados
        while True:
            #Pegar propriedade do video
            playlist = self.youtube.playlistItems().list(part="snippet", playlistId= namePlaylist, maxResults=1, pageToken = nextPage).execute() 

            
            nextPage = playlist.get('nextPageToken') 
            if nextPage is None: # se não houver vídeos pare o loop
                break;
            
            idVideo = playlist['items'][0]['snippet']['resourceId']['videoId'] 
            title = playlist['items'][0]['snippet']['title']
            
            print("Video:", idVideo, "importado com sucesso!")

            video = []
            video = self.youtube.videos().list(part="statistics", id=idVideo).execute() # Pegar estatisticas dos vídeos
            viewCount = video['items'][0]['statistics']['viewCount']

            # Alguns vídeos possuem like desativas então estão sendo retornados como 0.
            try:
                likeCount = video['items'][0]['statistics']['likeCount']
            except:
                likeCount = 0
            

            # Configurações dos vídeos, duração e definição.
            contentDetails = []
            contentDetails = self.youtube.videos().list(part='contentDetails', id=idVideo).execute()
            duration = contentDetails['items'][0]['contentDetails']['duration']
            dimension = contentDetails['items'][0]['contentDetails']['definition']

            #Inserção no banco de dados
            self.insertVideosDb(idVideo, idChannel, title, viewCount, likeCount, duration, dimension)

    #Conexão com o banco de dados.
    def dbConnection(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-6APO6LU;Database=Hitbell;Trusted_Connection=yes')
        self.cursor = conn.cursor()


    #Vai inserir o canal selecionado no banco de dados
    def insertChannelDb(self, idC, titleC, subscriberCount, videoCount):
        inserirCanal = f"""INSERT INTO CHANNEL(ID, TITLE, SUBSCRIBERCOUNT, VIDEOCOUNT)
                    VALUES
                        ('{idC}', '{titleC}', {subscriberCount}, {videoCount})"""
        self.cursor.execute(inserirCanal)
        self.cursor.commit()


    #Vai inserir os vídeos no banco de dados
    def insertVideosDb(self, idVideo, idChannel, title, viewCount, likeCount, duration, dimension):
        inserirVideos = f"""INSERT INTO VIDEOS(IDVIDEO, IDCHANNEL, TITLE, VIEWCOUNT, LIKECOUNT, DURATION, DIMENSION)
                        VALUES 
                            ('{idVideo}', '{idChannel}', '{title}', {viewCount}, {likeCount}, '{duration}', '{dimension}')"""
        self.cursor.execute(inserirVideos)
        self.cursor.commit();

boasVindas = Canal('AIzaSyCVTSrpICIdZ1x74qkj0hoNJtWv9Hfs3gc', 'UCopVMAEcdblYjF1-4Z7rcvw')

#Eu possuo mais experiência com POO em Java, em Python ainda estou aprendendo.
