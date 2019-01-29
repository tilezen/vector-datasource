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


# the set of breakable codepoints, which might indicate separation between
# words.
BREAKABLE = set([
    'Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po',  # punctuation
    'Zl', 'Zp', 'Zs',  # space / separator
])


def _normalise(word, preserve_breaks=False):
    """
    Normalise a word by removing as many homoglyphs as possible.

    If preserve_breaks is truthy, then breaking codepoints (spaces,
    punctuation) will be converted into spaces. This means that they can
    be used to anchor "exact" words.
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
        cat = unicodedata.category(codepoint)
        if cat in PRINTABLE:
            new_word += CONFUSABLES.get(codepoint, codepoint)
        elif preserve_breaks and cat in BREAKABLE:
            new_word += u' '

    return new_word.lower()


def _break_sentence(sentence):
    word = u''

    for codepoint in sentence:
        if unicodedata.category(codepoint) in BREAKABLE:
            if word:
                yield word
                word = u''
        else:
            word += codepoint
    if word:
        yield word


def _build_automaton(words):
    automaton = Automaton()
    for word in words:
        if not isinstance(word, unicode):
            raise TypeError("BadWords words should be a list of unicode"
                            ", not %r" % (type(word)))

        norm_str = _normalise(word).encode('utf-8')
        automaton.add_word(norm_str, word)

    # finalise the automaton to "compile" it.
    automaton.make_automaton()
    return automaton


class BadWords(object):

    def __init__(self, words=[], exact_words=[]):
        # we store the words in an Aho-Corasick automaton, which allows for
        # very fast substring searching. NOTE: pyahocorasick _requires_ that
        # we use raw strings, and won't work with unicode in python 2.7. yet
        # another good reason to move to Python 3.
        if words:
            self.automaton = _build_automaton(words)
        else:
            self.automaton = None

        # exact words need to match at the string start/end and word
        # boundaries, which is a little more complicated than searching as a
        # simple substring. at the moment, storing them in a map allows a
        # naive implementation, but we might want to figure out a more
        # efficient way of doing this.
        self.exact_words = {}
        for word in exact_words:
            if not isinstance(word, unicode):
                raise TypeError("BadWords exact_words should be a list of "
                                "unicode, not %r" % (type(word)))

            norm = _normalise(word, preserve_breaks=True)
            self.exact_words[norm] = word

    def check(self, word):
        """
        Checks for a bad word. If there is at least one, then it returns one.
        If no bad words were found, returns None.
        """

        if not isinstance(word, unicode):
            raise TypeError("BadWords.check takes a unicode, not %r"
                            % (type(word)))

        # we just return the first - it's possible there's a bunch more.
        if self.automaton:
            norm_str = _normalise(word).encode('utf-8')
            for _, value in self.automaton.iter(norm_str):
                return value

        for k, v in self.exact_words.iteritems():
            norm = _normalise(word, preserve_breaks=True)
            if k == norm or \
               norm.startswith(k + u' ') or \
               norm.endswith(u' ' + k) or \
               (u' ' + k + u' ') in norm:
                return v

        return None

    def is_bad(self, word):
        if not isinstance(word, unicode):
            raise TypeError("BadWords.is_bad takes a unicode, not %r"
                            % (type(word)))

        return self.check(word) is not None
