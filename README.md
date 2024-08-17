# Rmotrgram
  *This project is part of the [INE](my.ine.com) x [SDA](https://t.co/zI6rJymObV) Data Science Program, [Object-Oriented Programming with Python](https://my.ine.com/DataScience/courses/26ad63e1/object-oriented-programming-with-python).*

**Rmotrgram** is a simple social network clone built in Python, similar to a popular social media platform. It allows users to create and view different types of posts, follow other users, and get a timeline of posts from users they follow.

## Features
- User Creation: Users can be created with a first name, last name, and email.
- Follow Users: Users can follow other users.
- Timeline: A user’s timeline displays posts from the users they follow, sorted by the most recent posts.
- Posts: Users can create different types of posts:
  - TextPost: A simple text-based post.
  - PicturePost: A post with text and an image URL.
  - CheckInPost: A post with text and geographic coordinates.
  
## Project Structure
- **`social_network` Folder**: Contains the core classes for the social network.
  - **`accounts.py`**: Defines the `User` class.
  - **`posts.py`**: Defines the `Post`, `TextPost`, `PicturePost`, and `CheckInPost` classes.

- **`main.py`**: The script that demonstrates the functionality of the social network by creating users, posts, and showing timelines.

## Sample Run

```
### John's timeline
@Paul McCartney: Check my new guitar
        imgur.com/guitar.png
        Saturday, Aug 17, 2024
@Paul McCartney: At 20 Forthlin Road
        20.111, -10.2222
        Saturday, Aug 17, 2024
@Paul McCartney: At Abbey Road Studios
        19.111, -9.2222
        Saturday, Aug 17, 2024
@George Harrison: My guitar gently weeps...
        Saturday, Aug 17, 2024
@George Harrison: For you, I'd go full blue...
        Saturday, Aug 17, 2024
```
