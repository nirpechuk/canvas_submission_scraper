import pymsteams

WEBHOOK = "https://davidsononline.webhook.office.com/webhookb2/53ebf1e7-4890-4eaf-a5e5-1d41cac760e1@0ec5874b-c352" \
          "-49ff-ba00-40ef1998e526/IncomingWebhook/0b3f190df98149c48714885142e1bb23/2b91f670-f44c-4d36-925a" \
          "-6b2696eb7d4c "


def invalid_message(error, assignment, week, debug=False):
    name = "Nir Pechuk"
    email = "npechuk@davidsononline.org"
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
                            "text": f"<at>{name}</at>, {assignment}, Week {week}, Error: {error}"
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
                            "text": f"<at>{name}</at>, {assignment}, Week {week}, Feedback Due {due} @ 4:00 pm"
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
