import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/session',
      name: 'session',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/SessionView.vue')
    },
    {
      path: '/karateka',
      children: [
        { path: '', component: () => import('../views/KaratekaView.vue') },
        { path: 'create', component: () => import('../views/CreateKaratekaView.vue') },
        { path: 'list', component: () => import('../views/ListKaratekaView.vue') },
        { path: 'modify', component: () => import('../views/ModifyKaratekaView.vue') }
      ]
    }
  ]
})

export default router
