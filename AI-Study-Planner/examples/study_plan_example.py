import json

study_planner_examples = [
    {
        "goal": "Learn Python Basics",
        "duration": "5 days",
        "output": json.dumps({
            "goal": "Learn Python Basics",
            "duration": "5 days",
            "plan": [
                {"day": 1, "difficulty": "Beginner", "topics": ["Introduction to Python", "Variables"]},
                {"day": 2, "difficulty": "Beginner", "topics": ["Operators", "If-Else"]},
                {"day": 3, "difficulty": "Intermediate", "topics": ["Loops", "Lists"]},
                {"day": 4, "difficulty": "Intermediate", "topics": ["Functions", "Dictionaries"]},
                {"day": 5, "difficulty": "Intermediate", "topics": ["File Handling", "Mini Project"]}
            ]
        }, indent=2)
    },
    {
        "goal": "Learn SQL",
        "duration": "6 days",
        "output": json.dumps({
            "goal": "Learn SQL",
            "duration": "6 days",
            "plan": [
                {"day": 1, "difficulty": "Beginner", "topics": ["SELECT", "Basic Queries"]},
                {"day": 2, "difficulty": "Beginner", "topics": ["WHERE", "ORDER BY"]},
                {"day": 3, "difficulty": "Intermediate", "topics": ["GROUP BY", "Aggregations"]},
                {"day": 4, "difficulty": "Intermediate", "topics": ["JOINS"]},
                {"day": 5, "difficulty": "Intermediate", "topics": ["Subqueries"]},
                {"day": 6, "difficulty": "Advanced", "topics": ["Optimization", "Project"]}
            ]
        }, indent=2)
    }
]