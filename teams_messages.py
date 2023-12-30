import pymsteams


def send_message(name, email, assignment, week, due):
    myTeamsMessage = pymsteams.connectorcard(
        "https://davidsononline.webhook.office.com/webhookb2/53ebf1e7-4890-4eaf-a5e5-1d41cac760e1@0ec5874b-c352-49ff-ba00"
        "-40ef1998e526/IncomingWebhook/0b3f190df98149c48714885142e1bb23/2b91f670-f44c-4d36-925a-6b2696eb7d4c")

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
                            "size": "Medium",
                            "weight": "Bolder",
                            "text": "New Assignment"
                        },
                        {
                            "type": "TextBlock",
                            "text": f"<at>{name}</at>, {assignment}, Week {week}, Feedback Due {due}"
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

    myTeamsMessage.printme()

    # myTeamsMessage.send()