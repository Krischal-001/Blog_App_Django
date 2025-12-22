from django.db import models

# Database Relationships:
# 1:1 (One-to-One) – Each record in Table A is linked to only one record in Table B, and vice versa.
# Example: Each person has one passport.

# 1:N (One-to-Many) – A record in Table A can link to multiple records in Table B, but a record in Table B links to only one record in Table A.
# Example: A teacher can teach many students, but each student has only one teacher.

# N:M (Many-to-Many) – Records in Table A can link to multiple records in Table B, and vice versa.
# Usually requires a junction/association table to store relationships.
# Example: Students can enroll in many courses, and courses can have many students.

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.title