import media
import fresh_tomatoes

"""
This file is the place where instances of Movie
class are created and passed onto
a list which will be used to generate
html page dynamically
"""
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/"
                        "Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        120)

avatar = media.Movie("Avatar",
                     "Story of aliens",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/"
                     "Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     145)

enter_the_dragon = media.Movie("Enter The Dragon",
                               "Bruce Lee",
                               "https://upload.wikimedia.org/wikipedia/en/"
                               "thumb/e/ef/Enter_the_dragon.jpg/220px"
                               "-Enter_the_dragon.jpg",
                               "https://www.youtube.com/watch?v=81jCPIag4KA",
                               175)

predator = media.Movie("Predator",
                       "Monster attack",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/"
                       "Predator_Movie.jpg/220px-Predator_Movie.jpg",
                       "https://www.youtube.com/watch?v=Y1txEAywdiw",
                       165)

troy = media.Movie("Troy",
                   "Hector v/s Achillies",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/"
                   "Troy2004Poster.jpg/220px-Troy2004Poster.jpg",
                   "https://www.youtube.com/watch?v=znTLzRJimeY",
                   123)

lordofrings = media.Movie("Lord of The Rings",
                          "Magic ring",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/thumb/8/87/Ringstrilogyposter.jpg/"
                          "220px-Ringstrilogyposter.jpg",
                          "https://www.youtube.com/watch?v=V75dMMIW2B4",
                          135)

movie_list = [toy_story, avatar, enter_the_dragon, predator, troy, lordofrings]


fresh_tomatoes.open_movies_page(movie_list)
