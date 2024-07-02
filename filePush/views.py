import base64
import requests
from django.shortcuts import render, HttpResponse

def filePush(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file_obj = request.FILES['file']
        
        # Read and encode the file content to base64
        file_content = base64.b64encode(file_obj.read()).decode('utf-8')
        file_name = file_obj.name
        mime_type = file_obj.content_type
        data = {
            'files': file_content,
            'fileName': file_name,
            'mimeType': mime_type
        }

        url = 'https://script.google.com/macros/s/AKfycbzs3RV-eX4dMSzWuzM7gu6cZ88QIerOlGc9HP_aJDbIS6otkBcHFnM8iJuK4s7O1Dw/exec'
        
        # Send the JSON data to the Google Apps Script endpoint
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            response_data = response.content.decode('utf-8')  # Get the response data
            print(response_data)  # Print the response data to console
            return HttpResponse('File uploaded successfully to Google Drive.')
        else:
            return HttpResponse('Failed to upload file to Google Drive.')
    
    return render(request, 'upload_form.html')
