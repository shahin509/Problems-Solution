from django.db import models

class SignatureComparison(models.Model):
    original_image = models.ImageField(upload_to='images/original/')
    signature_image = models.ImageField(upload_to='images/signature/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comparison {self.id}"
