<?php
$Name  = $_POST[' Name '];
$EmailAddress = $_POST['EmailAddress'];
$Subject = $_POST['Subject'];
$message = $_POST['message'];
//$phoneCode = $_POST['phoneCode'];
//$phone = $_POST['phone'];
if (!empty($Name) || !empty($EmailAddress) || !empty($Subject) || !empty($message)) {
    $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "forestfire";
    //create connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
    if (mysqli_connect_error()) {
     die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    } else {
     $SELECT = "SELECT  EmailAddress  From report Where EmailAddress = ? Limit 1";
     $INSERT = "INSERT Into report (Name , EmailAddress , Subject , message) values(?, ?, ?, ?)";
     //Prepare statement
     $stmt = $conn->prepare($SELECT);
     $stmt->bind_param("s", $EmailAddress);
     $stmt->execute();
     $stmt->bind_result($EmailAddress);
     $stmt->store_result();
     $rnum = $stmt->num_rows;
     if ($rnum==0) {
      $stmt->close();
      $stmt = $conn->prepare($INSERT);
      $stmt->bind_param("ssss", $Name, $EmailAddress, $Subject, $message);
      $stmt->execute();
      echo "New record inserted sucessfully";
     } else {
      echo "Someone already register using this email";
     }
     $stmt->close();
     $conn->close();
    }
} else {
 echo "All field are required";
 die();
}
?>