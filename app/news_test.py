import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    
    Test Class to test the behavior of the News class
    '''
    

    def setUp(self):
        
        
        '''
        
        Set up method that will run before every Test
        '''
        
        
        self.new_news = News('bbc-news','BBC news','Minister suspended after grabbing activist','after Mark Field marched out Greenpeace protester during City dinner','http://www.bbc.co.uk/news/uk-politics-48718725','https://ichef.bbci.co.uk/images/ic/1024x576/p07dr7gl.jpg','2019-06-21T11:37:50Z')

    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_news,News))
        

if __name__ == '__main__':
    unittest.main()