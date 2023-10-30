function dream() {
  // Get the button element
  var generateButton = document.querySelector("button");

  // Disable the button and change its text
  generateButton.disabled = true;
  generateButton.textContent = "Generating...";

  // Get the values of the input fields
  var promptValue = document.getElementById("prompt").value;
  var pwdValue = document.getElementById("pwd").value;
  var imgWidthValue = document.getElementById("imgWidth").value;
  var imgHeightValue = document.getElementById("imgHeight").value;

  // Construct the URL to the backend app with query parameters
  var url = "https://sliq-appx.frankcheng7.repl.co/dream?";
  url += new URLSearchParams({
    prompt: promptValue,
    pwd: pwdValue,
    imgWidth: imgWidthValue,
    imgHeight: imgHeightValue
  }).toString();

  // Make a GET request to the URL
  fetch(url)
    .then(response => {
      if (response.ok) {
        return response.blob();
      } else {
        alert('Fail to generate the image.');
        throw new Error('Fail to generate the image.');
      }
    })
    .then(blob => {
      // Check if the response is a PNG image
      if (blob.type.includes('image/png')) {
        // Find the image container within the main section
        var imageContainer = document.getElementById("imageContainer");

        // Remove any existing images
        while (imageContainer.firstChild) {
          imageContainer.removeChild(imageContainer.firstChild);
        }

        // Create a new image element and set its source to the response data
        var image = document.createElement('img');
        image.src = URL.createObjectURL(blob);

        // Append the new image to the image container
        imageContainer.appendChild(image);
      } else {
        // Display an error message if the response is not a PNG
        alert('Error: The response is not a PNG image.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    })
    .finally(() => {
      // Re-enable the button and reset its text
      generateButton.disabled = false;
      generateButton.textContent = "Generate";
    });
}
