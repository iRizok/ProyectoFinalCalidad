import unittest
import proyecto
from unittest import mock
from mock import patch, MagicMock


parameters = {
        'date': {'2008-11-15'},
        'hd': 'True',
        'api_key': '0v2IzxVpfiOGIzKUsnQnmt50RsrdMw4E4HqbkYrV'
    }

data = proyecto.getData(parameters)
mock_parameters = MagicMock()
mock_parameters.parameters = parameters
mock_parameters.json.return_value = data
ReturnValue = ['Adam Block','Arp 273','2008-11-15','image','https://apod.nasa.gov/apod/image/0811/ugc1810crop_block.jpg']

class testProyecto(unittest.TestCase):

    def setUp(self):
       self.patcher = mock.patch('proyecto.getData', MagicMock(return_value=ReturnValue))
       self.patcher.start()

    def testGetAuthor(self):
        self.assertEqual(data['copyright'], proyecto.getData()[0])

    def testGetTitle(self):
        self.assertEqual(data['title'], proyecto.getData()[1])
        
    def testGetDate(self):
        self.assertEqual(data['date'], proyecto.getData()[2])
    
    def testGetType(self):
        self.assertEqual(data['media_type'], proyecto.getData()[3])
        
    def testGetUrl(self):
        self.assertEqual(data['url'], proyecto.getData()[4])
        
    def tearDown(self):
        self.patcher.stop()
      


if __name__ == '__main__':
     unittest.main()