from django.db import models

class Deck(models.Model):
    name       = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    deck       = models.ForeignKey(Deck, related_name='cards', on_delete=models.CASCADE)
    front      = models.CharField(max_length=255)
    back       = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.deck} : {self.back}'

class State(models.Model):
    card          = models.ForeignKey(Card, related_name='states',on_delete=models.CASCADE)
    answered      = models.BooleanField(default=False)
    correct       = models.BooleanField(null=True)
    front_of_card = models.BooleanField(null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    @classmethod
    def there_is_an_active_question(cls):
        return not cls.objects.last().answered
