from django.http import JsonResponse ,HttpResponse
from cryptography.fernet import Fernet
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EncryptAPIView(APIView):
    def post(self, request):
        text = request.data.get('text', '')  # Use request.data to get POST data in DRF

        if not text:
            return Response({'error': 'text field is required'}, status=status.HTTP_400_BAD_REQUEST)

        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode('utf-8'))

        response_data = {
            'key': key.decode('utf-8'),
            'encrypted_text': encrypted_text.decode('utf-8')
        }

        return Response(response_data, status=status.HTTP_200_OK)


def encrypt_view(request):
    if request.method == 'POST':
        text = request.POST['text']
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode('utf-8'))
        return JsonResponse({'key': key.decode('utf-8'), 'encrypted_text': encrypted_text.decode('utf-8')})

def decrypt_view(request):
    if request.method == 'POST':
        key = request.POST['key'].encode('utf-8')
        encrypted_text = request.POST['encrypted_text'].encode('utf-8')
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode('utf-8')
        return JsonResponse({'decrypted_text': decrypted_text})

class DecryptAPIView(APIView):
    def post(self, request):
        key = request.data.get('key', '')
        encrypted_text = request.data.get('encrypted_text', '')

        if not key or not encrypted_text:
            return Response({'error': 'Both "key" and "encrypted_text" fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            key = key.encode('utf-8')
            encrypted_text = encrypted_text.encode('utf-8')
            cipher_suite = Fernet(key)
            decrypted_text = cipher_suite.decrypt(encrypted_text).decode('utf-8')

            response_data = {'decrypted_text': decrypted_text}
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': 'Decryption failed: {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)

def encrypt_form_view(request):
    return render(request, 'encrypt.html')

def decrypt_form_view(request):
    return render(request, 'decrypt.html')
