import sys

class Movie:
    """This class describes a movie's id, title and genres."""
    def __init__(self, id, title, genres):
        self.id = id 
        self.title = title 
        self.genres = genres 

def main():
    if len(sys.argv) != 2:
        print('usage: python3 find_movie.py "PART OF A TITLE"')
        return
    infile = open("movies.tsv")
    header = infile.readline()
    desired_text = sys.argv[1].lower()
    for line in infile:
        fields = line.removesuffix('\n').split('\t')
        genres = fields[2].split('|')
        assert len(genres) > 0 
        if genres == '(no genres listed)':
            genres = ()
        else: 
            genres = tuple(genres)
        movie = Movie(id = int(fields[0]), title = fields[1], genres = genres)
        if desired_text in movie.title.lower():
            print(f'{movie.id}\t{movie.title}\t{movie.genres}')
    return None 

if __name__ == "__main__":
    main()