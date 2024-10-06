# Send Emails in Python with Gmail SMTP

This repository demonstrates how to use different modules in Python to construct and send various types of email messages, review existing authentication methods, and more. This section guides you through importing the `smtplib` module, creating an SMTP object for your server, and leveraging its core functions to send emails.


# Requirements
    - `smtplib`
    - `email` module.
    - `Jinja2`
<br>

# Usage

1. **App Passwords**: For accounts with two-factor authentication (2FA), you'll need to generate an app-specific password.

	1.1. Go to [App Passwords](https://myaccount.google.com/apppasswords).

	1.2. Signing in to Google.

	1.3. Type your application name (E.g.: send-emails-app).	

	1.4. Click on **Create**.

	1.5. **Copy the generated password**.
<br>

2.  Create `conf.json` file in `./conf` directory. Template:
	 
    ```
    {
	    "account": {
	        "email": "example.user@example.com",          	// Your email address
	        "key": "abcd efgh xxxx xxxx"                 	// App Password (You copied it in step 1)
	    },
	    "receiver": [
	        "example.user1@example.com",                 	// First recipient's email address
	        "example.user2@example.com",                 	// Second recipient's email address
	        "example.user3@example.com"                  	// Third recipient's email address
	    ],
	    "sender_alias": "No Reply",                      	// Alias for the sender (displayed in the recipient's inbox)
	    "email_alias": "noreply@example.com",            	// Alias email for the sender (displayed in the recipient's inbox)
	    "subject": "Automated Email Notification",       	// Email subject line
	    "template": "template.html",                     	// HTML file email template (see ./templates/)
	    "user_name": "Nguyen Van A",                	// Display name of the sender
	    "attachment": "file_1.txt",                    	// The file to be attached (see ./attachment/)
	    "attachment_alias": "attachment.txt"             	// Display name of the attachment
	}
    ```
<br>

3. Launch `./src./main`