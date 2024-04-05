function redirectToGitHub(repoURL) {
  window.location.href = repoURL;
}
function redirectToTableau(repoURL) {
  window.location.href = repoURL;
}


document.addEventListener('DOMContentLoaded', function () {
  const inputs = document.querySelectorAll('.form-group input, .form-group textarea');
  
  inputs.forEach(input => {
    input.addEventListener('focus', function () {
      const label = this.parentElement.querySelector('label');
      label.style.transform = 'translateY(-20px)';
      label.style.fontSize = '12px';
      label.style.color = '#2C2913';
    });
    
    input.addEventListener('blur', function () {
      const label = this.parentElement.querySelector('label');
      if (this.value === '') {
        label.style.transform = '';
        label.style.fontSize = '';
        label.style.color = '#C8B393';
      }
    });
  });
});

