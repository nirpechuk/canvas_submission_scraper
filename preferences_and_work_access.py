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
RLA = "rla"
CNA = "cna"
SND = "snd"
live = "live"
written = "written"

nir = Nerd("Nir Pechuk",
           "npechuk@davidsononline.org",
           {weekend: no, weekday: neutral},
           {RLA: yes, CNA: no, SND: neutral},
           {live: no, written: neutral}, {})
michael = Nerd("Michael Pechuk",
               "npechuk@davidsononline.org",
               {weekend: no, weekday: neutral},
               {RLA: no, CNA: yes, SND: neutral},
               {live: no, written: neutral}, {"Lincoln Frankel": no})
ron = Nerd("Ron Pechuk",
           "npechuk@davidsononline.org",
           {weekend: no, weekday: neutral},
           {RLA: neutral, CNA: no, SND: neutral},
           {live: no, written: neutral},
           {"Olga Pechuk": yes})

nerdlist = [nir, michael, ron]
