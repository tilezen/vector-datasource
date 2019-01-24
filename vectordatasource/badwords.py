from ahocorasick import Automaton
from vectordatasource.confusables import CONFUSABLES
import unicodedata


# the set of printable codepoints.
#
# deliberately leaves out:
#  - marks, i.e: accents and so forth. this rules out a whole class of
#        near-homoglyph attacks.
#  - spaces, because there's lots of ways to hide bad stuff in places
#        that by definition aren't printed! zero-width space is a
#        particular favourite of people trying to circumvent bad words
#        lists.
PRINTABLE = set([
    'Lu', 'Ll', 'Lt', 'Lm', 'Lo',  # TODO: remove Lm = Letter Modifier?
    'Nd', 'Nl', 'No',
    'Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po',
    'Sm', 'Sc', 'Sk', 'So',  # TODO: remove Sk = Symbol Modifier?
])


def _normalise(word):
    """
    Normalise a word by removing as many homoglyphs as possible.

    Returns a UTF-8 encoded str!
    """

    assert isinstance(word, unicode)

    # in NFKD form, compatible codepoint sequences are decomposed (i.e:
    # ligature 'ff' is decomposed into two 'f' codepoints), and combining
    # characters are left as separate codepoints. this allows us to strip
    # them off easily.
    word = unicodedata.normalize('NFKD', word)

    # build the new word by replacing confusable characters with canonical
    # equivalents, skipping anything that isn't letter-like.
    new_word = u''
    for codepoint in word:
        if unicodedata.category(codepoint) in PRINTABLE:
            new_word += CONFUSABLES.get(codepoint, codepoint)

    return new_word.lower().encode('utf-8')


class BadWords(object):

    def __init__(self, words):
        # we store the words in an Aho-Corasick automaton, which allows for
        # very fast substring searching. NOTE: pyahocorasick _requires_ that
        # we use raw strings, and won't work with unicode in python 2.7. yet
        # another good reason to move to Python 3.
        self.automaton = Automaton()
        for word in words:
            if not isinstance(word, unicode):
                raise TypeError("BadWords takes a list of unicode, not %r"
                                % (type(word)))

            self.automaton.add_word(_normalise(word), None)

        # finalise the automaton to "compile" it.
        self.automaton.make_automaton()

    def is_bad(self, word):
        if not isinstance(word, unicode):
            raise TypeError("BadWords.is_bad takes a unicode, not %r"
                            % (type(word)))

        # this is just a way of returning true if there is _any_ match. the
        # library doesn't seem to have a method for this.
        for _, _ in self.automaton.iter(_normalise(word)):
            return True
        return False
