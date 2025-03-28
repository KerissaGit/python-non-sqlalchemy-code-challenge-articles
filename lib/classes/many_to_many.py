class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise TypeError("Title must be a string between 5 and 50 characters.")
        

        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        if hasattr(self, "_name"):
            raise ValueError("Name cannot be changed once set")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        topics = [article.magazine.category for article in self.articles()]
        if not topics:
            return None
        else:
            return list(set(topics))

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Title must be 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if not len(value) > 0:
            raise ValueError("Category must be greater than 0 characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if not titles:
            return None
        else:
            return titles

    def contributing_authors(self):
        author_article_counts = {}
        for article in self.articles():
            if article.author not in author_article_counts:
                author_article_counts[article.author] = 0
            author_article_counts[article.author] += 1
        authors_more_than_two = [author for author, count in author_article_counts.items() if count > 2]
        return None if not authors_more_than_two else authors_more_than_two