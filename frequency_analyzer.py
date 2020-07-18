class ASCIIBuilder(object):
    @staticmethod
    def build_ASCII(starting_char, length):
        chars = []
        char = starting_char
        for i in range(length):
            chars.append(char)
            char = chr(ord(char) + 1)
        return chars


class CharFrequencyAnalyzer(object):

    def __init__(self):
        self._allowed_alpha = []
        self._current_map = {}
        self._build_alpha()



    def _build_alpha(self):
        raise NotImplementedError()

    def _mutate_char(self,c):
        raise NotImplementedError()

    def is_char_allowed(self, c):
        return c in self._allowed_alpha

    def process_text(self, text):
        for line in text.splitlines():
            for c in line:
                if self.is_char_allowed(c):
                    c = self._mutate_char(c)

                    self._current_map[c] = self._current_map.get(c, 0) + 1

    def compute_statistics(self):
        total_counts = sum(self._current_map.values()) * 1.0
        return [total_counts, {k: v * 100 / total_counts for k, v in self._current_map.items()}]


class EnglishAlphaFrequencyAnalyzer(CharFrequencyAnalyzer):

    def _mutate_char(self, c):
        return c.lower() if c.isupper() else c

    def _build_alpha(self):
        # Small Chars
        self._allowed_alpha += ASCIIBuilder.build_ASCII('a', 26)
        # Capital Chars
        self._allowed_alpha += ASCIIBuilder.build_ASCII('A', 26)


class ArabicAlphaFrequencyAnalyzer(CharFrequencyAnalyzer):
    def __init__(self):
        super().__init__()
        self._groups = [
            ('ا', 'أ', 'إ', 'آ'),
            ('و', 'ؤ'),
            ('ى', 'ي'),
            ('ئ', 'ء'),
            ('ة', 'ت'),

        ]

    def _build_alpha(self):
        self._allowed_alpha = ['س','ف','ر','ا','ل','ت','ك','و','ي','ن','ب','د','ء','خ','ق','ه','م','أ','ض','ة','ع','ى','ج','غ','ظ','ح','ص','ط','ذ','ث','إ','ش','ز','آ','ئ','ؤ',]

    def _mutate_char(self, c):
        group = self._get_char_group(c)
        if group is not None:
            return group

        return c


    def _get_char_group(self,c):
        for group in self._groups:
            if c in group:
                return group
        return  None