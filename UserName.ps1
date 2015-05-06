$lName = Read-Host "User's last name"
$fName = Read-Host "User's first name"

$lArray = $lName.ToCharArray()
$fArray = $fName.ToCharArray()

$firstHalf = @()
$secondHalf = @()

for ($i = 0; $i -lt 5; $i++) {
    $firstHalf += $lArray[$i]
}

for ($i = 0; $i -lt 3; $i++) {
    $secondHalf += $fArray[$i]
}

$uname = $firstHalf + $secondHalf

$uname -join ""
