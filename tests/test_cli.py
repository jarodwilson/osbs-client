import sys

from osbs.cli.main import str_on_2_unicode_on_3


class TestStrOn2UnicodeOn3(object):
    def test_force_str(self):
        b = b"s"
        if sys.version_info[0] == 3:
            s = "s"
            assert str_on_2_unicode_on_3(s) == s
            assert str_on_2_unicode_on_3(b) == s
        else:
            s = u"s"
            assert str_on_2_unicode_on_3(s) == b
            assert str_on_2_unicode_on_3(b) == b
