from django.test import TestCase
from analyser import views
from django.core.urlresolvers import reverse
try: import cPickle
except: import pickle as cPickle
import pickle
import os.path as path

class ViewsTestCase(TestCase):

  def test_welcome_view(self):
    """Welcome view is rendered correctly"""
    url = reverse('welcome')
    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)

  def test_home_view(self):
    """Home view is rendered correctly"""
    url = reverse('home')
    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)

  def test_graph_view(self):
    """Graph view is rendered correctly"""
    url = reverse('graph')
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "..",  "resources.txt"))

    # Write data to resource file to test data rendering
    with open(filepath, 'wb') as f:
            cPickle.dump(('packages', ['mac', 'debian']), f, protocol=cPickle.HIGHEST_PROTOCOL)

    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)