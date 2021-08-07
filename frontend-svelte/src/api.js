import axios from "axios"
import { API_URL } from "./constants"

export default {
  get: (resource) => axios.get(`${API_URL}${resource}`).then((res) => res.data),

  post: (resource, body) =>
    axios.post(`${API_URL}${resource}`, body).then((res) => res.data),

  update: (resource, body) =>
    axios.patch(`${API_URL}${resource}`, body).then((res) => res.data),

  delete: (resource) => axios.delete(`${API_URL}${resource}`),
}
