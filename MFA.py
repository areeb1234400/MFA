import smtplib
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import requests

# Function to print the banner for the MFA tool
def print_banner():
    print("""
    ████╗ ███╗███████╗████████╗██╗  ██╗
    ██╔══██╗██║██╔════╝╚══██╔══╝██║  ██║
    ██████╔╝██║███████╗   ██║   ███████║
    ██╔═══╝ ██║╚════██║   ██║   ██╔══██║
    ██║     ██║███████║   ██║   ██║  ██║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
    MFA - Advanced Cybersecurity & Social Engineering Tool
    """)

# Function to show options for operations
def show_options():
    print("\nSelect an operation:")
    print("1. Conduct Phishing Attack (Email)")
    print("2. Conduct Vishing Attack (Phone Simulation)")
    print("3. Impersonation Attack Simulation")
    print("4. Bypass MFA (Simulation)")
    print("5. Social Media Reconnaissance")
    print("6. Fake Login Page Attack")
    print("7. SMS Phishing (Smishing)")
    print("8. Exit")

# Simulate a Phishing Attack using email
def phishing_attack(target_email):
    print(f"Initiating phishing attack simulation on {target_email}...")

    phishing_subject = "Urgent: Account Verification Needed"
    phishing_body = """Dear User,

    Your account has been flagged for suspicious activity. Please click the link below to verify your identity and secure your account:

    http://malicious-link.com/verify

    Failure to do so within 24 hours will result in account suspension.

    Regards,
    Security Team"""

    from_email = "attacker@example.com"
    to_email = target_email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_email@gmail.com"  # Replace with actual email address
    smtp_password = "your_password"  # Replace with actual email password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = phishing_subject
    msg.attach(MIMEText(phishing_body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            server.login(smtp_username, smtp_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
        print(f"Phishing email sent to {target_email}.")
    except Exception as e:
        print(f"Failed to send phishing email: {e}")

# Simulate a Vishing Attack (Voice-based phishing) - Placeholder
def vishing_attack(target_phone_number):
    print(f"Initiating vishing attack simulation on {target_phone_number}...")
    vishing_script = """
    Hello, this is your bank's customer service. We noticed some suspicious activity on your account. Please verify your account by providing your PIN.
    """
    print(f"Script: {vishing_script}")

# Simulate an Impersonation Attack (using fake identity)
def impersonation_attack(target_name):
    print(f"Simulating impersonation attack against {target_name}...")
    impersonation_script = """
    Hello, I am John from IT support. I need you to give me access to your system to fix an issue. Please provide your credentials.
    """
    print(f"Impersonation Script: {impersonation_script}")

# Simulate Bypassing Multi-Factor Authentication (MFA) using social engineering
def bypass_mfa(target_name):
    print(f"Simulating bypass of MFA for {target_name}...")
    mfa_bypass_script = """
    Hello, this is Sarah from your company's IT department. We are upgrading our security system, and we need to bypass the MFA to complete the process. Can you provide your secondary verification code?
    """
    print(f"MFA Bypass Script: {mfa_bypass_script}")

# Simulate Social Media Reconnaissance (Collect publicly available information)
def social_media_recon(target_username):
    print(f"Initiating social media reconnaissance for {target_username}...")

    # Simulate collecting publicly available information (just an example)
    recon_info = {
        "LinkedIn": f"https://www.linkedin.com/in/{target_username}",
        "Twitter": f"https://twitter.com/{target_username}",
        "Facebook": f"https://facebook.com/{target_username}",
    }

    print(f"Collected public data for {target_username}:")
    for platform, link in recon_info.items():
        print(f"{platform}: {link}")

# Simulate Fake Login Page Attack
def fake_login_page(target_url):
    print(f"Initiating fake login page attack on {target_url}...")

    fake_page_url = "http://malicious-website.com/fake-login"
    print(f"Redirecting user to: {fake_page_url}")
    print("User credentials will be collected if they attempt to log in.")

# Simulate SMS Phishing (Smishing) Attack
def smishing_attack(target_phone_number):
    print(f"Initiating SMS phishing (smishing) attack simulation on {target_phone_number}...")

    sms_body = """Dear User,

    Your account has been temporarily suspended due to suspicious activity. Please click the link below to restore access:

    http://malicious-link.com/restore

    Regards,
    Security Team"""

    print(f"Sending SMS to {target_phone_number} with the following content:\n{sms_body}")

# Main function
def main():
    print_banner()

    while True:
        show_options()
        choice = input("Enter your choice: ")
        if choice == "1":
            target_email = input("Enter target email for phishing attack: ")
            phishing_attack(target_email)
        elif choice == "2":
            target_phone_number = input("Enter target phone number for vishing attack: ")
            vishing_attack(target_phone_number)
        elif choice == "3":
            target_name = input("Enter target name for impersonation attack: ")
            impersonation_attack(target_name)
        elif choice == "4":
            target_name = input("Enter target name for MFA bypass simulation: ")
            bypass_mfa(target_name)
        elif choice == "5":
            target_username = input("Enter social media username for reconnaissance: ")
            social_media_recon(target_username)
        elif choice == "6":
            target_url = input("Enter target URL for fake login page attack: ")
            fake_login_page(target_url)
        elif choice == "7":
            target_phone_number = input("Enter target phone number for smishing attack: ")
            smishing_attack(target_phone_number)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
