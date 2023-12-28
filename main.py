from canvasapi import Canvas

# Get into DAO canvas
API_URL = "https://davidsononline.instructure.com/"
API_KEY = "22471~IICIQmCEWpwSKRk8eB0531zGD0hA9hvicDNdSEaZp2fOIoexBj6L6I9mqCwbzsLp"
canvas = Canvas(API_URL, API_KEY)

# Get the Writing Center Course object
course = canvas.get_course(635)

print(course.get_assignments()[16].get_submissions()[0].__dir__())

for submission in course.get_assignments()[16].get_submissions():

    if submission.workflow_state == "graded":
        print(submission.id)

# for assignment in course.get_assignments():
#     print(assignment.name + " - " + str(assignment.get_submissions))
