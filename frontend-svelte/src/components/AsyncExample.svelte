<script>
  import api from "../api"

  let getPosts = api.list("/posts")

  const addPost = async () => {
    await api.post("/posts", { title, author })
    getPosts = api.list("/posts") // triggers refresh
  }

  // declare form values
  let title
  let author

  // set default values
  title = `Random  ${Math.floor(Math.random() * 10000)}`
  author = "Tom"
</script>

<div class="async-example">
  <h4>Async examples</h4>

  <section>
    {#await getPosts}
      <p>Loading...</p>
    {:then posts}
      <ul>
        {#each posts as post}
          <li>Id: {post.id} | Title: {post.title} | Author: {post.author}</li>
        {/each}
      </ul>
    {:catch error}
      <p class="error"><b>Error</b> <small>{error.message}</small></p>
    {/await}
  </section>

  <section>
    <form on:submit|preventDefault={addPost}>
      <label>
        Title
        <input type="text" bind:value={title} />
      </label>

      <label>
        Author
        <input type="text" bind:value={author} />
      </label>

      <button type="submit">Add post</button>
    </form>
  </section>
</div>

<style>
  .async-example {
    border: 1px solid rgba(133, 4, 4, 0.5);
    color: rgb(119, 6, 6);
    background: rgba(158, 12, 12, 0.041);
    padding: 1em;
    margin: 1em 0;
  }

  section + section {
    border-top: 1px solid rgba(133, 4, 4, 0.5);
    margin-top: 1em;
    padding-top: 1em;
  }

  button {
    all: inherit;
    border: initial;
    display: inline-block;
    border-radius: 5px;
    background: rgba(158, 12, 12, 0.26);
    padding: 0.25em 1em;
    cursor: pointer;
  }

  button:hover {
    background: rgba(158, 12, 12, 0.432);
  }

  .error {
    padding: 0.25em 1em;
    background-color: rgba(236, 205, 205, 0.911);
  }
</style>
