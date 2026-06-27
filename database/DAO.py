from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAlbum(d):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """ select a.*, t.Nbrani as NBrani, t.media as Media
                    from album a ,
                    (select t.AlbumId , avg(t.Milliseconds )/1000 as media, count(*) as Nbrani
                    from track t 
                    group by t.AlbumId 
                    having media > %s) as t
                    where a.AlbumId = t.albumid  """
        cursor.execute(query, (d,))
        for row in cursor:
            results.append(Album(**row))
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(d, idMapA):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """with album_media as (
                    select t.AlbumId, avg(t.Milliseconds )/1000 as media
                    from track t 
                    group by t.AlbumId 
                    having media > %s
                    ),
                    album_playlist as (
                    select a.albumid , p.PlaylistId 
                    from track t , playlisttrack p, album_media a
                    where a.albumid = t.AlbumId 
                    and t.TrackId = p.TrackId )
                    select a.albumid as id1, a2.albumid as id2
                    from album_playlist a
                    join album_playlist a2 on a.playlistid = a2.playlistid 
                    where a.albumid < a2.albumid 
                    group by a.albumid , a2.albumid """
        cursor.execute(query, (d,))
        for row in cursor:
            results.append((idMapA[row['id1']], idMapA[row['id2']]))
        cursor.close()
        conn.close()
        return results