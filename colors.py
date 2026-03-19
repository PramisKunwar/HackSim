# ANSI color helpers
C = {'green': '92', 'red': '91', 'yellow': '93', 'cyan': '96', 'bold': '1'}

def color(t, c): 
    return f"\033[{c}m{t}\033[0m"

green = lambda t: color(t, C['green'])
red = lambda t: color(t, C['red'])
yellow = lambda t: color(t, C['yellow'])
cyan = lambda t: color(t, C['cyan'])
bold = lambda t: color(t, C['bold'])