
from tweet import send_tweet

DEBUG = False

QUEUE_FILE = '/home/krother/Desktop/Academis/PR/posts_shuffled.txt'

def get_first():
    lines = open(QUEUE_FILE).readlines()
    first = lines.pop(0)
    return first.strip()

def rotate():
    lines = open(QUEUE_FILE).readlines()
    first = lines.pop(0)
    lines.append(first)
    open(QUEUE_FILE, 'w').writelines(lines)

if __name__ == '__main__':
    tweet = get_first()
    if DEBUG:
        print tweet
    else:
        send_tweet(tweet)
    rotate()


