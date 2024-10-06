document.getElementById('shortenBtn').addEventListener('click', function() {
    const urlInput = document.getElementById('urlInput').value;
    
    if (urlInput) {
      // Bug: This random string will sometimes include special characters that break the URL
      const shortLink = 'https://short.ly/' + Math.random().toString(36).substr(2, 5);
      
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