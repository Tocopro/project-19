import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_template(filename):
    with open(filename, ‘r’, encoding=’utf-8') as template_file:
    template_file_content = template_file.read()
    return Template(template_file_content)

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == ‘__main__’:
    main()
