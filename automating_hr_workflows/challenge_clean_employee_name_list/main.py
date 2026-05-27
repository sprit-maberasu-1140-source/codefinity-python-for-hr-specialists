def clean_employee_names(names):
    cleaned = []
    for name in names:
        tmp = name.strip().title()
        cleaned.append(' '.join(tmp.split()))
    return cleaned
    pass

names = ["   aLICE   sMith  ", "BOB jOnes", "   carol   JOHNSON", "  dave miller "]
cleaned = clean_employee_names(names)
print(cleaned)
