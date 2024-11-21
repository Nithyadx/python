import pytest

class TestClass:

    @pytest.fixture
    def setup(self):
        print("launching browser")
        print("open application..")
    def test_login(self,setup):
        print("this is login test")
    def test_search(self,setup):
        print("this is search test")
    def test_Advancedsearch(self,setup):
        print("this is advanced search test")
