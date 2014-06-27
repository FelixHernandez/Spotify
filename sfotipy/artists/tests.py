from django.test import TestCase
from .models import Artist
class TestArtists(TestCase):
	def setUp(self):
		self.artist=Artist.objects.create(First_Name='Vicente',Last_Name='Fernandez')

	def tes_existe_vista(self):
		res=self.client.get('/artists/%d/'%self.artist.id)
		self.assertEqual(res.status_code,200)
		self.assertTrue('david' in res.content)
