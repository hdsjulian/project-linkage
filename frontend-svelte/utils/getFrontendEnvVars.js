// Picks all env vars starting with PREFIX
// and returns a corresponding object

const PREFIX = "FRONTEND_APP_"
const ENV = process.env

export const getFrontendEnvVars = () =>
  Object.keys(ENV).reduce((acc, val) => {
    if (val.startsWith(PREFIX)) acc[val] = ENV[val]
    return acc
  }, {})
