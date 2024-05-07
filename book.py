class Book:
    def __init__(self, isbn,title,  publisher, language, num_copies, availability):
        self._title = title
        self._isbn = isbn
        self._publisher = publisher
        self._language = language
        self._num_copies = num_copies
        self._availability = availability

    # Getter and setter methods for title
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    # Getter and setter methods for isbn
    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn

    # Getter and setter methods for publisher
    def get_publisher(self):
        return self._publisher

    def set_publisher(self, publisher):
        self._publisher = publisher

    # Getter and setter methods for language
    def get_language(self):
        return self._language

    def set_language(self, language):
        self._language = language

    # Getter and setter methods for num_copies
    def get_num_copies(self):
        return self._num_copies

    def set_num_copies(self, num_copies):
        self._num_copies = num_copies

    # Getter and setter methods for availability
    def get_availability(self):
        return self._availability

    def set_availability(self, availability):
        self._availability = availability


