from telebot import * 
from dbhelper import DBHelper

db = DBHelper()
bot = telebot.TeleBot("5067906689:AAFQUNvope3pVR2zASCRAN0W-EktCmBSlXI")

hasAnswered=dict() # 2D map make it 

q_no_list=["Q1","Q2","Q3","Q4","Q5","Q6","Q7"]

answer_key=["beterbarker","nitw","bbb.me@gmail.com","paperfishsushi","spiderman_dil_ka_chain","os1nti5fun","st@rtis7he3nd"] 

ques_txt="""
Founder of "@picksar.co" had received death threat messages and has now gone missing. The police need your help to crack the case and trace the blackmailer. 
He was active on Instagram it seems .

Q1) What is his name ?

Q2) Where did he graduate from?

Q3) What is his email-id? 

Q4) Where was the last location he was at?

Q5) He had accidently exposed his password in github's code but soon noticed it and deleted it. There is a way you can still retrieve the password. What is the password ? 

Q6) (Bonus Qs) Find the flag on his personal website.

Q7) What is flag2 ?
"""

hint_txt ="""

Q3) Hint : The first & third star symbol make the name of the Heart Hacker

Q5)Hint : Follow email-automation github link and look for  : "commit" history 

Q6) Hint : Shows "website not found" ? Cause it got deleted but there is a way you can still visit it in the past : Wayback Machine 
"""
manual="""
/start - To view manual
/ques - To view OSINT questions
/ans - To submit answer
/hint - View hint
/help - For help
"""
@bot.message_handler(commands=['start'])
def send_help(message):
    bot.send_message(message.chat.id, manual)  

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Contact CybSec on social media for personal help .https://www.instagram.com/nitw_cybsec/?hl=en")

@bot.message_handler(commands=['ques'])
def send_ques(message):
    bot.reply_to(message, ques_txt )

@bot.message_handler(commands=['hint'])
def send_hint(message):
    bot.reply_to(message, hint_txt )

@bot.message_handler(commands=['ans'])
def send_ans(message):
    # or add KeyboardButton one row at a time:
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Q1')
    itembtn2 = types.KeyboardButton('Q2')
    itembtn3 = types.KeyboardButton('Q3')
    itembtn4 = types.KeyboardButton('Q4')
    itembtn5 = types.KeyboardButton('Q5')
    itembtn6 = types.KeyboardButton('Q6')
    itembtn7 = types.KeyboardButton('Q7')
    markup.row(itembtn1, itembtn2 , itembtn3)
    markup.row(itembtn4 , itembtn5, itembtn6,itembtn7)
    bot.send_message(message.chat.id, "Choose one Qs:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in q_no_list)
def echo_all(message):
    bot.reply_to(message,"Enter your ans: [Format : No space in between & no brackets ] ")

@bot.message_handler(func=lambda message: message.text.lower() in answer_key)
def echo_all(message):

    msg=message.text.lower()
    pos=answer_key.index(msg)
    user_id=message.from_user.id
    first_name=message.from_user.first_name
    last_name=message.from_user.last_name
    
    
    #insert new user
    user_list =db.get_user()
    if user_id not in user_list:
        db.insert_user(user_id,first_name,last_name,0)
    
    #insert new ifanswered bool list for user
    ifExists=hasAnswered.get(user_id,-1) 
    if ifExists==-1:
        hasAnswered[user_id]=[0,0,0,0,0,0,0]
    
    if hasAnswered[user_id][pos]==0:
        
        #add 10 points 
        n_score=db.get_score(user_id) 
        n_score+=10 
        db.update_user(user_id,n_score) 

        #display affirmation
        stmt="Correct answer ! Your score is :"+str(n_score) 
        bot.reply_to(message,stmt)
        hasAnswered[user_id][pos]=1
    else: 
        bot.reply_to(message,"Already answered !")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,"I don't understand you mate!")

bot.infinity_polling()