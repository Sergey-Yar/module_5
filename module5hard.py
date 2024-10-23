from time import sleep


class User:
    """
    Класс пользователя
    """

    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname  # имя пользователя, строка
        self.password = hash(password)  # пароль в хэшированном виде
        self.age = age  # возраст, число


class Video:
    """
    Класс видео
    """
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class UrTube:
    """
    Класс видеохостинга
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def __eq__(self, other):
        # if isinstance(other, User):
        #     return self.nickname == other.nickname
        if isinstance(other, Video):
            return self.title == other.title


    def log_in(self, nickname, password): # вход
        for log in self.users:
            if log.nickname == nickname and log.password == hash(password):
                self.current_user = log
                print(f'Вход выполнен. Привет, {nickname}')



    def register(self, nickname, password, age): #регистрация пользователя
        for us in self.users:
            if us.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return None
        user = User(nickname, password, age)
        self.users.append(user)
        print('Регистрация прошла успешно.')
        self.current_user = user
        return user


    def log_out(self):
        self.current_user = None


    def add(self, *args): #добавление видео
        for vid in args:
            if vid not in self.videos:
                self.videos.append(vid)
                print(f'Добавлено видео: "{vid.title}"')
            else:
                print('Такое видео уже есть')


    def get_videos(self, search): #поиск видео
        result_videos = []
        for get in self.videos:
            if search.lower() in get.title.lower():
                result_videos.append(get.title)
        return result_videos


    def watch_video(self, title): #воспроизведение видео
        for j in self.videos:
            if j.title == title:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif self.current_user.age >= 18:
                    j.adult_mode = True
                elif j.adult_mode == False:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print('Просмотр видео: ', title)
                    for time_now in range(1, j.duration + 1):
                        sleep(1)
                        print(time_now, end=" ", flush=True)
                    print("\nКонец видео")
                    sleep(1)
                    time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 30)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print('Результат поиска 1 ', ur.get_videos('лучший'))
print('Результат поиска 2 ', ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Лучший язык программирования 2024 года')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

# ur.watch_video('Для чего девушкам парень программист?')
#
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print('Текущий пользователь: ', ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
