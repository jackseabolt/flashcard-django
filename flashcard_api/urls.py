from django.urls import path

from flashcard_api import views

urlpatterns = [
    path('flashcards/', views.FlashcardAPIView.as_view())
]