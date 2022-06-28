import os, platform, time

b = platform.architecture()[0]

if b == '64bit':

    print("\n\x1b[1;92mCongratulations Your Device Support This Tool\033[1;37m")

    os.system('xdg-open https://youtube.com/channel/UC6OSDzf3I3Ws8onwga637uA/');time.sleep(5)

    import SSB

elif b == '32bit':

    print("\x1b[1;91mOpps Sorry Beb Your Mobile Not Support This Tool")
