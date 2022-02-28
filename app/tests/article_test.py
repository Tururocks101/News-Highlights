import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_article=Articles('Kenyans stuck in Ukraine ,trying to survive','slyvia', 'this is a description' ,'https://www.google.com','https://www.google.com/image', '2022-02')

    def test_instance(self):
        '''
        '''
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_init(self):
        '''
        '''
        self.new_article.title = 'Kenyans stuck in Ukraine ,trying to survive'
        self.new_article.author = 'slyvia'
        self.new_article.description = 'this is a description'
        self.new_article.url = 'https://www.google.com'
        self.new_article.url_to_image = 'https://www.google.com/image'
        self.new_article.published_at = '2022-02'