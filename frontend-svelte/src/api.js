import axios from "axios"
import { API_URL } from "./constants"

export default {
  get: (resource) => axios.get(`${API_URL}${resource}`).then((res) => res.data),

  post: (resource, body) =>
    axios.post(`${API_URL}${resource}`, { body }).then((res) => res.data),
}
