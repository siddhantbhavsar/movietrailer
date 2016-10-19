import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


Inferno = media.Movie("Inferno",
                      "Another case solved by professor Langford",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/6/66/Inferno_%282016_film%29.png/220px-Inferno_%282016_film%29.png",
                      "https://www.youtube.com/watch?v=RH2BD49sEZI")

Martian = media.Movie("Martian",
                      "An astronaut's struggle for survival on planet mars",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")

Ironman = media.Movie("Ironman",
                      "Mr.Stark becomes the Ironman",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Iron_Man_bleeding_edge.jpg/250px-Iron_Man_bleeding_edge.jpg",
                      "https://www.youtube.com/watch?v=8hYlB38asDY")

Bahubali = media.Movie("Bahubali",
                       "A great warrior",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Baahubali_poster.jpg/220px-Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")

movies = [toy_story, avatar, Inferno, Martian, Ironman, Bahubali]
#fresh_tomatoes.open_movies_page(movies)

#print (toy_story.storyline)
#print (avatar.storyline)
#avatar.show_trailer()
#Inferno.show_trailer()
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
