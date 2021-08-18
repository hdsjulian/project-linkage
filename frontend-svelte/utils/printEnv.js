export const printEnv = (envVars) => {
  const entries = Object.entries(envVars)

  console.log("\n= FRONTEND ENV VARS ".padEnd(70, "="))
  for (const [k, v] of entries) {
    console.log(` ${k}=${v}`.substring(0, 68))
  }
  console.log("\n".padStart(70, "="))
}
