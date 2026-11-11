# mini-32m-z: A Small Subset of MovieLens 32M with Zero-Based Ids

This dataset is a subset of the much larger MovieLens 32M dataset:
https://grouplens.org/datasets/movielens/32m/

To create this dataset, we've selected a subset of regular users with
fairly recent movie ratings.  We've also filtered the dataset in
other ways for pedagogical reasons.  This data cannot be used for
research, and it cannot be used to say anything about the original
dataset.

The `z` stands for zero: **`movie_id` and `user_id` run from 0 with no
gaps**, so they can be used directly as list indexes.  The movie with
`movie_id` 0 can be row 0 of a list, and the user with `user_id` 0 can
be column 0.

> **Note: these are NOT the MovieLens ids.**  The ratings, movies and
> users are the same as in the `mini-32m` dataset used earlier in MSE
> 121, but the ids have been renumbered, so a `movie_id` or `user_id`
> here will not match the same number in `mini-32m` or in MovieLens
> 32M.  The original MovieLens movie id is kept in the `ml_movie_id`
> column of `links.tsv`.  The
> [`mini-32m`](https://github.com/UWaterloo-MSE-121/mini-32m) dataset
> is otherwise identical to this one but keeps the original ids.

## Files

All files are UTF-8 text with one header line.  Fields are separated by
a single tab, and lines end with `\n`.  No field is quoted, no field is
empty, and no field contains a tab.

| File | Rows | Columns |
|---|---|---|
| `ratings.tsv` | 340,221 | `user_id`, `movie_id`, `rating`, `timestamp` |
| `movies.tsv` | 23,136 | `movie_id`, `title`, `genres` |
| `links.tsv` | 23,136 | `movie_id`, `ml_movie_id`, `imdb_id`, `tmdb_id` |

- `user_id` runs from 0 to 981 and `movie_id` from 0 to 23,135, with no
  gaps.  Every movie has at least one rating and every user has at
  least 19 ratings.
- `rating` is on a 5-star scale in half-star steps, from 0.5 to 5.0.
- `timestamp` is in seconds since midnight UTC on January 1, 1970.
- `ratings.tsv` is sorted by `user_id` and then by `timestamp`.
- `genres` is a `|`-separated list chosen from: Action, Adventure,
  Animation, Children, Comedy, Crime, Documentary, Drama, Fantasy,
  Film-Noir, Horror, IMAX, Musical, Mystery, Romance, Sci-Fi, Thriller,
  War, Western.  Movies with no genre have the value
  `(no genres listed)`.
- `imdb_id` is the number from an IMDb URL with the `tt` prefix and
  leading zeros removed.  For example, `114709` is
  https://www.imdb.com/title/tt0114709/.
- `tmdb_id` is the id used by The Movie Database, for example
  https://www.themoviedb.org/movie/862.

## Reading the files

Each line can be split on tabs:

```python
with open("ratings.tsv", encoding="utf-8") as f:
    header = f.readline().removesuffix("\n").split("\t")
    for line in f:
        user_id, movie_id, rating, timestamp = line.removesuffix("\n").split("\t")
```

If you use the `csv` module or pandas instead, turn off quote
handling.  One title begins with a quote mark (`"Sr." (2022)`), and
with the default settings the quote marks are silently removed:

```python
import csv
import pandas as pd

reader = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
movies = pd.read_csv("movies.tsv", sep="\t", quoting=csv.QUOTE_NONE)
```

## Things to watch out for

- **Titles are not unique.**  48 titles appear under more than one
  `movie_id`, for example *War of the Worlds (2005)*.  Use `movie_id`,
  not `title`, to identify a movie.
- **Not every title ends with a year.**  128 titles have no `(YYYY)`
  at the end.
- **Many movies have very few ratings.**  The median movie has 2
  ratings, and 43% of movies have exactly 1.

## Differences from mini-32m

This dataset was made from the comma-separated
[`mini-32m`](https://github.com/UWaterloo-MSE-121/datasets/tree/main/mini-32m) in the MSE 121 datasets repository
by [`convert.py`](https://github.com/UWaterloo-MSE-121/datasets/blob/main/mini-32m-z/convert.py):

- The files are tab-separated instead of comma-separated, and column
  names are in snake_case.
- `movie_id` and `user_id` were renumbered from 0, in order of the
  original MovieLens ids.  `ml_movie_id` holds the original movie id.
  (Running `convert.py` with `--keep-ids` instead produces
  [`mini-32m`](https://github.com/UWaterloo-MSE-121/mini-32m), which
  keeps the original ids.)
- The 8 movies with no TMDb id were removed, along with their 16
  ratings.
- `tmdb_id` is written as an integer (`862` rather than `862.0`).
- Spaces at the start or end of titles were removed (30 titles).

## Citation

To acknowledge use of the dataset in publications, please cite the
following paper:

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets:
History and Context. ACM Transactions on Interactive Intelligent
Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872

This data is made available to MSE 121 students under the same
usage license as the original ML-32M dataset:

# Usage License

Neither the University of Minnesota nor any of the researchers
involved can guarantee the correctness of the data, its suitability
for any particular purpose, or the validity of results based on the
use of the data set. The data set may be used for any research
purposes under the following conditions:

- The user may not state or imply any endorsement from the University of Minnesota or the GroupLens Research Group.
- The user must acknowledge the use of the data set in publications resulting from the use of the data set (see above for citation information).
- The user may redistribute the data set, including transformations, so long as it is distributed under these same license conditions.
- The user may not use this information for any commercial or revenue-bearing purposes without first obtaining permission from a faculty member of the GroupLens Research Project at the University of Minnesota.
- The executable software scripts are provided "as is" without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of them is with you. Should the program prove defective, you assume the cost of all necessary servicing, repair or correction.

In no event shall the University of Minnesota, its affiliates or
employees be liable to you for any damages arising out of the use or
inability to use these programs (including but not limited to loss of
data or data being rendered inaccurate).
