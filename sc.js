function login()
{
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if(username === "jasmine" && password==="1234"){
        window.location.href = "dashboard.html";
    }

    else{
        alert("wrong username or password");
    }
}

function logout()
{
    window.location.href= "pine.html";
}