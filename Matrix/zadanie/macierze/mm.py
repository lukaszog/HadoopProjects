from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import UltraJSONProtocol
import re
import os

WORD_RE = re.compile(r"[\w']+")

class MRmm(MRJob):
    OUTPUT_PROTOCOL =UltraJSONProtocol
    def mapper_get_kv(self, _, line):
        x = -1
        # yield each word in the line
        print line
        if 'M' in line:
            x = 0
        elif 'L' in line:
            x = 1
        digit = re.search('[0-9]', line)
        if digit is not None:
            m, i, j, v = line.rstrip('\n').split(";")
            if x ==0:
                yield (j, (m, i, v))
            elif x==1:
                yield (i, (m, j, v))
                
    def reducer_mlp_kv(self, word, counts):
        print word, counts
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        yield word, counts

    # discard the key; it is just None
    def reducer_get_sum(self, _, word_count_pairs):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        yield max(word_count_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_kv,
                   reducer=self.reducer_mlp_kv),
            #MRStep(reducer=self.reducer_get_sum)
        ]


if __name__ == '__main__':
    MRmm.run()
