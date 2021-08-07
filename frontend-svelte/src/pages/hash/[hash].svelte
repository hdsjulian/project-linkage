<script>
  import { url, params, afterPageLoad } from "@roxi/routify"
import { dataset_dev } from "svelte/internal";
import Rules from "../rules.svelte"
import api from "../../api";

  let hash
  let coin_id

  let handover_id = 0

  $afterPageLoad(() => {
    console.log($params.hash)
    hash = $params.hash
    api.get(`/hash/${hash}`).then((res) => { 
      console.log(res.data.coin)
      coin_id = res.data.coin.id
      handover_id = res.data.coin.handover.id
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

{#if handover_id == 0}
<p><strong>Welcome!</strong> You are the first person to use this coin!
<strong>Please read the instructions carefully and then click on "continue"!</strong></p>
{/if}
{#if handover_id >0}
<strong>Welcome!</strong> This coin has changed hands {travels} times so far! 
<p>We assume you want to hand it over to a friend? Please make sure you read the instructions again before you continue!</p> 
Here goes index.svelte - lets see how we can include that.
{/if}
<Rules />
blub
<button on:click={handover_id=1}>Continue</button>