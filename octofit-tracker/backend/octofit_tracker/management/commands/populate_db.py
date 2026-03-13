from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        teams = [
            {"name": "Marvel", "description": "Team Marvel"},
            {"name": "DC", "description": "Team DC"}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Activities
        activities = [
            {"user": "Spider-Man", "activity": "Running", "duration": 30},
            {"user": "Iron Man", "activity": "Cycling", "duration": 45},
            {"user": "Wonder Woman", "activity": "Swimming", "duration": 60},
            {"user": "Batman", "activity": "Yoga", "duration": 40}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 120}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"user": "Spider-Man", "workout": "Push-ups", "reps": 50},
            {"user": "Iron Man", "workout": "Sit-ups", "reps": 40},
            {"user": "Wonder Woman", "workout": "Squats", "reps": 60},
            {"user": "Batman", "workout": "Pull-ups", "reps": 30}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
