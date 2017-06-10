import sys

from pyspark.sql import SparkSession
from pyspark.shell import sc

textFile = sc.textFile("test.txt")

print textFile.first()

def parse_file(filename):

    edges = set()

    with open(filename) as f:
        lines = f.read().splitlines()

    is_start_vertex = 0
    for l in lines:
        if is_start_vertex == 1:
            date = l.split(' ')
            src = date[0]
            dst = date[1]
            edges.add((src, dst))
            print "src {} dst {}".format(date[0], date[1])

        if l == "#":
            is_start_vertex = 1

    return edges


if __name__ == "__main__":

    # parse_file("graf.tgf")

    spark = SparkSession.builder.appName("TransitiveClosure").getOrCreate()

    partitions = 2

    tc = spark.sparkContext.parallelize(parse_file("graf.tgf"), partitions).cache()

    edges = tc.map(lambda x_y: (x_y[1], x_y[0]))

    oldCount = 0
    nextCount = tc.count()
    while True:
        oldCount = nextCount
        new_edges = tc.join(edges).map(lambda __a_b: (__a_b[1][1], __a_b[1][0]))
        print new_edges.toDF().show()
        tc = tc.union(new_edges).distinct().cache()
        nextCount = tc.count()
        if nextCount == oldCount:
            break

    print("TC has %i edges" % tc.count())

    spark.stop()




