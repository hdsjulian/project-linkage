import axios from "axios"

const API_URL = "http://localhost:3000"

export default {
  get: (resource) => axios.get(`${API_URL}${resource}`).then((res) => res.data),

  post: (resource, body) =>
    axios.post(`${API_URL}${resource}`, { body }).then((res) => res.data),
}
