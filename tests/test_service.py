import os
import shutil

from unittest import TestCase

from finolog.services import FinologService


class PathTest(TestCase):
    pass

    # def test_make_main_service(self):
    #     expected = FinologService(api_token='test', biz_id=123)
    #     actual = str(Path.script_dir())
    #     self.assertEqual(expected, actual)
    #
    # def test_file_access(self):
    #     script_dir = os.path.abspath(os.path.dirname(__file__))
    #     subdir = os.path.join(script_dir, 'test_data')
    #     if Path(subdir).is_dir():
    #         shutil.rmtree(subdir)
    #     os.makedirs(subdir)
    #     file_path = str(Path(subdir)/'file.txt')
    #     content = '123'
    #     open(file_path, 'w').write(content)
    #     test_path = Path.script_dir()/subdir/'file.txt'
    #     actual = open(str(test_path)).read()
    #     self.assertEqual(content, actual)