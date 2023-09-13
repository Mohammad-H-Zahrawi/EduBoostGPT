const signInLink = document.querySelector('.sign-in');
const signInModal = document.querySelector('.sign-in-modal');
const closeModalButton = document.querySelector('.close-modal');

signInLink.addEventListener('click', () => {
  signInModal.classList.add('open');
});

closeModalButton.addEventListener('click', () => {
  signInModal.classList.remove('open');
});
