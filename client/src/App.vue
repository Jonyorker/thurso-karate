<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>


    <div class="wrapper">
      <div class="grid grid-rows-3 md:grid-rows-2 grid-flow-col md:gap-4 md:px-4 md:py-4 leading-10">
          <div class="md:p-4 w-full rounded-xl row-span-1 md:row-span-2 flex justify-center items-center">
            <img alt="Vue logo" src="@/assets/logo.jpg" class="object-center h-24 w-24 md:object-contain" />
          </div>
          <div class="md:p-4 w-full rounded-xl col-span-1 md:col-span-2 flex items-center justify-center "><h1 class="text-4xl md:text-5xl font-bold">Thurso Karate</h1></div>
          <div class="md:p-4 w-full rounded-xl row-span-1 col-span-1 md:col-span-2 flex justify-center md:justify-start items-left">
            <nav>
        <RouterLink to="/">Accueil</RouterLink>
        <RouterLink to="/session">Session</RouterLink>
        <RouterLink to="/karateka">Karateka</RouterLink>
      </nav>
          </div>
      </div>


    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

h1 {
  color: red;
}

nav {
  font-size: 15px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}


</style>
