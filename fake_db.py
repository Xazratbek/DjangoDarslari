# import os
# import django
# import random
# import requests
# import json
# from faker import Faker
# from django.core.files import File
# from django.utils.text import slugify

# # Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()

# from project.models import Project, Review, Tag, Comment
# from users.models import Profil, Skill

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()

# fake = Faker()

# # Pixabay API parameters
# pixabay_api_key = "22968062-150924647d813fab458caf2fb"
# pixabay_base_url = "https://pixabay.com/api/"
# pixabay_params = {
#     "key": pixabay_api_key,
#     "q": random.choice(
#         (
#             "programming",
#             "python",
#             "programming quote",
#             "developer",
#             "programmer",
#             "hacker",
#         )
#     ),  # You can change the search query as needed
#     "image_type": "photo",  # Retrieve one image for each project
# }


# # Function to fetch an image from Pixabay
# # Function to fetch an image from Pixabay with error handling
# def fetch_pixabay_image():
#     try:
#         response = requests.get(pixabay_base_url, params=pixabay_params)
#         response.raise_for_status()  # Raise an exception if the request was not successful

#         data = response.json()
#         if "hits" in data and data["hits"]:
#             image_url = data["hits"][random.randint(0, 15)]["largeImageURL"]
#             response = requests.get(image_url)
#             response.raise_for_status()  # Raise an exception if the image request was not successful
#             return File(response.content)
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred while fetching an image: {e}")
#     except (KeyError, IndexError):
#         print("Invalid response from Pixabay API, no image found.")

#     return None


# # Generate more than 1000 users
# for _ in range(100):
#     user = Profil.objects.create(
#         name=fake.name(),
#         email=fake.email(),
#         info=fake.job(),
#         location=fake.city(),
#         bio=fake.text(),
#         social_github=fake.url(),
#         social_youtube=fake.url(),
#         social_instagram=fake.url(),
#         social_telegram=fake.url(),
#         personal_website=fake.url(),
#         social_linkedin=fake.url(),
#         social_facebook=fake.url(),
#         social_leetcode=fake.url(),
#     )

#     # Create skills for each user
#     for _ in range(4):
#         Skill.objects.create(
#             user=user,
#             name=fake.word(),
#             description=fake.sentence(),
#         )

#     # Create projects for each user
#     for _ in range(random.randint(1, 5)):
#         project = Project.objects.create(
#             user=user,
#             title=fake.catch_phrase(),
#             description=fake.text(),
#             demo_link=fake.url(),
#             source_link=fake.url(),
#             vote_count=random.randint(0, 100),
#             vote_ratio=random.randint(0, 100),
#         )

#         # Add tags to projects
#         for _ in range(random.randint(1, 3)):
#             tag_name = fake.word()
#             tag, created = Tag.objects.get_or_create(name=tag_name)
#             project.tag.add(tag)

#         # Fetch and attach an image from Pixabay
#         project_image = fetch_pixabay_image()
#         if project_image:
#             project.image.save(
#                 slugify(project.title) + ".jpg", project_image, save=True
#             )

#     # Create reviews for projects
#     for project in user.project_set.all():
#         for _ in range(random.randint(1, 3)):
#             Review.objects.create(
#                 user=user,
#                 project=project,
#                 body=fake.text(),
#                 value=random.choice(("+", "-")),
#             )

# print("Fake data generation completed.")
