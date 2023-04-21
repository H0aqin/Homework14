class Film:
    def __init__(self, title, director, year, genre, duration, rating):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration
        self.rating = rating
        self.is_watched = False

    def get_title(self):
        return self.title

    def set_watched(self):
        self.is_watched = True

    def get_info(self):
        info = "Title: {}\nDirector: {}\nYear: {}\nGenre: {}\nDuration: {}\nRating: {}\nWatched: {}\n".format(
            self.title, self.director, self.year, self.genre, self.duration, self.rating, self.is_watched)
        return info

   def upload_file(self, file_path):
       pass
   def get_film_address(self):
           return self.storage_address


def upload_file(self, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    with open(self.storage_address, 'wb') as file:
        file.write(data)
