from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as dj_messages
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'messaging/message_detail.html', {'message': message})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            dj_messages.success(request, "Mensagem enviada com sucesso!")
            return redirect('inbox')
    else:
        form = MessageForm(user=request.user)
    return render(request, 'messaging/send_message.html', {'form': form})
