function pin_direction_change() {
  console.log("hello");

  // TODO this should come from HTML tempaltes
  const data = { idx: 1 };

  fetch("/api/gpio", {
    method: "POST", // or 'PUT'
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function doSomething() {
  // TODO this should come from HTML tempaltes
  const data = { idx: 1 };

  fetch("/api/i2c", {
    method: "POST", // or 'PUT'
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  return false;
}
