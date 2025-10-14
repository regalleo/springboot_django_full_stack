from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import requests

def task_list_view(request):
    return render(request, 'tasks/task_list.html')

@csrf_exempt
def suggestion_api(request):
    if request.method != 'POST':
        return JsonResponse({'reply': 'Invalid request method'}, status=405)

    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()

        if not user_message:
            return JsonResponse({'reply': 'Please enter a message!'})

        reply = get_hf_response(user_message)
        return JsonResponse({'reply': reply})

    except Exception as e:
        print("Error in suggestion_api:", e)
        return JsonResponse({'reply': 'Error contacting AI server. Try again later.'})


def get_hf_response(user_message):
    model = settings.HF_MODEL
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}

    payload = {"inputs": user_message}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print(f"HF Status: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("HF raw response:", result)

            # Extract text safely
            if isinstance(result, list) and len(result) > 0:
                text = result[0].get('generated_text', '')
                if text:
                    return text.strip()
            return "Sorry, I couldn't generate a response."

        elif response.status_code == 503:
            return "Model is loading, try again in a few seconds."
        elif response.status_code == 404:
            return "❌ Model not found. Check HF_MODEL in .env"
        elif response.status_code == 401:
            return "🔐 Authentication failed. Check API token."
        else:
            return f"HF API error {response.status_code}: {response.text}"

    except requests.exceptions.Timeout:
        return "HF API request timed out."
    except Exception as e:
        print("HF Exception:", e)
        return "Error calling Hugging Face API."
