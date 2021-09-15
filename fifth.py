import threading
import time

from functools import wraps
from contextlib import contextmanager
from IPython.display import HTML, display


def report(threads):
    items = (f'<b>{thread.name}</b>'
             for thread in threads)
    items = ', '.join(items)
    line = f'New threads: {items}'
    display(HTML(line))


@contextmanager
def new_threads_tracker():
    seen_threads = set(threading.enumerate())
    exit_event = threading.Event()
    
    def tracker():
        while not exit_event.is_set():
            current = set(threading.enumerate())
            new_threads = current - seen_threads
            if new_threads:
                report(new_threads)
                seen_threads.update(new_threads)
            time.sleep(1)
                
    tracker = threading.Thread(target=tracker)
    seen_threads.add(tracker)
    tracker.start()

    try:
        yield
    finally:
        exit_event.set()
    

def decorate_run_cell(ipython, func):
    @wraps(func)
    def wrapper(code, *args, **kwargs):
        with new_threads_tracker():
            return func(code, *args, **kwargs)
    return wrapper

def load_ipython_extension(ipython):
    print('Loading "fifth" extension')

    ipython.run_cell = decorate_run_cell(
        ipython,
        ipython.run_cell
    )
