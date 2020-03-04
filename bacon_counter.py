from mrjob.job import MRJob
class Bacon_count(MRJob):
    #"map" | "filter"
    # "list comprehension"
    def mapper(self, _, line):
        for word in line.split():
            if word.lower().replace('.', '') == 'bacon':
                # async / asynchronous / N'SYNC / lazy evaluation
                # "Promise"
                yield ('bacon', 1)
    def reducer(self, key, values):
        #reduction is like aggregation:
        #reducing many values, to one value
        # "sum"
        yield (key, sum(values))
if __name__ == '__main__':
    Bacon_count.run()
