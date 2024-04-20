from flask import Flask,request,render_template 
import build_bot 
# Khởi tạo Flask app 
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def chatbot1():
    # Kiểm tra xem có phải người dùng view trang web không
    if request.method == "GET":
        #Trả về trang chatbot
        return render_template("chatbot1.html")
    else:
        user_input = request.form["user_message"]
        noidungchathientai = str(request.form["chat_content"])
        noidungchathientai += "\n [YOU]:"+ str(user_input)
        noidungchathientai += "\n [BOT]:"+ str(build_bot.predict_intent(user_input))
        return render_template('chatbot1.html',noidungchathientai= noidungchathientai)

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/lienhe')
def lienhe():
    return render_template('lienhe.html')

@app.route('/baiviet')
def baiviet():
    return render_template('baiviet.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)