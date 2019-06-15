import sqlite3
from config import Config

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DB, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def createTable(self):
        """
        Generate table for shortener. EXECUTE ONLY ONCE!
        """
        self.cursor.execute(
            "CREATE TABLE shortened_urls ( ID INT PRIMARY KEY  NOT NULL, URL TEXT NOT NULL )"
        )

    def checkId(self, urlID):
        id_cursor = self.cursor.execute('SELECT id FROM shortened_urls')
        ids = [row[0] for row in id_cursor]
        if urlID in ids:
            return True
        else:
            return False

    def checkUrl(self, url):
        url_cursor = self.cursor.execute('SELECT * FROM shortened_urls')
        for row in url_cursor:
            if url in row[1]:
                return row[0]
        return False
        
    def addEntry(self, urlID, url):
        sql = '''INSERT INTO shortened_urls (id, url) VALUES (?,?)'''
        if url[:8] != 'https://' or url[:8] != 'http://':
            url = f'http://{url}'

        task = (urlID, url)
        self.cursor.execute(sql, task)
        self.conn.commit()

    def getUrl(self, urlID):
        if not self.checkId(urlID):
            return False
        else:
            url = self.cursor.execute(f'SELECT url FROM shortened_urls WHERE id="{urlID}"')
            for row in url:
                return row[0]


db = Database()