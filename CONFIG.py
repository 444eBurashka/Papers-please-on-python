import ctypes
user = ctypes.windll.user32


class SCREEN:
    size = (user.GetSystemMetrics(0), user.GetSystemMetrics(1))
    label = 'The Descent'

# ACTIONS
startintro_1 = True
startintro_2 = False
startintro_3 = False
menu = False

fmenu = False

startgame = False