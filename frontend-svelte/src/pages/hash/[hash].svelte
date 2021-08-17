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
  let handoverText = ""
  let result 
  let lat = 52.520815
  let lon = 13.4094191
  let wrong_pass = false
  let password_match = true
  let coin
  let error_submitting = false
  let error_position = false
  let email_correct = true
  let name_correct = true
  let prevLat = 0
  let prevLon = 0
  function setLocation(position) {
    lat = position.coords.latitude
    lon = position.coords.longitude
  }
  function locationError(error) {
    if (error.code == error.PERMISSION_DENIED) {
      error_position = true
    }
  }

  const nextStep = async() => {
    if (step == 1) {
      password_match = checkPasswordMatch()
      email_correct = checkEmail()
      name_correct = checkName() 
      if (password_match == true && email_correct == true && name_correct == true) {
        navigator.geolocation.getCurrentPosition(setLocation, locationError)
        step +=1
      }
    }
    else if (step == 2) {
      const isHandoverSubmitted = await submitHandover()
      if (isHandoverSubmitted) {
        history.replaceState({}, null, `/handover/${handover_id}`)
      }
      else {
        error_submitting = true
      }
    }
    else {
      step += 1
    }
  }

  const prevStep = () => {
    step -= 1
  }

 /* const checkPass = async () => {
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
  }*/

const checkPasswordMatch = () => {
  if (recipientPassword == recipientPasswordAgain){
    return true
  }
  else {
      return false
  }
}

const checkEmail = () => {
  if (recipientEmail == "") {
    return false
  }
  else {
    return true
  }
}

const checkName = () => {
  if (recipientName == "") {
    return false
  }
  else {
    return true
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
        return true
      }
      else {
        return false
      }
    }


  $afterPageLoad(() => {
    myMap.setView([lat,lon], 6)
    hash = $params.hash
    api.get(`/hash/${hash}`).then((res) => {
      travels = res.data.coin.travels == null? 0: res.data.coin.travels
      coin = res.data.coin
      console.log(coin)
      api.get(`/coins/${coin.id}/handovers/`).then((hl_res) => {
        if (hl_res.length > 0) {
          myMap.setView([hl_res[0].lat, hl_res[0].lon], 10)
        }
        let polyFill = hl_res?.map((val) => [val.lat, val.lon])
        let iterator = 0
        myMap.eachLayer((layer) => {
            if (iterator > 1) { 
                layer.remove();
            }
            iterator +=1
        });
        for (const line of hl_res) { 
          L.marker([line.lat, line.lon], {icon: mapMarker}).addTo(myMap)
          if (prevLat != 0) {
              var polyLine = L.polyline([[prevLat, prevLon], [line.lat, line.lon]], {color:'red', weight: 5}).addTo(window.myMap)
          }
          prevLat = line.lat
          prevLon = line.lon
        }

      })      
    })
    console.log(coin)

      //if there is a handover, get handover and display form. if not, just display form and display instructions
      
      //travels = coin.travels

      //   recipientName = handover.recipient.name
      // giverName = handover.giver.name
      //lat = handover.lat
      //lon = handover.lon
      //console.log(coin)
    myMap.setView([lat, lon], 10)
  })
</script>

<form class="form">
  {#if step === 0}
    {#if travels == 0}
      <p>
        <strong>Congratulations!</strong>

        You have received this coin as part of Project linkage - an art project about trust! 

        <strong>
          Please read the instructions <strong>carefully</strong> and then click
          on "continue"!
        </strong>
      </p>
      <p>
       <strong>IMPORTANT!</strong> this is an art project. We will collect data but we will never abuse it for commercial purposes. 
        We will, however, kindly ask you for your email address and your geolocation as well as a name. This is important for the project to work!
      </p>

      <Rules />
    {:else}
      <strong>Welcome!</strong>

      This coin has changed hands {travels} times so far 

      <p>
        We assume you received this coin from your friend? If not, please contact us! Please make sure you
        read the instructions again before you continue! 
      </p>
      <p>
        <strong>IMPORTANT!</strong> this is an art project. We will collect data but we will never abuse it for commercial purposes. 
        We will, however, kindly ask you for your email address and your geolocation as well as a name. This is important for the project to work!
      </p>

      <Rules /> 
    {/if}
    <button on:click={nextStep}>Continue</button>
  {:else if step === 1}
  <fieldset>
    {#if travels  == 0}

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
            type="email"
            placeholder="Your email" />
        </label>

        <label>
          <span>Original holder's password</span>

          <input
            bind:value={recipientPassword}
            type="password"/>
        </label>

        <label>
          <span>I accept that the entered data including location data is recorded for the purpose of this website and my name and location data is published for the purpose of this website and are published.</span>
          <input
            bind:value={recipientPasswordAgain}
            type="checkbox"/>
        </label>
    {:else}
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
            type="email"
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
          <span>I accept that the entered data including location data is recorded for the purpose of this website and my name and location data is published for the purpose of this website and are published.</span>
          <input
            bind:value={recipientPasswordAgain}
            type="checkbox"/>
        </label>
      
    {/if}
  {#if password_match == false}
    <span class="error">Password mismatch!</span>
  {/if}
  {#if email_correct == false}
    <span class="error">Please enter a valid email address!</span>
  {/if}
  {#if name_correct == false}
    <span class="error">Please enter a valid name!</span>
  {/if}
  </fieldset>
  <Paging {prevStep} {nextStep} />


  {:else if step == 2} 
    <fieldset>
    {#if travels == 0}
      <p>
        Thank you! Now almost set to hand over this coin to another person! 
        Please let the world know how you received this coin!
      </p>
      <label>
        <span>Your Story</span>

        <textarea bind:value={handoverText} />
      </label>
    {:else} 
        <legend>Handover Story</legend>

        <p>
          Now please tell us your story. It would be very nice of you if you could
          allow the phone to retrieve your location data!
        </p>

        <label>
          <span>Your Story</span>
         <textarea bind:value={handoverText} />
        </label>
        {#if error_submitting == true}
        <span class="error">Something went wrong - retry, reload or contact us if it persists</span>
        {/if}    
      {/if}
      </fieldset>
      <Paging {prevStep} {nextStep} />
  {/if}
</form>

