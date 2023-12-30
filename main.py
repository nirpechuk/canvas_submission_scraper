from canvasapi import Canvas
from submission_parser import *
from teams_messages import *
from preferences_and_work_access import nerdlist


def chooseNerd(current, nerdlist):
    scores = {}
    for nerd in nerdlist:
        score = 0
        score += nerd.classes[current.submission_class] * 1
        score += nerd.shift[current.get_shift()] * 1
        score += nerd.feedback[current.feedback_type] * 2
        try:
            score += nerd.people[current.student_name] * 2
        except Exception:
            pass
        scores[nerd] = score
        # TODO: ADD WORK

    return max(scores, key=scores.get)


# Get into DAO canvas
API_URL = "https://davidsononline.instructure.com/"
API_KEY = "22471~IICIQmCEWpwSKRk8eB0531zGD0hA9hvicDNdSEaZp2fOIoexBj6L6I9mqCwbzsLp"
canvas = Canvas(API_URL, API_KEY)

# Get the Writing Center Course object
course = canvas.get_course(635)
assignment = course.get_assignment(33571)
submissions = assignment.get_submissions(include=['submission_comments', 'attempt'])
debug = False

# Get Students
enrollments = course.get_enrollments()
# Build a map of student ID to their name
idToName = dict((e.user_id, e.user['name']) for e in enrollments)

# Go through each ungraded sub
for submission in submissions:

    try:
        # print(submission.workflow_state, submission.attempt)
        if submission.workflow_state != "submitted":
            continue
        if submission.attempt > len(submission.submission_comments):
            raise Exception("No Comment")
        if "Thank you for submitting" in submission.submission_comments[-1]["comment"]:
            continue

        current = Submission(submission)
        chosen_nerd = chooseNerd(current, nerdlist)
        assignment_message(name=chosen_nerd.name,
                           email=chosen_nerd.email,
                           assignment=current.student_name,
                           week="16",
                           due=current.get_feedback_due(),
                           debug=debug)

        submission.edit(
            comment={'text_comment': f'Thank you for submitting! Your word nerd will be {chosen_nerd.name}. '
                                     f'You\'ll receive feedback by {current.get_feedback_due()} at 4 pm PST. '
                                     f'Please reach out to them or Nir Pechuk if you don\'t receive feedback '
                                     f'by then.'})

    except Exception as e:

        invalid_message(error=e,
                        assignment=idToName[submission.user_id],
                        week="16",
                        debug=debug)

        submission.edit(
            comment={'text_comment': f'Thank you for submitting! The automated system has caught an issue with your '
                                     f'submission or comment: \"{e}\". If you need help correcting/understanding this '
                                     f'error, message Nir Pechuk on Teams :). If you don\'t need help, just resubmit a '
                                     f'proper submission to the same assignment.'})
