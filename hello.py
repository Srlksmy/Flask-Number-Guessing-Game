import random
from flask import Flask
gif_higher=["https://media.giphy.com/media/9qkhcOKn1qNqG6fiIP/giphy.gif?cid=790b7611m999g9lconxxuf05ogtko88docf5zqsj8ncix7nr&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/BsQAVgY6ksvIY/giphy.gif?cid=790b7611rs9n52e1tnqykm9pownaogjt3d858afj82u5bfth&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/yoJC2QUWUA4xNSyQbm/giphy.gif?cid=ecf05e47h01t1xjj7vj4dhmjwm126rb9pxqsmdlib1utly4m&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/hPPx8yk3Bmqys/giphy.gif?cid=790b76112xvckxnjbooda4it5hvatcdbumyhiyc2cnqsk7hl&ep=v1_gifs_search&rid=giphy.gif&ct=g"]
gif_lower=["https://media.giphy.com/media/LFA6Qbj3Z7l4Y/giphy.gif?cid=ecf05e47okvj6eah3kna7tfjh9ivyv77fa43vkdw6ezzxxek&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/iv1mk4AxZ1lJl767ib/giphy.gif?cid=790b7611a0kf3h7p4wlnyya8pb4358byc1byjyvta6wudrxo&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/MAhxOeY6u5uVPdlSoz/giphy.gif?cid=790b76116l87pcmf08ayj2ssb3c3stugzeiymza8zgvtf8z0&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/UQUiq0lLGDRMCvJUjX/giphy.gif?cid=ecf05e47zo5c8u4il50nornwney6jvz6r4t46t7tof2oqhyn&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHU2NTBzdGNpazU2eXA1MjVhN2V0ZXYwd3pwOWJxaG9rd3dnYzhnbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VL48WGMDjD64umCEkv/giphy.gif"]
gif_win=["https://media.giphy.com/media/l3q2BXqLMnzhVF720/giphy.gif?cid=ecf05e47z5l4y7ngwe9bzhlbfemci6ojdxag5kydm1lohr67&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/g9582DNuQppxC/giphy.gif?cid=790b7611qrjgbye0m2rnj0xru3xar1iulqyq2lm3n0g87pvl&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/b7MtjZ8uhWMaHMsueA/giphy.gif?cid=790b7611k1obth3s2ktyrav30admatl72kp0n8mgdp4po5i6&ep=v1_gifs_search&rid=giphy.gif&ct=g","https://media.giphy.com/media/S6Hyy3F1bd90uMYDXj/giphy.gif?cid=ecf05e479137hq9gt5l88uizcqv3pxzbhvo9hz4gdkwnyfm7&ep=v1_gifs_search&rid=giphy.gif&ct=g"]
def styling(func):
    def wrapper(**kwargs):
        text=func(**kwargs)
        if func.__name__ == 'game':

            if 'lower' in text:
                colour='blue'
                return f' <h1 style="color:{colour}";text-align:center;>{text}</h1><br><br><img src={random.choice(gif_lower)}>'

            if  'higher' in text:
                colour='orange'
                return f' <h1 style="color:{colour}">{text}</h1><br><br><img src={random.choice(gif_higher)}>'

            if 'Right' in text:
                colour='green'
                return f' <h1 style="color:{colour};text-align:center;">{text}</h1><br><br><img src={random.choice(gif_win)}>'
        else:
            return f'<h1 style="color:blueviolet;text-align:center;"> Let"s play number guess game..!!</h1><br><br><img style="text-align:center;" src="https://media.giphy.com/media/ZYjbvRRCSDb9mthj9E/giphy.gif?cid=790b7611436ubtnr88uqvnmqzj3n2yhuwpssmpf2z3nb27do&ep=v1_gifs_search&rid=giphy.gif&ct=g">'

    return wrapper

app=Flask('__main__')

@app.route('/')
def home():
    global N
    N = random.randint(1, 20)

    return f'<h1 style="color:blueviolet;text-align:center;"> Let us play number guess game..!!</h1><h2>Please enter your guessed number(between 1-20) in end of URL as "/yourguess"<br> eg:if guess is 8 type \8 at end of url </h2>'\
           f'<img style="text-align:center;" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXgydXljZHI0eTI0eXo0Nm5pdTZrMzFuaGIzYjU2cHRmemN2cXQxeCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/bAV0Sr4IunHeSJoVmX/giphy.gif">'


@app.route('/<int:num>')
@styling
def game(num):

    if num<N:
        return 'you guessed lower'
    if num>N:
        return 'you guessed higher'
    if num==N:
        return 'WOW!! Right guess'

@app.route('/<notnumber>')
def error(notnumber):
    if not isinstance(notnumber,int):
        return f' <h1 style="color:red;" >Please ,only type a number between 1 and 20 in url after /,  </h1>'\
               f'<h2> Guess again in URL</h2><br><img src="https://media.giphy.com/media/3o7WTDH9gYo71TurPq/giphy.gif?cid=790b7611o6srb6z74h8nxb6syvw1kitwmfhliuudj8cqpnb0&ep=v1_gifs_search&rid=giphy.gif&ct=g">'



if __name__=='__main__':
    app.run(debug=True)



