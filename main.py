from flask_mysqldb import MySQL
from flask import  get_flashed_messages, session,Flask,render_template,redirect,request,flash,url_for
app=Flask(__name__)

mydb=MySQL(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='GALGALLO10'
app.config['MYSQL_DB']='SONGS'

def insert_user(name,listv):
    with app.app_context():
        cursor = mydb.connection.cursor()
        cursor.execute('INSERT INTO USERS(NAME)VALUES(%s)',(name,))
        mydb.connection.commit()
        listv.append(name)

def check_user(name,listv):
    try:
        with app.app_context():
            cursor = mydb.connection.cursor()
            cursor.execute('SELECT * FROM USERS WHERE NAME="'+name+'"')
            x=cursor.fetchall()
            for person in x:
                for person in person:
                    listv.append(person)
            if name in listv:
                print('welcome back '+name)
            else:
                print('Hey there ')
                insert_user(name,listv)
    except:
        print('user does not exist')
        insert_user(name,listv)

#tables available are SONGS/NAME and USERS/NAME
list_of_names=[]
USERS='USERS'
list_of_songs=[]
SONGS='SONGS'




names=str(input('enter your name  '))
check_user(names,list_of_names)

song=str(input('add song'))

def add_user(names,song,listx):
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('INSERT INTO names('+names+')VALUES(%s)',(song))
        mydb.connection.commit()
        listx.append(names)

def check_user(names,song,listx):
    try:
        with app.app_context():
            cursor=mydb.connection.cursor()
            cursor.execute('SELECT * FROM '+names+' WHERE SONGS="'+song+'"')
            ll=cursor.fetchall()
            for song in ll:
                for song in song:
                    listx.append(song)
    except:
        print('user doesnt exist')
        add_user(names,song,listx)
    # check if the table with the user's name exists first
    #if it exists... check if the song exists in it
    #if the song exists in it...pass
    #if the song doesnt exist in it pass
    #if the table doesnt even exist... create it then
    #  add the song















