with open('alien_invasion/high_score.txt') as file_object:
    high_score = int(file_object.read())

print(f"High score is: {high_score}!!!")