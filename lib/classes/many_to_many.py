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
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, "_title"):
            self._title = title


    @property
    def author(self):
        return self._author
    

    @author.setter
    def author(self, author):
        if isinstance(author, Author):#ensure the author is an instance of Author class
            self._author = author
        else:
            raise TypeError("the author must be an instance of the Author class")
        

    @property
    def magazine(self):
        return self._magazine
    

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):#ensure the magazine is an instance of the Magazine class
            self._magazine = magazine
        else:
            raise TypeError("the magazine must be an instance of the Magazine class")
           


    















class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        self._magazines = []


    @property
    def name(self):
        return self._name
    
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name
            
        
   
    # def articles(self):
    #     return self._articles
    
    
    # def articles(self, articles):
    #     if isinstance(articles, Article):
    #         self.articles = articles



    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        self._magazines.append(magazine)
        if magazine not in self._magazines:
            self._magazines.append(magazine)
            return new_article


    def topic_areas(self):
        if not self._articles:
            return None
        categories = {article.magazine.category for article in self._articles}
        return list(categories)
        
        pass


















class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2<= len(name) <=16 and not hasattr(self, "_name"):
            self._name = name


    @property
    def category(self):
        return self.category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) >0:
            self._category = new_category
        pass

    @property
    def magazines(self):
        return self._magazines
    @magazines.setter
    def magazines(self, magazines):
       if isinstance(magazines, Magazine):
        self._magazines = magazines

    def articles(self):
        
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass