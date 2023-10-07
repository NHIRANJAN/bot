from django.shortcuts import render,redirect
import re
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import ChatbotResponse
from .models import ChatHistory
def send_email(request):
    subject = 'Subject of the Email'
    message = 'This is the message body of the email.'
    from_email = 'your-email@gmail.com'
    recipient_list = ['recipient@example.com']  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return HttpResponse('Email sent successfully.')
def chatbot(request):
    last_user_message_index = -1  # Default value if no user messages exist
    user_input = request.POST.get('user_input')
    bot_response = get_bot_response(user_input)

    # Save the interaction to the database
    if user_input is not None:
        chat_history = ChatHistory( user_input=user_input, bot_response=bot_response)
        chat_history.save()
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        if user_input is not None:
            # Process user input and get a bot response (you can use your logic here)
            bot_response = get_bot_response(user_input)

            # Store the user interaction in the database
            

            messages = request.session.get('chat_messages', [])
            messages.append({'user': True, 'text': user_input})
            messages.append({'user': False, 'text': bot_response})
            request.session['chat_messages'] = messages

            # Update the last_user_message_index
            last_user_message_index = len(messages) # Index of the last user message
    chat_history_entries = ChatHistory.objects.all().order_by('-timestamp') 
 # Debugging statement
    messages = request.session.get('chat_messages', [])
    return render(request, 'chatbot.html', {'messages': messages, 'last_user_message_index': last_user_message_index, 'chat_history_entries': chat_history_entries})

from fuzzywuzzy import fuzz
def get_bot_response(user_input):
    # Define a list of unwanted words or stop words
    unwanted_words = ["tell", "me", "about", "please", "explain","describe","meant","list","can","be","consumed","eaten","provide","give",
                      "show","what","is","the","in","for","to","of","on","at","with","by","it","its","they","then","their","a","an","as","you","your","how","why","when","where","which"
                      "details","detail","healthy","from","are"]

    print("User Input:", user_input)  # Add this line for debugging
    if user_input is not None:
    # Convert user input to lowercase and split it into words
        input_words = user_input.lower().split()

    # Filter out unwanted words
        base_keyword = [word for word in input_words if word not in unwanted_words]

    # Convert the base keyword back to a string
        base_keyword = " ".join(base_keyword)

    # Get all responses from the database
        all_responses = ChatbotResponse.objects.all()

    # Find the best response based on similarity with the base keyword
        best_match = None
        best_score = 0

        for response in all_responses:
            similarity_score = fuzz.ratio(base_keyword,response.input_text)
            # print(response)
            # print(similarity_score)
            if similarity_score > best_score:
                best_match = response.response_text
                best_score = similarity_score
                print(best_score)
                print(best_match)

        
        if best_score>60:
            bot_response=best_match
            return bot_response
        else:
            return "Does not have respond that"
    else:
        # Handle the case when user_input is None or empty
        return "User input is empty or None"

from django.shortcuts import render
from .models import ChatHistory  # Import the ChatHistory model

def chat_history(request):
    # Retrieve chat history entries from the database, ordered by timestamp
    chat_history_entries = ChatHistory.objects.all().order_by('-timestamp')

    # Render the chat history template and pass the entries as context
    return render(request, 'history.html', {'chat_history_entries': chat_history_entries})
def delete_entry(request, entry_id):
    try:
        entry_to_delete = ChatHistory.objects.get(id=entry_id)
        entry_to_delete.delete()
    except ChatHistory.DoesNotExist:
        pass  # Handle the case when the entry does not exist (optional)

    return redirect('chatbot')  
from django.core.mail import send_mail
from django.http import HttpResponse

def test_page(request):
    return render(request, 'test.html')
