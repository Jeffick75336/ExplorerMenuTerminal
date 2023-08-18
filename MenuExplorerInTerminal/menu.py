import curses
import os

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    options = [
        "Open Linux File Explorer",
        "Open Windows File Explorer",
        "Open macOS File Explorer",
        "Exit"
    ]
    current_row = 0

    while True:
        stdscr.clear()

        for i, option in enumerate(options):
            x = int((curses.COLS - len(option)) / 2)
            y = int((curses.LINES - len(options)) / 2) + i

            if i == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, option)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == 10:  # Enter key
            if current_row == len(options) - 1:
                break
            elif current_row == 0:
                try:
                    os.system("xdg-open .")  # Open File Explorer in Linux
                except:
                    pass
            elif current_row == 1:
                try:
                    os.system("explorer .")  # Open File Explorer in Windows
                except:
                    pass
            elif current_row == 2:
                try:
                    os.system("open .")      # Open File Explorer in macOS
                except:
                    pass

if __name__ == "__main__":
    curses.wrapper(main)
