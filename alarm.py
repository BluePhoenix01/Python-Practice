import time

import schedule
from playsound import playsound
from pathlib import Path

BASE_DIR = Path(__file__).parent
ALARM_FILE = BASE_DIR / "alarm.mp3"


class Alarm:
    def __init__(self, sound_file, alarm_time):
        self.sound_file = sound_file
        self.alarm_time = alarm_time

    def play_sound(self, sound_file):
        playsound(sound_file)

    def start(self):
        schedule.every().day.at(self.alarm_time).do(self.play_sound, self.sound_file)

        while True:
            schedule.run_pending()
            time.sleep(1)


def main():
    alarm = Alarm(ALARM_FILE, "05:01")
    alarm.start()


if __name__ == "__main__":
    main()
