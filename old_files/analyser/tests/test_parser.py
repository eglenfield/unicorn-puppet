from django.test import TestCase
from analyser.models import Packages, Users, Volumes
from puppet_parser import test_package_parser, test_users_parser, test_volumes_parser

class ParserTestCase(TestCase):
  def setUp(self):
    testData = {
        "resources":
          [{"resource": "package", "provider": "apt", "title": "test_open-ssl", "versions": ["test_version"]}
           , {"resource": "user", "title": "test_user", "uid": 1, "gid": 100, "groups": [], "shell": "/usr/bin", "comment": "",
              "home": "test_home"}],
        "facts": {
          "mountpoints": {
            "test_volume": {
              "available": "17.19 GiB",
              "available_bytes": 1234567,
              "capacity": "6%",
              "device": "/home/",
              "filesystem": "/",
              "options": [
                "no_options"
              ],
              "size": "18.46 GiB",
              "size_bytes": 1345678910,
              "used": "1.27 GiB",
              "used_bytes": 1363279872
            }
          }
        }
      }
    test_package_parser(Packages, testData)
    test_users_parser(Users, testData)
    test_volumes_parser(Volumes, testData)

  def test_resources_are_correct(self):
    """Packages are correctly parsed and added to database"""
    package_test = Packages.objects.get(title="test_open-ssl")
    volume_test = Volumes.objects.get(volume_name="test_volume")
    user_test = Users.objects.get(title="test_user")
    self.assertEqual(package_test.version, ["test_version"], "Correct version was parsed")
    self.assertEqual(package_test.provider, "apt", "Correct provider was parsed")
    self.assertEqual(package_test.title, "test_open-ssl", "Title is correct")
    self.assertEqual(volume_test.available, "17.19 GiB", "Availability is correct")
    self.assertEqual(volume_test.capacity, "6%", "Capacity parsing is correct")
    self.assertEqual(volume_test.device, "/home/", "Device is correct")
    self.assertEqual(volume_test.used, "1.27 GiB", "Used volume is correct")
    self.assertEqual(user_test.uid, 1, "UID is correct")
    self.assertEqual(user_test.gid, 100, "GID is correct")
    self.assertEqual(user_test.shell, "/usr/bin", "User shell is correct")
    self.assertEqual(user_test.home, "test_home", "Used home is correct")

