<script>
  import { url, params, afterPageLoad } from "@roxi/routify"
  import Rules from "../rules.svelte"
  import api from "../../api";

  let hash
  let coin_id
  let travels
  let handover_id = 0
  let giver_password = ""
  let recipient_password=""
  let recipient_email = ""
  let recipient_name = ""
  let recipient_password_again = ""
  let step = 0
  let handover_text ="Your Story"
  const next_step = () => {
    step +=1
  }
  const prev_step = () => {
    step -=1
  }
  const check_pass = () => {
    console.log(giver_password)
    console.log(recipient_name)
    step +=1
  }
  $afterPageLoad(() => {
    console.log($params.hash)
    hash = $params.hash
    api.get(`/hash/${hash}`).then((res) => { 
      console.log(res.data.coin)
      coin_id = res.data.coin.id
      travels = 1


      //coin = res.data.coin
      //if there is a handover, get handover and display form. if not, just display form and display instructions
      //if handover = coin.handover
      //travels = coin.travels
    
   //   recipientName = handover.recipient.name
     // giverName = handover.giver.name
      //lat = handover.lat
      //lon = handover.lon
      //console.log(coin)

    })
  })
</script>
<form class="form">
{#if step === 0}
  {#if handover_id == 0}
  <p><strong>Welcome!</strong> You are the first person to use this coin!
  <strong>Please read the instructions <strong>carefully</strong> and then click on "continue"!</strong></p>
  <Rules />
  <button on:click={next_step}>Continue</button>
  {/if}
  {#if handover_id == 1}
  <strong>Welcome!</strong> This coin has changed hands {travels} times so far! 
  <p>We assume you want to hand it over to a friend? Please make sure you read the instructions again before you continue!</p> 
  Here goes index.svelte - lets see how we can include that.
  {/if}
{:else if step === 1}

  <fieldset>
    <legend>Giving Person's Password</legend>
    <p>Now please enter the <strong>giving person's</strong> secret - We need to make sure that you didn't just find this coin somewhere. If you did, or if you forgot your password, please <a href='/contact'>contact</a> us (we're working on a reset password function)!
    </p>
    <label><span>Giving person's password</span>
      <input type="password" placeholder="Your name" bind:value={giver_password}>
    </label>
  </fieldset>
  <nav class="paging">
    <ul class="paging__list">
      <li class="previous" on:click={prev_step}><a>Previous</a></li>
      <li class="next"on:click={check_pass}><a>Afterwards</a></li>
    </ul>
  </nav>
 {:else if step === 2}
 <fieldset>
  <legend>Handover Entry</legend>
  <p>Now it's time to enter the name of the person <strong>receiving the coin</strong>, as well as their password and other data
  </p>
  <label><span>Receiving person's name</span>
    <input type="text" placeholder="Your name" bind:value={recipient_name}>
  </label>
  <label><span>Receiving person's e-mail address</span>
    <input type="text" placeholder="Your name" bind:value={recipient_email}>
  </label>
  <label><span>Receiving person's password</span>
    <input type="password" placeholder="Your name" bind:value={recipient_password}>
  </label>
  <label><span>Receiving person's password (again!)</span>
    <input type="password" placeholder="Your name" bind:value={recipient_password_again}>
  </label>
</fieldset>
<nav class="paging">
  <ul class="paging__list">
    <li class="previous" on:click={prev_step}><a>Previous</a></li>
    <li class="next"on:click={check_pass}><a>Afterwards</a></li>
  </ul>
</nav>
 {:else if step === 3}
 <fieldset>
   <legend>Handover Story</legend>
   <p> Now please tell us your story. It would be very nice of you if you could allow the phone to retrieve your location data! </p>
   <label><span>Your Story</span>
    <textarea bind:value={handover_text}></textarea>
 </fieldset>
 <nav class="paging">
  <ul class="paging__list">
    <li class="previous" on:click={prev_step}><a>Previous</a></li>
    <li class="next"on:click={check_pass}><a>Afterwards</a></li>
  </ul>
</nav>
{/if}
</form>