
import mysql.connector as connector 

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='ashq.mysql.pythonanywhere-services.com',port='3306', user='***', password='****', database='ashq$cyberverse', auth_plugin='mysql_native_password')
        query='CREATE TABLE IF NOT EXISTS ScoreTable (userID INTEGER PRIMARY KEY,firstID text,lastID text,score INTEGER DEFAULT 0)'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self, user_id , first_id , last_id ,new_score):
        query = "INSERT INTO ScoreTable (userID,firstID,lastID,score) VALUES ({},'{}','{}',{})".format(user_id , first_id,last_id ,new_score )
        print(query)
        self.con.reconnect()
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to db")
    
    def update_user(self, user_id ,new_score):
        query = "UPDATE ScoreTable SET score={} WHERE userID={}".format(new_score ,user_id  )
        print(query)
        self.con.reconnect()
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Score updated")

    def get_score(self,user_id):
        query = "SELECT score FROM ScoreTable WHERE userID=({})".format(user_id) 
        self.con.reconnect()
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            return (row[0])
    
    def get_user(self):
        query = "SELECT userID FROM ScoreTable "
        self.con.reconnect()
        cur=self.con.cursor()
        cur.execute(query)
        arr=[]
        for row in cur:
            arr.append(row[0])
        return (arr) 

#db.insert_user(124,"admin2",20)
#db.get_user()
#db.update_user(123,30)
