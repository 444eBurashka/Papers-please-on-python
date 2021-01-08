import ctypes
user = ctypes.windll.user32

class SCREEN:
    size = (user.GetSystemMetrics(0), user.GetSystemMetrics(1))
    label = 'The Descent'