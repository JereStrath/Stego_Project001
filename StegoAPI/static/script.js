// Submit the form using AJAX and display the prediction result
document.querySelector('form').addEventListener('submit', function (e) {
  e.preventDefault();

  const fileInput = document.querySelector('input[type="file"]');
  const formData = new FormData();
  formData.append('image', fileInput.files[0]);

  if (!fileInput.files[0]) {
      alert('Please select an image to upload.');
      return;
  }

  fetch('/detect', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      const resultDiv = document.getElementById('result');
      if (data.is_stegomalware === true) {
          resultDiv.innerHTML = `Warning!!! Stegomalware detected. This image poses a threat to your device. We recommend that you delete it.`;
      } else {
          resultDiv.innerHTML = `The image appears to have no malicious file and is safe.`;
      }
  })
  .catch(error => console.error(error));
});

// function previewImage(event) {
//     var reader = new FileReader();
//     reader.onload = function() {
//       var preview = document.getElementById('preview');
//       preview.src = reader.result;
//       document.getElementById('image-container').style.display = 'block';
//     };
//     reader.readAsDataURL(event.target.files[0]);
// //   }
  
//   function clearImage() {
//     document.getElementById('preview').src = '#';
//     document.getElementById('image-container').style.display = 'none';
//     document.getElementById('file-input').value = '';
//   }
const selectImage = document.querySelector(`.select-image`);
const inputFile = document.querySelector(`#file`);
const imgArea = document.querySelector(`.img-area`);

selectImage.addEventListener('click', function () {
    inputFile.click();
})

inputFile.addEventListener('change', function(){
    const image = this.files[0]
    const reader = new FileReader();
    reader.onload = ()=> {
        const allImg = imgArea.querySelectorAll('img');
        allImg.forEach(item=> item.remove());
        const imgUrl = reader.result;
        const img = document.createElement('img');
        img.src=imgUrl;
        imgArea.appendChild(img);
        imgArea.classList.add('active');
        imgArea.dataset.img = image.name;
    }
    reader.readAsDataURL(image);
})