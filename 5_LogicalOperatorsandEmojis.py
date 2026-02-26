temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is warm outside 😄")
    print("It is Sunny ☀️")
if temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is Cloudy ☁️")
elif temp <= 0 and not is_sunny: 
    print("It is COLD outside 🥶")
    print("It is Cloudy ☁️")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is warm outside 😄")
    print("It is Cloudy ☁️")

#File>Preferences>Settings (also CTRL + ,)>enable.RunInTerminal
#Above is how you allow emojis to be displayed on Virtual Studio
#or is another logical operator