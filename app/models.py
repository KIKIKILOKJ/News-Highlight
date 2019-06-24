class Business:
    """
    Class to define the display of the business news
    """
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
class Headlines:
    """
    Class to define the display of the major headlines
    """
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
class Sources:
    """
    Class define the display of all the news sources available
    """
    def __init__(self, id, name, url, country, description):
        """
        This method allows us to instantiate an instance.
        """
        self.id = id
        self.name = name
        self.url = url
        self.country = country
        self.description = description


class Everything:
    """
    Class to define the display of all the news
    """
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt