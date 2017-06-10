from pyspark.mllib.linalg.distributed import *
from pyspark import SparkContext, SQLContext
from pyspark.mllib.linalg.distributed import DistributedMatrix
from pyspark.mllib.linalg import Matrices, Vectors

sc = SparkContext()
matrix_1 = sc.parallelize([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).zipWithIndex()
matrix_2 = sc.parallelize([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).zipWithIndex()
vector_1 = sc.parallelize([[1], [2], [3]]).zipWithIndex()

sqlContext = SQLContext(sc)
matrix_1 = IndexedRowMatrix(matrix_1.map(lambda row: IndexedRow(row[1], row[0]))).toBlockMatrix()
matrix_2 = IndexedRowMatrix(matrix_2.map(lambda row: IndexedRow(row[1], row[0]))).toBlockMatrix()

vector_1 = IndexedRowMatrix(vector_1.map(lambda row: IndexedRow(row[1], row[0]))).toBlockMatrix()


mat_product = matrix_1.multiply(matrix_2)
mat_product_vector = matrix_1.multiply(vector_1)

print mat_product.toLocalMatrix()
print mat_product_vector.toLocalMatrix()





