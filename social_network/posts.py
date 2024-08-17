from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp or datetime.now()
        self.user = None

    def set_user(self, user):
        self.user = user


class TextPost(Post):  
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return f'@{self.user.first_name} {self.user.last_name}: {self.text}\n\t{self.timestamp.strftime("%A, %b %d, %Y")}'


class PicturePost(Post):  
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return f'@{self.user.first_name} {self.user.last_name}: {self.text}\n\t{self.image_url}\n\t{self.timestamp.strftime("%A, %b %d, %Y")}'


class CheckInPost(Post):  
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'@{self.user.first_name} {self.user.last_name}: {self.text}\n\t{self.latitude}, {self.longitude}\n\t{self.timestamp.strftime("%A, %b %d, %Y")}'
