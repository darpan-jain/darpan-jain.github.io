<?php

if(isset($_POST['submit'])) {
    $name = $_POST['name'];
    $subject = $_POST['subject'];
    $visitor_email = $_POST['email'];
    $message = $_POST['message'];

    $email_from = "darpan-jain.github.io";
    $emailTo = "darpan.pmun@gmail.com";

    $headers = "From: ".$email_from;
    $txt = "You have a new inquiry from ".$name.".\n\n".$message;

    mail($emailTo, $subject, $txt, $headers);
    header("Location: index.php?mailsent");
}