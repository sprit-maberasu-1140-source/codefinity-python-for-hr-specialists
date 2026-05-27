def print_survey_summary(survey_responses):
    if not survey_responses:
        average_score = "No responses"
        counts = {}
    else:
        total = sum(survey_responses)
        count = len(survey_responses)
        average_score = total / count
        counts = {}
        for score in range(1, 6):
            counts[score] = survey_responses.count(score)
    summary = f"Average Satisfaction Score: {average_score}"
    print(summary)
    print("Score Counts:")
    for score in range(1, 6):
        count = counts.get(score, 0)
        line = f"  {score}: {count}"
        print(line)

responses = [4, 3, 5, 2, 4, 3, 5, 1, 4, 2]
print_survey_summary(responses)

empty_responses = []
print_survey_summary(empty_responses)