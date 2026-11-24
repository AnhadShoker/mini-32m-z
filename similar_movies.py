import sys 
import math

def similarity(vector_1, vector_2):
    """Returns the cosine similarity of vector1 and vector2, two lists of numbers of the same length.
    If either vector is all zeros, the similarity is 0.0.0"""
    dot_product = 0.0
    sum_squares1 = 0.0 
    sum_squares2 = 0.0
    for i in range(len(vector_1)):
        dot_product = dot_product + vector_1[i] * vector_2[i] 
        sum_squares1 = sum_squares1 + vector_1[i] * vector_2[i]
        sum_squares2 = sum_squares2 + vector_2[i] * vector_2[i]
    if sum_squares1 == 0.0 or sum_squares2 == 0.0:
        return 0.0 
    return dot_product / (math.sqrt(sum_squares1) * math.sqrt(sum_squares2))

def main():
    if len(sys.argv) != 2:
        print("usage: python3 similar_movies.py MOVIE_ID")
        return #checks whether the user has entered a movie_id or not 
    movie_id = int(sys.argv[1])
    #sys.argv[0] = program's name
    #sys.argv[1] = first word after it
    #python similar_movies.py 20102 --> sys.argv = ['similar_movies.py', 20102]
    #spaces split arguments 




if __name__ == "__main__":
    main()