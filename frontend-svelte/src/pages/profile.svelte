<script>
    let email
    let password
    let step = 0
    let name
    let repeat_password
    const next_step = () => {
    step +=1
  }    
</script><h1>Profile</h1>
<form class="form">
{#if step === 0}
    <fieldset>
        <h2 class="error">THIS DOES NOT WORK YET</h2>
        <legend>Enter your email and password</legend>
        <p>In order to access and edit your profile or to edit handovers, please enter your email and password
        </p>
        <label><span>Email address</span>
          <input type="text" placeholder="Your Email" bind:value={email}>
        </label>
        <label><span>Password</span>
          <input type="password" bind:value={password}>
        </label>
    </fieldset>
{:else if step === 1}

    <fieldset>
        <legend>Edit your user details</legend>
        <p>Here you can edit your user details. Go ahead, change your name or email address, and even password!
        </p>
        <label><span>name</span>
            <input type="text" placeholder="Martin" bind:value={name}>
          </label>
        <label><span>Email address</span>
          <input type="text" placeholder="coderman@protonmail.com" bind:value={email}>
        </label>
        <label><span>Password</span>
          <input type="password" bind:value={password}>
        </label>
        <label><span>Repeat Password</span>
            <input type="password" bind:value={repeat_password}>
          </label>
 
    </fieldset>
{/if}
</form>
<button on:click={next_step}>Continue</button>