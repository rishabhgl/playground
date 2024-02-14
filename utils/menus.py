from simple_term_menu import TerminalMenu
from .prompts import mode, diff

mode_options = ["Player Vs Player", "Player Vs Bot"]
diff_options = ["Easy", "Medium", "Impossible"]

mode_menu = TerminalMenu(mode_options, title = mode)
diff_menu = TerminalMenu(diff_options, title = diff)

