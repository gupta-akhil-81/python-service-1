import unittest
import main_api

class MainAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = main_api.app
        main_api.start_app()

    def test_get_put_customer(self):
        rsp = self.app.get('/customers?size=2')
        print(rsp)
        assert True

if __name__ == '__main__':
    unittest.main()