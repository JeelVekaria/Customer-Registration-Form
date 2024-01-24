#!/usr/bin/perl -wT 
use strict; 
use CGI; 
use CGI::Carp qw ( fatalsToBrowser ); 
use File::Basename;

$CGI::POST_MAX = 1024 * 5000;
my $safe_filename_characters = "a-zA-Z0-9_.-";

my $query = new CGI;
my $filename = $query->param('photo');
if ( !$filename ) { print $query->header ( ); print "There was a problem uploading your photo (try a smaller file)."; exit; }
my $upload_dir = "/home/j2vekari/public_html/upload";
my $upload_filehandle = $query->upload("photo");
open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!"; 
binmode UPLOADFILE; while ( <$upload_filehandle> ) { print UPLOADFILE; } close UPLOADFILE;

print "Content-type: text/html\n\n";


# Retrieve form inputs
 my $firstName = $query->param("firstName");
 my $lastName = $query->param('lastName');
 my $street = $query->param('street');
 my $city = $query->param('city');
 my $postalCode = $query->param('postalCode');
 my $province = $query->param('province');
 my $phoneNumber = $query->param('phoneNumber');
 my $email = $query->param('email');
 my $linkRef = "https://www2.cs.ryerson.ca/~j2vekari/upload";

print qq(<body style="background-color:rgba(206,236,241,255); text-align: center;font-family: 'IBM Plex Mono', monospace; font-size: 30px;">);

if ($phoneNumber =~ /^\d{10}$/ && 
$postalCode =~ /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/ && 
$email =~ /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]+$/) {
    print "<h1><u>Form submitted successfully!</u></h1>";
    print "<p><b>Name</b>: $firstName $lastName</p>";
    print "<p><b>Address</b>: $street, $city, $province, $postalCode</p>";
    print "<p><b>Phone Number</b>: $phoneNumber</p>";
    print "<p><b>Email</b>: $email</p>";
    print qq(<p><img src="$linkRef/$filename" alt="Photo"/></p>);
} 
else {
    print "<h1>Format not accepted. Please try again.</h1>";
}
if (!($phoneNumber =~ /^\d{10}$/)){
    print "<p>Your Input: <mark>Phone Number (format 10 digits):  $phoneNumber</mark></p>";
    print "<p>Desired Input is in the format of XXXXXXXXXX (10 X's replaced with numbers)</p>";
}
if (!($postalCode =~ /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/)){
    print "<p>Your Input: <mark>Postal Code (format L0L 0L0): $postalCode</mark></p>";
    print "<p>Desired Input is in the format of 'L0L 0L0' where the 'L' and '0' are replaced with the real postal code characters</p>";
}
if (!($email =~ /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]+$/)){
    print "<p>Your Input: <mark>Email Addresss: $email</mark></p>";
    print "<p>Desired Input is in the format of A\@B.C (A - email id before the \@, B - email id after the \@, C - the domain after the dot</p>";
}
print "</body>";