from django.shortcuts import render 
from .forms import ContactForm
from django.core.mail import send_mail


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['isadbc42@gmail.com']
			if cc_myself:
				recipients.append(sender)

			#TODO: Configurar no arquivo settings.py as credenciais para envio de e-mails
			#send_mail(subject, message, sender, recipients)
			context = {
				'form':form,
			}
			return render(request, 'treasure/thanks.html', context)
			
		context = {
				'form':form,
		}
	else:
		form = ContactForm()
		context = {'form':form,}

	return render(request, 'treasure/contact.html', {'form': form})

def index(request):
	context = {}
	return render (request, 'base.html', context)


