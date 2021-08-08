<script>
  import { url, params, afterPageLoad } from "@roxi/routify"
  import Rules from "../rules.svelte"
  import Paging from "../../components/Paging.svelte"
  import api from "../../api"

  let hash
  let travels
  let handover_id = 1
  let giverPassword = ""
  let recipientPassword = ""
  let recipientEmail = ""
  let recipientName = ""
  let recipientPasswordAgain = ""
  let step = 0
  let handoverText = "Your Story"
  let result 
  let lat = 52.520815
  let lon = 13.4094191
  let wrong_pass = false
  let password_match = true
  let coin
  let error_submitting = false
  let error_position = false
  function setLocation(position) {
    lat = position.coords.latitude
    lon = position.coords.longitude
    console.log(lat)
  }
  function locationError(error) {
    if (error.code == error.PERMISSION_DENIED) {
      error_position = true
    }
  }

  const nextStep = () => {
    if (travels > 0) { 
      if (step == 1) { 
        checkPass()
      }
      else if (step == 2) {
        password_match = checkPasswordMatch()
        step +=1;
        navigator.geolocation.getCurrentPosition(setLocation, locationError)
      }
      else if (step == 3) {
        if (submitHandover() != false) {
          step +=1
        }
        else {
          error_submitting = true
        }
      }
      else {
        step += 1
      }
      console.log(step)
    }
    else { 
      if (step == 0) {
        navigator.geolocation.getCurrentPosition(setLocation, locationError)
        console.log(lat)

      }
      if (step == 1) {
        password_match = checkPasswordMatch()
        if (password_match == true) {
          handoverText = ""
          if (submitHandover() != false) {
            step += 1
          }
          else {
            error_submitting = true
          }
        }
      }
      else { 
        step +=1
      }
    }
  }

  const prevStep = () => {
    step -= 1
  }

  const checkPass = async () => {
    console.log("Checking Pass")
    result = await (api.post("/verify_user/", { "hash": hash, "password": giverPassword }))
    console.log(result.is_verified)
    if (result.is_verified == false) {
      console.log("blub:")
      wrong_pass = true
    }
    else {
      wrong_pass = false
      step += 1
    }
  }

  const submitHandover = async() => {
    result = await(api.post("/submit_handover/", {
      "hash": hash, 
      "giver_password": giverPassword, 
      "recipient_password": recipientPassword,
      "recipient_password_again": recipientPasswordAgain,
      "recipient_name": recipientName, 
      "text": handoverText, 
      "recipient_email": recipientEmail, 
      "lat": lat, 
      "lon": lon
    }))
      if (result.is_saved == true) {
        handover_id = result.handover_id
        console.log(handover_id)
        return handover_id
      }
      else {
        return false
      }
    }
  const checkPasswordMatch = () => {
    if (recipientPassword == recipientPasswordAgain){
      return true
    }
    else {
        return false
    }

  }

  $afterPageLoad(() => {
    console.log($params.hash)
    hash = $params.hash
    api.get(`/hash/${hash}`).then((res) => {
      travels = res.data.coin.travels == null? 0: res.data.coin.travels
      console.log(travels)
      coin = res.data.coin
    })
      //if there is a handover, get handover and display form. if not, just display form and display instructions
      
      //travels = coin.travels

      //   recipientName = handover.recipient.name
      // giverName = handover.giver.name
      //lat = handover.lat
      //lon = handover.lon
      //console.log(coin)
  })
</script>

<form class="form">
  {#if step === 0}
    {#if travels == 0}
      <p>
        <strong>Welcome!</strong>

        You are the first person to use this coin!

        <strong>
          Please read the instructions <strong>carefully</strong> and then click
          on "continue"!
        </strong>
      </p>
      <p>
        <strong>IMPORTANT!</strong> - in the next step we will ask you to allow the browser to give us your location. <strong>Please say yes!</strong>
      </p>

      <Rules />
    {:else}
      <strong>Welcome!</strong>

      This coin has changed hands {travels} times so far!

      <p>
        We assume you want to hand it over to a friend? Please make sure you
        read the instructions again before you continue!
      </p>

      <Rules /> 
    {/if}
    <button on:click={nextStep}>Continue</button>
  {:else if step === 1}
    {#if travels > 0}
      <fieldset>
        <legend>Giving Person's Password</legend>

        <p>
          Now please enter the <strong>giving person's</strong> secret - We need
          to make sure that you didn't just find this coin somewhere. If you did,
          or if you forgot your password, please
          <a use:$url href="/contact">contact</a>
          us (we're working on a reset password function)!
        </p>
        <p>
          <strong>IMPORTANT!</strong> - in the next step we will ask you to allow the browser to give us your location. <strong>Please say yes!</strong>>
        </p>

        <label>
          <span>Giving person's password</span>

          <input
            bind:value={giverPassword}
            type="password"
            placeholder="Your name" />
        </label>
        {#if wrong_pass === true}
          <span class="error">Password is wrong! If you can't remember your password, please contact us!</span>
        {/if}

      </fieldset>
    {:else}
      <fieldset>
        <legend>Enter your Data!</legend>

        <p>
          We would kindly ask you to enter your name, e-mail-address and a password. This way we can record you as the original holder of this coin.
          We promise you, that we will never ever publish your personal data _anywhere_! We might however use your e-mail-address to update you about what is going on with this coin. 
          If you don't want this: we're working hard on a detailed concept. Let us know what you think!
        </p>
        {#if error_position == true}
        <span class="error">Unfortunately you didn't allow us to set your location. We will automatically set it to Berlin</span>
        {/if}
         <label>

          <span>Original holder's name</span>
          <input bind:value={recipientName} type="text" placeholder="Your name" />
        </label>

        <label>
          <span>Original holder's e-mail address</span>

          <input
            bind:value={recipientEmail}
            type="text"
            placeholder="Your email" />
        </label>

        <label>
          <span>Original holder's password</span>

          <input
            bind:value={recipientPassword}
            type="password"/>
        </label>

        <label>
          <span>Original holder's password (again!)</span>
          <input
            bind:value={recipientPasswordAgain}
            type="password"/>
        </label>
      </fieldset>
      {#if password_match == false}
        <span class="error">Password mismatch!</span>
      {/if}
      {#if error_submitting == true}
      <span class="error">Something went wrong - retry, reload or contact us if it persists</span>
      {/if}
    {/if}

    <Paging {prevStep} {nextStep} />
  {:else if step === 2}
    {#if travels > 0}
      <fieldset>
        <legend>Handover Entry</legend>

        <p>
          Now it's time to enter the name of the person
          <strong>receiving the coin</strong>, as well as their password and other
          data
        </p>
        {#if error_position == true}
        <span class="error">Unfortunately you didn't allow us to set your location. We will automatically set it to Berlin</span>
        {/if}
        <label>
          <span>Receiving person's name</span>
          <input bind:value={recipientName} type="text" placeholder="Your name" />
        </label>

        <label>
          <span>Receiving person's e-mail address</span>

          <input
            bind:value={recipientEmail}
            type="text"
            placeholder="Your name" />
        </label>

        <label>
          <span>Receiving person's password</span>

          <input
            bind:value={recipientPassword}
            type="password"
            placeholder="Your name" />
        </label>

        <label>
          <span>Receiving person's password (again!)</span>
          <input
            bind:value={recipientPasswordAgain}
            type="password"
            placeholder="Your name" />
        </label>
      </fieldset>
      {#if password_match == false}
        <span class="error">Password mismatch!</span>
      {/if}
      {#if error_submitting == true}
        <span class="error">Something went wrong - retry, reload or contact us if it persists</span>
      {/if}

      <Paging {prevStep} {nextStep} />
    {:else} 
    <fieldset>
      <p>
        Thank you! You are now all set to hand over this coin to another person! 
        This coin, by the way, carries the id {coin.id} and you can see its path <a href="/coin/{coin.id}">here</a>. 
      </p>

    </fieldset>
    {/if}
    
  {:else if step === 3}
    <fieldset>
      <legend>Handover Story</legend>

      <p>
        Now please tell us your story. It would be very nice of you if you could
        allow the phone to retrieve your location data!
      </p>

      <label>
        <span>Your Story</span>

        <textarea bind:value={handoverText} />
      </label>
    </fieldset>

    <Paging {prevStep} {nextStep} />
    {:else if step === 4}
    <fieldset>
      <p>
        Thank you! {recipientName} is now all set to hand over this coin to another person! 
        This coin, by the way, carries the id {coin.id} and you can see its path <a href="/coin/{coin.id}">here</a>. 
      </p>

    </fieldset>
    {/if}
</form>
