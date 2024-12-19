from django.shortcuts import render
from .forms import SignatureComparisonForm
from .utils import compare_images

def upload_images(request):
    if request.method == 'POST':
        form = SignatureComparisonForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            score = compare_images(instance.original_image.path, instance.signature_image.path)
            return render(request, 'signature/result.html', {'score': score})
    else:
        form = SignatureComparisonForm()
    return render(request, 'signature/upload.html', {'form': form})
