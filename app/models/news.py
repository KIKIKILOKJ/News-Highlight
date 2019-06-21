class News:
    """
    News class to define news objects
    """
    def __init__(self,id,name,author,title,description,url,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        