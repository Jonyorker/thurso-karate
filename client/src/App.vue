<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>


    <div class="wrapper">
      <div>
      <img alt="Vue logo" class="logo" src="@/assets/logo.jpg" width="125" height="125" />
      <HelloWorld msg="Thurso Karate" />
        </div>

      <nav>
        <RouterLink to="/">Accueil</RouterLink>
        <RouterLink to="/session">Session</RouterLink>
        <RouterLink to="/karateka">Karateka</RouterLink>
      </nav>
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

nav {
  width: 100%;
  font-size: 12px;
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
