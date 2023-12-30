from datetime import datetime, timezone, timedelta
import pytz


class FakeSubmission:
    # current = FakeSubmission("~RLA~12/31/2023~Written~Uploaded~Conclusion", "Olga Pechuk", "id here",
    #                      "2023-12-10T20:45:46Z")
    def __init__(self, comment, student_name, student_id, submission_time):
        self.comment_list = comment[1:].split("~")
        self.submission_class = self.comment_list[0].lower()
        self.due_date = self.comment_list[1]
        self.feedback_type = self.comment_list[2].lower()
        self.rubric = self.comment_list[3].lower()
        self.student_name = student_name
        self.student_id = student_id
        self.submission_time = datetime.strptime(submission_time, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc).astimezone(tz=pytz.timezone('US/Pacific'))
        self.submission_weekday = datetime.weekday(self.submission_time)

    def get_shift(self):

        if self.submission_weekday == 3 and self.submission_time.hour >= 16:
            return "weekend"
        elif self.submission_weekday == 4:
            return "weekend"
        elif self.submission_weekday == 5 and self.submission_time.hour <= 16:
            return "weekend"
        else:
            return "weekday"

    def get_feedback_due(self):
        if self.submission_time.hour <= 16:
            return str((self.submission_time + timedelta(days=1)).date())
        else:
            return str((self.submission_time + timedelta(days=2)).date())


class Submission:
    def __init__(self, submission_object):
        # try:
        #     if comments[0]["author_id"] != submission.user_id:
        #         print("OH NO!")
        #         raise Exception("Author didn't submit comment")
        #
        #     print(comments[0]["author_name"], submission.attachments[0], submission.submitted_at)
        #
        # except:
        #     print("Something's wrong")
        # print(comments[0]["author_name"], comments[0]["comment"],
        #       list(attachment.url for attachment in submission.attachments), submission.submitted_at)

        self.comment_text = submission_object.submission_comments[-1]["comment"].replace("\n", "")
        self.comment_list = self.comment_text[1:].split("~")
        self.submission_class = self.comment_list[0].lower().strip(" ")
        self.due_date = self.comment_list[1].strip(" ")
        self.feedback_type = self.comment_list[2].lower().strip(" ")
        self.rubric = self.comment_list[3].lower().strip(" ")
        self.student_name = submission_object.submission_comments[-1]["author_name"]
        self.student_id = submission_object.user_id
        self.submission_time = datetime.strptime(str(submission_object.submitted_at), "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc).astimezone(tz=pytz.timezone('US/Pacific'))
        self.submission_weekday = datetime.weekday(self.submission_time)

    def get_shift(self):

        if self.submission_weekday == 3 and self.submission_time.hour >= 16:
            return "weekend"
        elif self.submission_weekday == 4:
            return "weekend"
        elif self.submission_weekday == 5 and self.submission_time.hour <= 16:
            return "weekend"
        else:
            return "weekday"

    def get_feedback_due(self):
        if self.submission_time.hour <= 16:
            return str((self.submission_time + timedelta(days=1)).date())
        else:
            return str((self.submission_time + timedelta(days=2)).date())
