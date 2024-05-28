from django.db.models import *  #(Model, CharField, ForeignKey, DO_NOTHING,
                                #IntegerField, DateField, TextField, DateTimeField)


class Genre(Model):
    name = CharField(max_length=16, null=False, blank=True)


    def __repr__(self):
        return f"<Genre: {self.name}>"

    def __str__(self):
        return f"{self.name}"



class Movie(Model):
    title = CharField(max_length=185, null=False, blank=True)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)


    def __repr__(self):
        return f"<Movie: {self.title}>"

    def __str__(self):
        return f"{self.title} ({self.released})"