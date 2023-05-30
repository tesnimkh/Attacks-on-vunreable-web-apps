# WebFireWall-Application
👋 Welcome to my Web Application Firewall!

This beginner-friendly tool is designed to help you learn about firewall rules and how to apply them to protect your web applications from malicious requests. 🔥🚫🐞

My programm is open-source and free to use, so feel free to clone the repository and experiment with the firewall rules. 😃🎉

You can use this demo to gain hands-on experience with configuring firewall rules to block SQL injection, cross-site scripting (XSS), command injection, and other types of malicious requests. 🛡️👨‍💻

Simply clone this repository and run the Python script. Then visit the demo website and test different types of requests to see how the firewall rules work. 🕵️‍♀️🔍

I hope you find this tool useful in your journey to learn about web application security and firewall rules. Let's get started! 🚀

**Getting Started**

Clone the Repository: Start by cloning this repository to your local machine. You can do this by running the following command in your terminal:
**```git clone <repository_url>```**

**Install Dependencies**
Navigate to the project directory and install the required dependencies by running the following command:

**````pip install -r requirements.txt````**


**Configuration**

Firewall Rules: Open the firewall.json file. This file contains a set of firewall rules that define various types of malicious requests to be blocked. You can customize these rules as per your requirements.

IP Blacklist: If you want to block specific IP addresses, add them to the ip_blacklist array in the firewall rules. For example, to block the IP address 127.0.0.2, add it to the ip_blacklist array.

Rate Limiting: If you want to set a rate limit for requests, configure the requests_per_minute value in the corresponding rule. Requests exceeding this limit will be blocked. You can also add IP addresses to the ip_whitelist array to exempt them from rate limiting.

**Running the App**

Start the App Run the following command in the terminal to start the Flask app:

**````python <filename>.py````**

It will open a local server.

**Testing the Firewall**

SQL Injection: To test the SQL injection protection, try accessing a URL that includes special characters like ', ", (), #, ;, :, <, >, {}, %, [], --, or /*. You should see a blocked request message.

XSS (Cross-Site Scripting): Test the XSS protection by accessing a URL that includes HTML tags like <script> or <img>. You should see a blocked request message.

Command Injection: To test the command injection protection, access a URL that includes the $, (, {, or [ characters. You should see a blocked request message.

Blacklisted IP: If you added an IP address to the blacklist, try accessing the website from that IP. You should see a blocked request message.

Rate Limiting: If you set a rate limit for requests, try exceeding the specified limit. You will receive a blocked request message.

That's it! You now have a basic understanding of how to use my Web Application Firewall!
