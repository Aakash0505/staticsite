from django.core.mail import send_mail as core_send_mail
from django.core.mail import EmailMultiAlternatives, EmailMessage
import threading
from email.mime.text import MIMEText


class EmailThread(threading.Thread):
    def __init__(self, subject, template_object, from_email, to,
                 resume, fail_silently):
        super(EmailThread, self).__init__()
        self.subject = subject
        self.to = to
        self.from_email = from_email
        self.template_object = template_object
        self.resume = resume
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(
            self.subject, self.template_object, self.from_email, self.to)
        # if self.template_object:
        msg.content_subtype = "html"
        if self.resume:
            msg.attach(self.resume.name, self.resume.read())
        msg.send(self.fail_silently)


def send_mail(subject, template_object, from_email, to, resume,
              fail_silently=False, *args, **kwargs):
    EmailThread(subject, template_object, from_email,
                to, resume, fail_silently).start()
