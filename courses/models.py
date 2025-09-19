# courses/models.py

from django.db import models
from django.contrib.auth.models import User

# Modelo para o Curso
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Modelo para a Aula
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField() # Pode ser o texto da aula, link para um vídeo, etc.
    order = models.PositiveIntegerField() # A ordem das aulas no curso

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ['order']

# Modelo para o Progresso do Usuário
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'lesson') # Garante que um usuário só tenha um registro por aula

    def __str__(self):
        status = 'Concluído' if self.completed else 'Em Andamento'
        return f"{self.user.username} - {self.lesson.title} ({status})"