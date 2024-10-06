document.getElementById('shortenBtn').addEventListener('click', function() {
  const urlInput = document.getElementById('urlInput').value;

  if (urlInput) {
    // Generate a short link with only alphanumeric characters
    const shortLink = 'https://short.ly/' + generateShortCode(5); // Bug fix here

    // Display the shortened link
    const shortLinkElem = document.getElementById('shortenedLink');
    shortLinkElem.href = shortLink;
    shortLinkElem.textContent = shortLink;

    // Show the shortened link section
    document.querySelector('.short-link').style.display = 'block';
  } else {
    alert('Please enter a valid URL!');
  }
});

// Bug fix: Function to generate a short code with alphanumeric characters only
function generateShortCode(length) {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; // Safe character set
  let result = '';
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    result += characters[randomIndex];
  }
  return result;
}
