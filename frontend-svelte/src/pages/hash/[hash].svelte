<script>
  import { params, afterPageLoad } from "@roxi/routify"
  import Rules from "../rules.svelte"
  import Paging from "../../components/Paging.svelte"
  import api from "../../api"

  const BERLIN_LAT = 52.520815
  const BERLIN_LON = 13.4094191
  const MIN_PASSWORD_LENGTH = 6

  let hash
  let travels
  let handoverId
  let recipientPassword = ""
  let recipientEmail = ""
  let recipientName = ""
  let isConsented
  let step = 0
  let handoverText = ""
  let result
  let coin
  let manualMarker
  let handoverAnswer = ""
  let handoverQuestion = ""

  let defaultLat = BERLIN_LAT
  let defaultLon = BERLIN_LON
  let lat = 0
  let lon = 0
  let prevLat = 0
  let prevLon = 0

  let isErrorSubmitting = false
  let isErrorPosition = false
  let isErrorLocation = false

  let isCheckedLocation
  let willChooseLocation = false

  let formErrors = []

  const locationError = (error) => {
    if (error.code !== error.PERMISSION_DENIED) return
    isErrorPosition = true
  }

  const setLocation = () => {
    if (!isCheckedLocation) return

    navigator.geolocation.getCurrentPosition((position) => {
      lat = position.coords.latitude
      lon = position.coords.longitude
    }, locationError)
  }

  const nextStep = async () => {
    if (step === 1) {
      formErrors = []

      if (!checkIsNameFilled())
        formErrors = [...formErrors, "Please enter a valid name!"]

      if (!checkIsEmailFilled())
        formErrors = [...formErrors, "Please enter a valid email address!"]

      if (!checkIsPasswordValid())
        formErrors = [
          ...formErrors,
          `Please use a password of min ${MIN_PASSWORD_LENGTH} characters`,
        ]
      if (!checkIsConsented())
        formErrors = [
          ...formErrors,
          "You need to accept the data proection clause!",
        ]

      if (formErrors.length === 0) step += 1
    } else if (step === 2) {
      if (lat !== 0 && lon !== 0) {
        step += 1
      } else {
        isErrorLocation = true
      }
    } else if (step === 3) {
      const isHandoverSubmitted = await submitHandover()
      if (isHandoverSubmitted) {
        history.replaceState({}, null, `/handover/${handoverId}`)
      } else {
        isErrorSubmitting = true
      }
    } else {
      step += 1
    }
  }

  const prevStep = () => (step -= 1)

  const chooseLocation = () => {
    willChooseLocation = true
    manualMarker = myMap.on("click", addMarker)
  }

  const addMarker = (e) => {
    // Add marker to map at click location; add popup window
    if (manualMarker) myMap.removeLayer(manualMarker)

    manualMarker = L.marker(e.latlng, { icon: mapMarker }).addTo(myMap)
    lat = e.latlng.lat
    lon = e.latlng.lng
    return manualMarker
  }

  const checkIsConsented = () => isConsented
  const checkIsEmailFilled = () => !!recipientEmail
  const checkIsNameFilled = () => !!recipientName
  const checkIsPasswordValid = () =>
    recipientPassword.length >= MIN_PASSWORD_LENGTH

  const submitHandover = async () => {
    let handoverSubmission = {
      hash,
      recipientPassword,
      recipientName,
      text: handoverText,
      recipientEmail,
      lat,
      lon,
      question: handoverQuestion,
      answer: handoverAnswer,
    }
    console.log(handoverSubmission)

    result = await api.post("/submit_handover/", handoverSubmission)
    if (!result.is_saved) return false
    handoverId = result.handover_id
    return true
  }

  $afterPageLoad(() => {
    myMap.setView([defaultLat, defaultLon], 6)
    hash = $params.hash

    api.get(`/hash/${hash}`).then((res) => {
      //throw error if hash not found (res is empty Array)
      travels = res.data.coin.travels === null ? 0 : res.data.coin.travels
      coin = res.data.coin

      api.get(`/coins/${coin.id}/handovers/`).then((handovers) => {
        if (handovers.length > 0) {
          myMap.setView([handovers[0].lat, handovers[0].lon], 10)
        }
        let polyFill = handovers?.map((val) => [val.lat, val.lon])
        let iterator = 0
        myMap.eachLayer((layer) => {
          if (iterator > 1) {
            layer.remove()
          }
          iterator += 1
        })
        for (const line of handovers) {
          L.marker([line.lat, line.lon], { icon: mapMarker }).addTo(myMap)
          if (prevLat !== 0) {
            let polyLine = L.polyline(
              [
                [prevLat, prevLon],
                [line.lat, line.lon],
              ],
              { color: "red", weight: 5 }
            ).addTo(window.myMap)
          }
          prevLat = line.lat
          prevLon = line.lon
        }
      })
    })

    //if there is a handover, get handover and display form. if not, just display form and display instructions

    //travels = coin.travels

    //   recipientName = handover.recipient.name
    // giverName = handover.giver.name
    //lat = handover.lat
    //lon = handover.lon
    //console.log(coin)
    myMap.setView([defaultLat, defaultLon], 10)
  })
</script>

<form class="form">
  {#if step === 0}
    {#if travels === 0}
      <p>
        <strong>Congratulations!</strong>

        You have received this coin as part of Project linkage - an art project
        about trust!

        <strong>
          Please read the instructions <strong>carefully</strong> and then click
          on "continue"!
        </strong>
      </p>
      <p>
        <strong>IMPORTANT!</strong> this is an art project. We will collect data
        but we will never abuse it for commercial purposes. We will, however,
        kindly ask you for your email address and your geolocation as well as a
        name. This is important for the project to work! See more in the
        <a href="/privacy">privacy policy</a>
      </p>

      <Rules />
    {:else}
      <strong>Welcome!</strong>

      This coin has changed hands {travels} times so far

      <p>
        We assume you received this coin from your friend? If not, please
        contact us! Please make sure you read the instructions again before you
        continue!
      </p>
      <p>
        <strong>IMPORTANT!</strong> this is an art project. We will collect data
        but we will never abuse it for commercial purposes. We will, however,
        kindly ask you for your email address and your geolocation as well as a
        name. This is important for the project to work! See more in the
        <a href="/privacy">privacy policy</a>
      </p>

      <Rules />
    {/if}
    <button on:click={nextStep}>Continue</button>
  {:else if step === 1}
    <fieldset>
      {#if travels === 0}
        <legend>Enter your Data!</legend>

        <p>
          We would kindly ask you to enter your name, e-mail-address and a
          password. This way we can record you as the original holder of this
          coin. We promise you, that we will never ever publish your personal
          data _anywhere_! We might however use your e-mail-address to update
          you about what is going on with this coin. If you don't want this:
          we're working hard on a detailed concept. Let us know what you think!
        </p>
        {#if isErrorPosition}
          <span class="error"
            >Unfortunately you didn't allow us to set your location. We will
            automatically set it to Berlin</span>
        {/if}
        <label>
          <span>Original holder's name</span>
          <input
            bind:value={recipientName}
            type="text"
            placeholder="Your name" />
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

          <input bind:value={recipientPassword} type="password" />
        </label>

        <label>
          <input bind:checked={isConsented} type="checkbox" />
          <span>
            I consent that the entered data including my location and the story
            I enter within the next step will be used for this art project.
            Name, location and story will be published. Email address will be
            used to inform you about ... You can withdraw your consent any time
            for the future. For details please refer to the <a href="/privacy"
              >privacy policy</a>
          </span>
        </label>
      {:else}
        <legend>Handover Entry</legend>

        <p>
          Now it's time to enter the name of the person
          <strong>receiving the coin</strong>, as well as their password and
          other data
        </p>
        {#if isErrorPosition}
          <span class="error"
            >Unfortunately you didn't allow us to set your location. We will
            automatically set it to Berlin</span>
        {/if}
        <label>
          <span>Receiving person's name</span>
          <input
            bind:value={recipientName}
            type="text"
            placeholder="Your name" />
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
          <input bind:checked={isConsented} type="checkbox" />
          <span
            >I consent that the entered data including my location and the story
            I enter within the next step will be used for this art project.
            Name, location and story will be published. Email address will be
            used to inform you about ... You can withdraw your consent any time
            for the future. For details please refer to the <a href="/privacy"
              >privacy policy</a
            ></span>
        </label>
      {/if}

      {#each formErrors as error}
        <div><span class="error">{error}</span></div>
      {/each}
    </fieldset>
    <Paging {prevStep} {nextStep} />
  {:else if step === 2}
    <fieldset>
      <legend>Your Location</legend>

      <p>
        Now please give us your location. You can either choose whether you want
        to give us your location, or whether you want to choose one on the map
      </p>
      <label>
        <input
          bind:checked={isCheckedLocation}
          on:change={setLocation}
          type="checkbox" />
        <span>
          I want the browser to choose my location (When you mark this checkbox
          as checked, please click "Allow" when your browser asks you to share
          your location)
        </span>
      </label>
      <p>
        <span
          ><button on:click={chooseLocation} type="button" class="full"
            >I want to choose my own location by setting a marker on the map</button
          ></span>
        (Tap on this button, then tap on the map to set a marker)
      </p>
      {#if isErrorSubmitting}
        <span class="error"
          >Something went wrong - retry, reload or contact us if it persists</span>
      {/if}
    </fieldset>
    <Paging {prevStep} {nextStep} />
  {:else if step === 3}
    <fieldset>
      {#if travels === 0}
        <legend>Question and story</legend>
        <p>
          Thank you! Now almost set to hand over this coin to another person!
          Every coin comes with a question that every recipient is asked to
          answer. Please ask your question to the world!
        </p>
        <label>
          <span>Your Question</span>

          <input
            bind:value={handoverQuestion}
            type="text"
            placeholder="Your Question" />
        </label>

        <p>
          Now please tell the world something about your story. How did you
          receive the coin? What do you think about the project? How would you
          like to see the coin travel? Anything more about your question?
        </p>

        <label>
          <span>Your Story</span>
          <textarea bind:value={handoverText} />
        </label>
      {:else}
        <legend>Handover Story</legend>

        <p>
          Now please tell us the story about how you received your coin. About
          your conversation with your friend
        </p>

        <label>
          <span>Your Story</span>
          <textarea bind:value={handoverText} />
        </label>
        <p>And please answer the question your friend asked you:</p>
        <label>
          <span>The Question: {coin.question}</span>
          <textarea bind:value={handoverAnswer} />
        </label>

        {#if isErrorSubmitting}
          <span class="error"
            >Something went wrong - retry, reload or contact us if it persists</span>
        {/if}
      {/if}
    </fieldset>
    <Paging {prevStep} {nextStep} />
  {/if}
</form>
