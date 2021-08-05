const API_URL = "http://localhost:3000"

export default {
  get: (resource) => fetch(`${API_URL}${resource}`).then((res) => res.json()),

  post: (resource, body) =>
    fetch(`${API_URL}${resource}`, {
      method: "post",
      body: JSON.stringify(body),
      headers: { "Content-Type": "application/json" },
    }).then((res) => res.json()),
}
