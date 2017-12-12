function verifyAndLogin() {
  let loginForm = document.querySelector('#loginForm');

  if(!loginForm.checkValidity()) {
    loginForm.reportValidity();
    return;
  }

  loginForm.submit();
}
