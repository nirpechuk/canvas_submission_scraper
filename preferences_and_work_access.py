class Nerd:
    def __init__(self, name, email, shift, classes, feedback, people):
        self.name = name
        self.email = email
        self.shift = shift
        self.classes = classes
        self.feedback = feedback
        self.people = people


neutral = 0
no = -10000
yes = 1
weekend = "weekend"
weekday = "weekday"
live = "live"
written = "written"

nir = Nerd("[nerd name]",
           "[nerd email]",
           {weekend: no, weekday: neutral},
           {[class]: neutral, [class]: no, [class]: neutral},
           {live: no, written: neutral},
           {"[preference person]": yes})
michael = Nerd("[nerd name]",
           "[nerd email]",
           {weekend: no, weekday: neutral},
           {[class]: neutral, [class]: no, [class]: neutral},
           {live: no, written: neutral},
           {"[preference person]": yes})
ron = Nerd("[nerd name]",
           "[nerd email]",
           {weekend: no, weekday: neutral},
           {[class]: neutral, [class]: no, [class]: neutral},
           {live: no, written: neutral},
           {"[preference person]": yes})

nerdlist = [nir, michael, ron]
