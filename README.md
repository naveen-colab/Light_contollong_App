# telegram_bot
Light Controlling App allows an user to control a light via telegram bot. 
Note: Telegram Bot is a programme that behaves like a normal chat partner with additional functions. It performs predefined tasks independently and without the user’s involvement. The term bot is derived from the term for robot.

Using telegram bot user can send queries to turn on or turn off the light.
These queries are send to adafruit cloud platform.
Note: Adafruit.io is a cloud service - that just means we run it for you and you don't have to manage it. You can connect to it over the Internet. It's meant primarily for storing and then retrieving data but it can do a lot more than just that.

When adafruit receives the query it process it and sends a response as a picture to the user via telegram bot.
The further scope of this app is the adafruit has to connect to a wifi connected arduino board to which the real light is connected. So based on the user queries arduino can turn on or off a real light.
