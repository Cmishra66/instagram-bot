from instabot import Bot
bot=Bot()
bot.login(username="enter your username",password="enter your password")
bot.follow('sasquatch_._')
bot.upload_photo("enter path",caption="enter caption")
bot.unfollow('sasquatch_._')
bot.send_message("hello world",["enter user1","enter user2","enter usern"])
followers=bot.get_user_followers("enter your username")
for follower in followers:
 print(bot.get_user_info(follower))
 following=bot.get_user_followers("enter your username")
for Following in following:
 print(bot.get_user_info(following))
 