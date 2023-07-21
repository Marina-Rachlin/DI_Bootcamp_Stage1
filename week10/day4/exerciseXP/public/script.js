const handleRegister = async (e) => {
  e.preventDefault();

  const fname = e.target.fname.value;
  const lname = e.target.lname.value;
  const email = e.target.email.value;
  const username = e.target.username.value;
  const password = e.target.password.value;

//   console.log(first_name, last_name, email, username, password);

  try {
    const registerFormReturn = await fetch('/users/register',{
        method:'POST',
        headers: {
            "content-type":"application/json"
        },
        body:JSON.stringify({fname, lname, email, username, password})
    });
    const returndata = await registerFormReturn.json();
    console.log(returndata);
    const div = document.getElementById("root");
    div.textContent = returndata;
  } catch (err) {
    console.log(err);
  }
  
};


const handleLogin = async (e) => {
  e.preventDefault();

  const username = e.target.username.value;
  const password = e.target.password.value;

  try {
    const registerFormReturn = await fetch('/users/login',{
        method:'POST',
        headers: {
            "content-type":"application/json"
        },
        body:JSON.stringify({username, password})
    });
    const returndata = await registerFormReturn.json();
    console.log(returndata);
    const div = document.getElementById('loginResult');
    div.textContent = returndata;
    


  } catch (err) {
    console.log(err);


  }

  
};