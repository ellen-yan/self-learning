import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_incredibles = media.Movie("The Incredibles",
                              "A family of undercover superheroes, while trying to live the quiet suburban life," +
                              " are forced into action to save the world",
                              "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                              "https://www.youtube.com/watch?v=eZbzbC9285I")

lotr_fellowship = media.Movie("The Lord of the Rings: Fellowship of the Ring",
                              "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle Earth from the Dark Lord Sauron",
                              "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                              "https://www.youtube.com/watch?v=V75dMMIW2B4")

forrest_gump = media.Movie("Forrest Gump",
                           "While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

lotr_twotowers = media.Movie("The Lord of the Rings: The Two Towers",
                             "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard",
                             "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                             "https://www.youtube.com/watch?v=LbfMDwc4azU")
movies_list = [toy_story, avatar, the_incredibles, forrest_gump, lotr_fellowship, lotr_twotowers]
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__
print lotr_twotowers.__name__ # doesn't exist

#fresh_tomatoes.open_movies_page(movies_list)
