
# converter/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from .models import UploadedFile
from .forms import UploadFileForm
from django.core.files.base import ContentFile




@login_required
def get_kakao_files(request):
    social_account = request.user.socialaccount_set.filter(provider='kakao').first()
    if social_account:
        access_token = social_account.socialtoken_set.first().token
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        
        response = requests.get('https://kapi.kakao.com/v2/api/talk/memo/default/send', headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            files = data.get('elements', [])
            return render(request, 'converter/files.html', {'files': files})
        else:
            return render(request, 'converter/files.html', {'error': 'Failed to fetch files'})
    else:
        return redirect('account_login')

@login_required
def download_kakao_file(request, file_url):
    social_account = request.user.socialaccount_set.filter(provider='kakao').first()
    if social_account:
        access_token = social_account.socialtoken_set.first().token
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        
        response = requests.get(file_url, headers=headers)
        
        if response.status_code == 200:
            filename = file_url.split('/')[-1]
            file_content = ContentFile(response.content)
            uploaded_file = UploadedFile(file=file_content, name=filename)
            uploaded_file.save()
            
            return redirect('file_success', file_id=uploaded_file.id)
        else:
            return render(request, 'converter/error.html', {'error': 'Failed to download file'})
    else:
        return redirect('account_login')
    
# converter/views.py


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            uploaded_file = UploadedFile(file=file, name=file.name)
            uploaded_file.save()
            return redirect('upload_success', file_id=uploaded_file.id)
    else:
        form = UploadFileForm()
    return render(request, 'converter/upload.html', {'form': form})

def upload_success(request, file_id):
    uploaded_file = UploadedFile.objects.get(id=file_id)
    return render(request, 'converter/upload_success.html', {'file': uploaded_file})


# Create your views here.
