// From an object following the format of `process.env`,
// produces an objects ready to use with rollup plugin-replace

export const getReplacements = (envVars) =>
  Object.entries(envVars).reduce((acc, [k, v]) => {
    return { ...acc, [`process.env.${k}`]: `"${v}"` }
  }, {})
