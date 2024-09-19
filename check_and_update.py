import time
import os
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

path = '/var/log/my-app.log'

changes_key = 'my_app_log_changes'
size_key = 'my_app_log_size'
mtime_key = 'my_app_log_mtime'
position_key = 'my_app_log_position'

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

            with open(path, 'r') as file:
                last_position = r.get(position_key)
                if last_position is not None:
                    file.seek(int(last_position))

                new_lines = file.readlines()
                for line in new_lines:
                    r.rpush(changes_key, line.strip())

                r.set(position_key, file.tell())

            print(f"Файл {path} змінився. Розмір: {file_size} байт")
        else:
            print(f"Файл {path} не змінився")

    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    check_and_update_redis()
