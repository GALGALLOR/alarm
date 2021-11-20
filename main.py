from flask_mysqldb import MySQL
import pywhatkit as kit
from flask import  get_flashed_messages, session,Flask,render_template,redirect,request,flash,url_for
app=Flask(__name__)

mydb=MySQL(app)
import time
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='GALGALLO10'
app.config['MYSQL_DB']='SONGS'
app.secret_key='yes'
def insert_user(name,list_of_users):
    with app.app_context():
        cursor = mydb.connection.cursor()
        cursor.execute('CREATE TABLE '+name+'(NAME VARCHAR(255))')
        mydb.connection.commit()
    with app.app_context():
        cursor = mydb.connection.cursor()
        cursor.execute('INSERT INTO USERS(NAME)VALUES(%s)',(name,))
        mydb.connection.commit()
        list_of_users.append(name)




def check_user(name,list_of_users):
    try:
        with app.app_context():
            cursor = mydb.connection.cursor()
            cursor.execute('SELECT * FROM USERS WHERE NAME="'+name+'"')
            x=cursor.fetchall()
            for person in x:
                for person in person:
                    list_of_users.append(person)
            if name in list_of_users:
                print('welcome back '+name)
            else:
                print('Hey there ')
                insert_user(name,list_of_users)
    except:
        print('user does not exist')
        insert_user(name,list_of_users)

#tables available are SONGS/NAME and USERS/NAME
list_of_names=[]
USERS='USERS'
list_of_songs=[]
SONGS='SONGS'

def insert_song(name,song,list_of_songs):
    with app.app_context():
        cursor = mydb.connection.cursor()
        cursor.execute('INSERT INTO '+name+'(NAME)VALUES(%s)',(song,))
        mydb.connection.commit()
        list_of_songs.append(song)

def check_song(name,song,list_of_songs):
    try:
        with app.app_context():
            cursor = mydb.connection.cursor()
            cursor.execute('SELECT * FROM '+name+' WHERE NAME="'+song+'"')
            cc=cursor.fetchall()
            for song in cc:
                for song in song:
                    if song in list_of_songs:
                        print('song already exists')
                    else:
                        list_of_songs.append(song)
            if song in list_of_songs:
                print('song already exists')
            else:
                print('this is a new song')
                insert_song(name,song,list_of_songs)                
    except:
        print('this is a new song')
        insert_song(name,song,list_of_songs)

def load_songs(name,list_of_songs):
        with app.app_context():
            cursor = mydb.connection.cursor()
            cursor.execute('SELECT * FROM '+name)
            cc=cursor.fetchall()
            for song in cc:
                for song in song:
                    if song in list_of_songs:
                        pass
                    else:
                        list_of_songs.append(song)

def clear_table(table,list):
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('DELETE FROM '+table)
        mydb.connection.commit()
    list.clear()

def delete_item(table,item,list):
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('DELETE FROM '+table+' WHERE NAME="'+item+'"')
        mydb.connection.commit()
    list.remove(item)
            


'''names=str(input('enter your name  '))
check_user(names,list_of_names)

song=str(input('add song '))

check_song(names,song,list_of_songs)
'''
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        name=str(request.form['name'])
        session['name']=name
        check_user(name,list_of_names)
        print(list_of_names)
        return redirect(url_for('home'))
    else:
        return render_template('login.html')
@app.route('/')
def x():
    return redirect(url_for('login'))
@app.route('/home',methods=['POST','GET'])
def home():
    if request.method=='POST':
        name=session['name']
        song=str(request.form['song'])
        check_song(name,song,list_of_songs)

        try:
            play=request.form['play']
            if 'play' in play:
                for song in list_of_songs:
                    kit.playonyt(song)
                    print('playing the video... waiting for 2 minutes')
                    time.sleep(150)
                    
            else:
                pass
        except:
            pass
        try:
            cleartable=str(request.form['cleartable'])
            print(cleartable)
            if cleartable=='cleartable':
                clear_table(name,list_of_songs)
            else:
                pass

        except:
            pass
        try:
            delete_song=str(request.form['deleted song'])
            print(delete_song)
            if delete_song in list_of_songs:
                delete_item(name,delete_song,list_of_songs)
            else:
                pass
        except:
            pass

        return redirect(url_for('home'))

    else:
        name=session['name']
        load_songs(name,list_of_songs)
        print(list_of_songs)
        return render_template('home.html',name=name,songs=list_of_songs)


if __name__=='__main__':
    app.run(debug=True)
















