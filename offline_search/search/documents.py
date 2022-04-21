from collections import Counter
from dataclasses import dataclass
from .analyzer import analyze


@dataclass
class Abstract:
    """ Abstract class for Data """
    ID: int
    title: str
    topic_ID: int
    content: str

    @property
    def full_text(self):
        return ' '.join([self.title, self.content])

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.full_text))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)


