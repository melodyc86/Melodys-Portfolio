<?php
// Get form data
$full_name = $_POST['full-name']; // Combine first name and last name
$email = $_POST['email'];
$subject = $_POST['Subject']; // Update to match the name attribute in your HTML form
$message = $_POST['message'];

// Split full name into first name and last name
list($first_name, $last_name) = explode(' ', $full_name, 2);

// Construct email message
$to = "melcheerios@gmail.com";
$email_subject = "Message from $full_name: $subject"; // Include subject in the email subject line
$body = "Name: $full_name\n"; // Use full name
$body .= "Email: $email\n\n";
$body .= "Message:\n$message";

// Send email
if (mail($to, $email_subject, $body)) {
    echo "Email sent successfully!";
} else {
    echo "Failed to send email. Please try again later.";
}
?>
