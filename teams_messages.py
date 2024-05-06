import pymsteams

WEBHOOK = "" #insert webhook here


def invalid_message(error, assignment, week, debug=False):
    name = "" # [your name]
    email = "" # [your email]
    myTeamsMessage = pymsteams.connectorcard(WEBHOOK)
    myTeamsMessage.payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "size": "Large",
                            "weight": "Bolder",
                            "text": "Invalid Submission"
                        },
                        {
                            "type": "TextBlock",
                            "wrap": "true",
                            "text": f"<at>{name}</at>, {assignment}, Assignment Name: {week}, Error: {error}"
                        }
                    ],
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.0",
                    "msteams": {
                        "entities": [
                            {
                                "type": "mention",
                                "text": f"<at>{name}</at>",
                                "mentioned": {
                                    "id": f"{email}",
                                    "name": f"{name}"
                                }
                            },
                        ]
                    }
                }
            }
        ]
    }
    if debug:
        myTeamsMessage.printme()
    else:
        myTeamsMessage.send()


def assignment_message(name, email, assignment, week, due, debug=False):
    myTeamsMessage = pymsteams.connectorcard(WEBHOOK)

    myTeamsMessage.payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "size": "Large",
                            "weight": "Bolder",
                            "text": "New Assignment"
                        },
                        {
                            "type": "TextBlock",
                            "wrap": "true",
                            "text": f"<at>{name}</at>, {assignment}, Assignment Name: {week}, Feedback Due {due} @ 4:00 pm"
                        }
                    ],
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.0",
                    "msteams": {
                        "entities": [
                            {
                                "type": "mention",
                                "text": f"<at>{name}</at>",
                                "mentioned": {
                                    "id": f"{email}",
                                    "name": f"{name}"
                                }
                            },
                        ]
                    }
                }
            }
        ]
    }

    if debug:
        myTeamsMessage.printme()
    else:
        myTeamsMessage.send()
