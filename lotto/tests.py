from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate()
        print(g.update_date)
        print(g.lottos)

        #실제 Test case (ok or failed)
        #dafault로 6개 숫자 x 5set = 30개의 숫자가 생성된을 확인
        self.assertTrue(len(g.lottos) > 20)
