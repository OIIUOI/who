function get() {
  let q1 = document.querySelector('input[name="q1"]:checked').value
  let q2 = document.querySelector('input[name="q2"]:checked').value
  let q3 = document.querySelector('input[name="q3"]:checked').value
  ans = Number(q1) + Number(q2) + Number(q3)

  if (ans < -1) {
    result = low
  } else if (ans < 2) {
    result = mid
  } else {
    result = up
  }
  return result
}



// fetch('/your-api-url/', {
//   method: 'POST',
//   headers: {
//     'Content-Type': 'application/json'
//   },
//   body: JSON.stringify({
//     data: 'your data here'
//   })
// })
// .then(response => response.json())
// .then(data => console.log(data))
// .catch(error => console.error(error))