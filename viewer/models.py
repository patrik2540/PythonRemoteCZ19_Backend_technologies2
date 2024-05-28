from django.db.models import *  #(Model, CharField, ForeignKey, DO_NOTHING,
                                #IntegerField, DateField, TextField, DateTimeField)


class Genre(Model):
    name = CharField(max_length=16, null=True, blank=False)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"<Genre: {self.name}>"

    def __str__(self):
        return f"{self.name}"



class Movie(Model):
    title = CharField(max_length=185, null=True, blank=True)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING, null=True)
    rating = IntegerField(null=True, blank=True)
    released = DateField(null=True, blank=True)
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']


    def __repr__(self):
        return f"<Movie: {self.title}>"

    def __str__(self):
        return f"{self.title} ({self.released})"