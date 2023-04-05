import datetime


def get_today_string():
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    return datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S')


def create_new_post(post, created=get_today_string()):
    new_post = post.copy()
    new_post['created'] = created

    return new_post


old_post = {'id': 100500, 'author': 'Tymofii Ivashchenko'}
new_post = create_new_post(post=old_post)

print('Old post:', old_post)
print('New post:', new_post)
