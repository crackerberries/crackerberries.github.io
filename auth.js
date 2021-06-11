function verifyPassword() {

    password = document.getElementById("password").value;

    if (password == "abhs32") {

        location.href = "downloads.html"

    } else {

        document.getElementById("br").innerText = "invalid password"

    }

}