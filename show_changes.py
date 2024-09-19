import redis

r = redis.Redis(host='localhost', port=6379, db=0)

changes_key = 'my_app_log_changes'

def print_all_changes():
    try:
        changes = r.lrange(changes_key, 0, -1)
        if not changes:
            return
        
        for i, change in enumerate(changes):
            print(f"Зміна {i+1}: {change.decode('utf-8')}")
        
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    print_all_changes()
