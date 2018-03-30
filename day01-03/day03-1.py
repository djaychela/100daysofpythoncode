from datetime import datetime, timedelta
import pygame

work_timer = 25
rest_timer = 5
cycles = 4
work_delta = timedelta(minutes=work_timer)
rest_delta = timedelta(minutes=rest_timer)


def print_header(message):
    stars = '*' * (len(message) + 6)
    gaps = '*  ' + (' ' * len(message)) + '  *'
    message = '*  ' + message + '  *'
    print(stars)
    print(gaps)
    print(message)
    print(gaps)
    print(stars)


def timer(end_time):
    while datetime.now() < end_time:
        pass
    play_alarm()
    return


def play_alarm():
    pygame.mixer.music.stop()
    pygame.mixer.music.rewind()
    pygame.mixer.music.play()


def start_timer(mode):
    start_time = datetime.now()
    print(datetime.strftime(start_time, '%H:%M:%S'))
    print(f'{mode} mode!')
    if mode.lower() == 'work':
        timer(start_time + work_delta)
    else:
        timer(start_time + rest_delta)


def main():
    pygame.mixer.init()
    pygame.mixer.music.load('gong.mp3')
    global cycles
    current_cycle = 1
    print_header('Pomodoro Timer App')
    while current_cycle <= cycles:
        print(f'Cycle :{current_cycle} of {cycles}')
        start_timer('Work')
        start_timer('Rest')
        current_cycle += 1
    print('Cycles finished!')


if __name__ == "__main__":
    main()