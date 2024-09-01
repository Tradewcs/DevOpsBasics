import time
import os
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

path = '/var/log/my-app.log'

size_key = 'my_app_log_size'
mtime_key = 'my_app_log_mtime'

def check_and_update_redis():
    try:
        file_stat = os.stat(path)

        file_size = file_stat.st_size
        file_mtime = file_stat.st_mtime

        last_size = r.get(size_key)
        last_mtime = r.get(mtime_key)

        if last_size is None or last_mtime is None or int(last_size) != file_size or float(last_mtime) != file_mtime:
            r.set(size_key, file_size)
            r.set(mtime_key, file_mtime)

            print(f"Файл {path} змінився. Розмір: {file_size} байт, Дата зміни: {time.ctime(file_mtime)}")
        else:
            print(f"Файл {path} не змінився")

    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
    except Exception as e:
        print(f"Помика: {e}")

if __name__ == "__main__":
    check_and_update_redis()
