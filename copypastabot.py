import socket
import random
import time
import config

connection_data = ('irc.chat.twitch.tv', 6667)
token = config.TOKEN
user = config.USER
channel = "#shocknoble"
server = socket.socket()
server.connect(connection_data)
server.send(f"PASS {token}\n".encode('utf-8'))
server.send(f"NICK {user}\n".encode('utf-8'))
server.send(f"JOIN {channel}\n".encode('utf-8'))
content_match = channel + " :.+"
play = 0

allowlist = ["geodun","dondums_","captainsalty3"]

while True:
    message = (server.recv(2048).decode('utf-8'))

    chatter_placement = message.find("!")
    chatter = message[1:chatter_placement]

    content_placement = message.find(":",1)
    content = message[content_placement+1:]

    print(content)
    print (chatter)

    print(message)
    
    if "PING" in message:
        server.send(bytes("PONG\r\n", "UTF-8"))

    if ("that reminds me of a random story" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "I was walking down the street the other day and some person stopped me and said 'did u kno "+channel[1:]+" is the most cracked gamer ever and has never lost a game or made a mistake or blinked during gameplay?' and i said 'i did kno that y u telling me this' and they said 'bc its so true' i was so confused but now i understand tysm\r\n", "UTF-8"))

    if ("berrypasta" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "It has been a great run. Whether I win or lose today will not determine if I had a good time tonight or not. What WILL determine that is the fun, the friendships, and the memories we made together. I am so thankful for this community and every single person here on this wonderful Friday night. I will close with this. Joel was not here when I complimented their eyebrows and I think they need to know that they are envied by all. Thank you.\r\n", "UTF-8"))

    if ("i am your #1 fan" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "If "+channel[1:]+" has million number of fans i am one of them. if "+channel[1:]+" has ten fans i am one of them. If "+channel[1:]+" have only one fan and that is me. If "+channel[1:]+" has no fans, that means i am no more on the earth. if world against the "+channel[1:]+", i am against the world. i love #"+channel[1:]+" till my last breath.. .. Die Hard fan of "+channel[1:]+". Hit Like If you Think "+channel[1:]+" Best strimmer & Smart In the world\r\n", "UTF-8"))

    if ("i am the only one here" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "Hi "+channel[1:]+" - It’s me, your only Viewer. For Months I have created the illusion that you are streaming to a large audience. But here’s the truth: all these people in the chat are me. And now, for you to be convinced of this, I will send this message from all my accounts.\r\n", "UTF-8"))

    if ("shock ded" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "apolgy for bad english. where were u wen shock die. i was at house eating dorito when phone ring. 'squak is kiln'. 'no'\r\n", "UTF-8"))

    if ("!gitgud" in content):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "git: 'gud' is not a git command. See 'git --help'. The most similar command is add\r\n", "UTF-8"))

    if ("bro you good?" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "That's just the darkness from down below welling up through your thoughts, bro. I was like you once. So full of malice and sin. Then I found the light and... you know what? It turned my life around. Maybe it can turn your life around too. There's this streamer called dondums underscore, and no cap fam, they're pretty rad. Why don't we go out for some laser tag and I'll introduce you to the best bro of all: dondums_. Also my wife sells HerbaLife and plastic jewelry, so bring a credit card.\r\n", "UTF-8"))

    if ("happy birthday bug!" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "nine hundred and thirty-three years ago, you were born on this day and helped finish building rome, curing polio, and creating spider-man. happy birthday bug!\r\n", "UTF-8"))

    if ("splain" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "shockn14Splaining bugbyt1Sparkle " +content.strip()+ " bugbyt1Sparkle shockn14Splaining\r\n", "UTF-8"))

    if (" told me something weird before stream" in content) and (chatter in allowlist):
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + chatter +" was here before stream even started. " + chatter + " was messaging me about 'i hope "+channel[1:]+" notices im here and that ive been here the entire time it would crush me if "+channel[1:]+" didnt notice i was here but that wont happen for sure haha rite?' and i said " + chatter + " thats weird --- i didnt undersand but now i do, ty\r\n", "UTF-8"))

    if ("literally the worst game: " in content) and (chatter in allowlist):
        game_placement = content.find(":")
        print(game_placement)
        bad_game = content[game_placement+1:].strip()
        print(bad_game)
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "hey " + bad_game + " was a disgrace and should not exist. its the the entire reason that i keep " + bad_game + " at the bottom of my junk drawer no offense to anyone here but, the game did not feel like a " + bad_game + " game, but im still waiting for " + bad_game + "\r\n", "UTF-8"))

    if "!play" in content:
        play = play + 1
        if play > 10:
            time.sleep(random.randint(3,10))
            server.send(bytes("PRIVMSG " + channel + " :" + "!play\r\n", "UTF-8"))
            play = 0
            time.sleep(120)

