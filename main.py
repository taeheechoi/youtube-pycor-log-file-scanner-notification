from mmap import mmap, ACCESS_READ
from glob import glob
from multiprocessing.dummy import Pool  # from multiprocessing is not working
from pathlib import Path
import logging

from notification import Notification

SOURCE_DIR = 'source'  # source folder
WORDS = ['where are you?', 'pycor']  # search word


def file_list():
    # return list of files within a specific directory
    path = Path(SOURCE_DIR)
    return list(path.glob('*.log'))  # file extension log only


def find_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:  # open file as read mode, encoding is optional.
        with mmap(file.fileno(), length=0, access=ACCESS_READ) as mp:  # length 0 means whole file
            for word in WORDS:  # search each word in words list
                if mp.find(bytes(word, 'utf-8')) != -1:
                    return word, str(file_name)  # return file name and first matched word


def word_search_from_source():
    pool_results = []

    with Pool() as pool:
        pool_results += pool.map(find_word, file_list())

    search_results = [result for result in pool_results if result]  # [('source\\test1.log', 'where are you?'), ('source\\test4.log', 'where are you?'), ('source\\test5.log', 'pycor')]
    return search_results


if __name__ == '__main__':
    logging.basicConfig(filename='log/search_word.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    search_results = word_search_from_source()
    message = '\n'.join([f'Word: {result[0]} @ {result[1]}' for result in search_results])  # word: where are you? @ source\test1.log
    logging.info(f'Message:\n{message}')

    if (message):
        notification = Notification()
        notification.send_notification(message)
