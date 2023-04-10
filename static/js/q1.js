// const form = document.querySelector('.fom')
// form.addEventListener('submit', function (event) {
//   event.preventDefault()

//   let q1 = document.querySelector('input[name="q1"]:checked').value
//   let q2 = document.querySelector('input[name="q2"]:checked').value
//   let q3 = document.querySelector('input[name="q3"]:checked').value
//   ans = Number(q1) + Number(q2) + Number(q3)

//   if (ans < -1) {
//     result = { value: "low" }
//   } else if (ans < 2) {
//     result = { value: "mid" }
//   } else {
//     result = { value: "high" }
//   }

//   fetch('http://127.0.0.1:8000/ifdog/test/', {
//     method: 'POST',
//     headers: {
//       'X-Requested-with': 'XMLHttpRequest',
//       'Content-Type': 'application/json',
//       'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken').value
//     },
//     body: JSON.stringify(result),
//   })
//     .then(() => console.log(result.value))
// })