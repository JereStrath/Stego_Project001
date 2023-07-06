// Submit the form using AJAX and display the prediction result
document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('image', document.querySelector('input[type="file"]').files[0]);

    fetch('/detect', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        // resultDiv.innerHTML = `Prediction: ${data.prediction}<br>Is Stegomalware: ${data.is_stegomalware}`;
        // resultDiv = document.getElementById("resultDiv"); // Assuming there is an HTML element with id "resultDiv"

        if (data.is_stegomalware === true) {
          resultDiv.innerHTML = `Warning!!! Stegomalware detected  this image posses a threat to your device. We recommend that you delete it`;
        } else {
          resultDiv.innerHTML = `The image is safe`;
        }

            })
            .catch(error => console.error(error));
        });

function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
      var preview = document.getElementById('preview');
      preview.src = reader.result;
      document.getElementById('image-container').style.display = 'block';
    };
    reader.readAsDataURL(event.target.files[0]);
  }
  
  function clearImage() {
    document.getElementById('preview').src = '#';
    document.getElementById('image-container').style.display = 'none';
    document.getElementById('file-input').value = '';
  }
