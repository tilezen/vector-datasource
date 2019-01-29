# -*- encoding: utf-8 -*-
from unittest import TestCase


# to avoid a whole class of errors involving str/unicode and various encoding
# related problems, the BadWords list should only operate on unicode strings.
# it shouldn't make assumptions that any str input is UTF-8. if we want to
# make that assumption, we should do it in other parts of the code.
#
# hopefully this saves us many excruciating hours of debugging.
#
class TestWordsMustBeUnicode(TestCase):

    def test_construct(self):
        from vectordatasource.badwords import BadWords

        with self.assertRaises(TypeError):
            BadWords(['foo'])

    def test_call(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([])
        with self.assertRaises(TypeError):
            badwords.is_bad("foo")


# check that the comparisons with the badwords list work as we'd expect. which
# is to say, that it detects variations of the original bad word that we also
# want to block.
class TestComparison(TestCase):

    def test_identity(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertTrue(badwords.is_bad(u'foo'))

    # def test_substring(self):
    #     # word is bad, even as part of a larger string
    #     from vectordatasource.badwords import BadWords

    #     badwords = BadWords([u'foo'])
    #     self.assertTrue(badwords.is_bad(u'xfoox'))

    def test_starts_with(self):
        # word is bad when it starts a longer word?
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertTrue(badwords.is_bad(u'Fooville'))
        self.assertTrue(badwords.is_bad(u'Footropolis'))

    def test_multiple_words(self):
        # some bad "words" are really bad phrases
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo bar'])
        self.assertFalse(badwords.is_bad(u'foo'))
        self.assertFalse(badwords.is_bad(u'bar'))
        self.assertTrue(badwords.is_bad(u'foo bar'))

        # should it be bad or OK if we drop the space?
        self.assertTrue(badwords.is_bad(u'foobar'))

    def test_space_delimited(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertTrue(badwords.is_bad(u' foo'))
        self.assertTrue(badwords.is_bad(u'foo '))
        self.assertTrue(badwords.is_bad(u' foo '))
        self.assertTrue(badwords.is_bad(u'the foo word'))

    def test_punctuation_delimited(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertTrue(badwords.is_bad(u'bad,foo,word'))
        self.assertTrue(badwords.is_bad(u'foo,'))
        self.assertTrue(badwords.is_bad(u',foo'))

    def test_not_bad(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertFalse(badwords.is_bad(u'fue'))
        self.assertFalse(badwords.is_bad(u'phoo'))
        self.assertFalse(badwords.is_bad(u'fox'))

    def test_case_insensitive(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        for bad_word in (u'Foo', u'FOO', u'fOO'):
            self.assertTrue(
                badwords.is_bad(bad_word), "%r should be detected as a bad "
                "word, but wasn't" % (bad_word,))

    def test_unicode_confusable(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertTrue(badwords.is_bad(u'f00'))

    def test_unicode_zero_width_space(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertTrue(badwords.is_bad(u'fo\u200Bo'))

    def test_unicode_accent(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords([u'foo'])
        self.assertTrue(badwords.is_bad(u'fôó'))


class TestExact(TestCase):

    def test_exact_word(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords(exact_words=[u'foo'])
        self.assertTrue(badwords.is_bad(u'foo'))

    def test_not_match_longer_word(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords(exact_words=[u'foo'])
        self.assertFalse(badwords.is_bad(u'foob'))
        self.assertFalse(badwords.is_bad(u'xfoo'))

    def test_match_when_space_delimited(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords(exact_words=[u'foo'])
        self.assertTrue(badwords.is_bad(u'the foo word'))

    def test_not_match_when_space_delimited_longer_word(self):
        from vectordatasource.badwords import BadWords

        badwords = BadWords(exact_words=[u'foo'])
        self.assertFalse(badwords.is_bad(u'the foob word'))
